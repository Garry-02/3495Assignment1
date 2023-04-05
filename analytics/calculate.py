from flask import Flask, flash, request, redirect, render_template
import mysql.connector
import os
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "secret_key"


#@app.route("/analytics", methods=["GET"])
#def show_form():
#    return render_template('analytics.html')
       
def get_mysql_conn():
    mysql_host = os.environ.get('MYSQL_HOST')
    mysql_user = os.environ.get('MYSQL_USER')
    mysql_password = os.environ.get('MYSQL_PASSWORD')
    mysql_db = os.environ.get('MYSQL_DATABASE')

    conn = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_db
    )

    return conn

@app.route("/", methods=["GET", "POST"])
def analytics():
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = "SELECT course1, course2, course3, course4, course5 from grades;"
    cursor.execute(query)
    res = cursor.fetchall()
    grades = []
    for data in res:
        for grade in data:
            grades.append(grade)
    max_value = 0
    min_value = 100
    sum_of_grades = 0
    number_of_grades = 0
    for grade in grades:
        if grade > max_value:
            max_value=grade
        if grade < min_value:
            min_value=grade
        sum_of_grades += grade
        number_of_grades += 1

    average_value = sum_of_grades/number_of_grades

    db = get_mysql_conn()
    db.analytics.insert_one({
        "min_grade": min_value,
        "max_grade": max_value,
        "avg_grade": average_value
    })

    conn.close()
    return redirect('http://localhost:5002/results', code=301)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5005', debug=True)
