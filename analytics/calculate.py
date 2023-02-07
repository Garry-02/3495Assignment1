from flask import Flask, flash, request, redirect, render_template
import mysql.connector
import os
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "secret_key"


#@app.route("/analytics", methods=["GET"])
#def show_form():
#    return render_template('analytics.html')
       
def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["grades"]
    return db

@app.route("/analytics", methods=["GET", "POST"])
def analytics():
    config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'grades'
    }
    if request.method == "POST":
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        username = request.form['user']
        query = f"""SELECT course1, course2, course3, course4, course5 from grades where user_id='{username}';"""
        cursor.execute(query)
        grades = cursor.fetchall()
        grades = list(grades[0])


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

        #client = MongoClient(os.environ["http://localhost:27017"])
        #db = client[os.environ["grades_db"]]
        
        db = get_db()        
        db.analytics.insert_one({
            "min_grade": min_value,
            "max_grade": max_value,
            "avg_grade": average_value
        })
        return "Analytics written to MongoDB", 201

    return render_template('analytics.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5005', debug=True)
