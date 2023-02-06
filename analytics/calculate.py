import mysql.connector
import os
from pymongo import MongoClient

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'grades'
}

connection = mysql.connector.connect(**config)

# if new data is added into the db, analytics should run

query_for_uid = "SELECT LAST(user_id) from GRADES;"
cursor_uid = connection.cursor()
user_id = cursor_uid.execute(query_for_uid)

cursor_uid.close()

cursor_for_grades = connection.cursor()
query_for_grades = "SELECT LAST(course1, course2, course3, course4, course5) from GRADES;"
cursor_for_grades.execute(query_for_grades)
grades = []
for grade in cursor_for_grades:
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

# Close the connections
cursor_for_grades.close()
connection.close()

client = MongoClient(os.environ["http://localhost:27017"])
db = client[os.environ["grades_db"]]

# Write the analytics to MongoDB
db.analytics.insert_one({
    "user_id": user_id, 
    "min_grade": min_value,
    "max_grade": max_value,
    "avg_grade": average_value
})


# sending the data to the mongo db 
