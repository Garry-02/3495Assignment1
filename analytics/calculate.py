import mysql.connector
import pymongo
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

    
client = MongoClient(os.environ["MONGO_DB_URI"])
db = client[os.environ["MONGO_DB_NAME"]]

# Write the analytics to MongoDB
db.analytics.insert_one({
    "min_grade": min_value,
    "max_grade": max_value,
    "avg_grade": average_value
})

# Close the connections
cursor.close()
connection.close()
# sending the data to the mongo db 