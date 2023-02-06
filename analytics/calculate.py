from flask import Flask, flash, request, redirect, render_template
import mysql.connector
import os
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "secret_key"

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'grades'
}

@app.route("/analytics", methods=["GET"])
def show_form():
    return render_template('analytics.html')
       
@app.route("/calculate", methods=["POST"])
def analytics():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    query = "SELECT course1, course2, course3, course4, course5 from GRADES where user_id is {user_id};"
    cursor.execute(query)
    grades = []
    for grade in cursor:
        grades.append(grade)

    max_value = 0
    min_value = 100
    sum_of_grades = 0
    number_of_grades = 0
    for grade in grades:
        for data in grades:
            if data > max_value:
                max_value=data
            if data < min_value:
                min_value=data
            sum_of_grades += data
            number_of_grades += 1

        average_value = sum_of_grades/number_of_grades

    client = MongoClient(os.environ["http://localhost:27017"])
    db = client[os.environ["grades_db"]]
    db.analytics.insert_one({
        "min_grade": min_value,
        "max_grade": max_value,
        "avg_grade": average_value
    })
    cursor.close()
    connection.close()
    return "Analytics written to MongoDB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5005', debug=True)
