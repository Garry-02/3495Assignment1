# reading the data from the sql database

# perform simple calculations on the data
#def calculator(data): 
#    max_value = 0
#    min_value = 100
#    sum_of_percentages = 0
#    number_of_percantages = 0 

#    for data in data_from_database:
#        if data[value] > max_value:
#            max_value=data[value]
#        if data[value] < min_value:
#            min_value=data[min_value]

#        sum_of_percentages += data[value]
#        number_of_percantages += 1

#    average_value = sum_of_percentages/number_of_percantages

#    return max_value, min_value, average_value

# sending the data to the mongo db 


from typing import List, Dict
from flask import Flask, request, render_template
import mysql.connector
import json

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def home():
    return "Hello world!"

@app.route('/submit', methods=['GET','POST'])
def submit():
    msg = ''
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'grades'
    }
