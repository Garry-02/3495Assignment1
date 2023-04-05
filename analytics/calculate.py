from flask import Flask, flash, request, redirect, render_template
from flaskext.mysql import MySQL
import os
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "secret_key"

mysql = MySQL()

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("db_root_password")
app.config["MYSQL_DATABASE_DB"] = os.getenv("db_name")
app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_SERVICE_HOST")
app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("MYSQL_SERVICE_PORT"))
mysql.init_app(app)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='root',
                        authSource="admin")
    db = client["grades_db"]
    return db

@app.route("/analytics", methods=["GET"])
def show_form():
    return render_template('analytics.html')

@app.route("/", methods=["GET", "POST"])
def analytics():
    conn = mysql.connect()
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

    db = get_db()
    db.analytics.insert_one({
        "min_grade": min_value,
        "max_grade": max_value,
        "avg_grade": average_value
    })

    conn.close()
    return redirect('http://localhost:5002/results', code=301)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5005', debug=True)
