from flask import Flask, render_template, request, make_response, g
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import os
import socket
import random
import json
import logging

app = Flask(__name__, template_folder='./templates', static_folder='./static')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass'
app.config['MYSQL_DB'] = 'grades'
mysql = MySQL(app)

""" 
cursor.execute('''  CREATE TABLE table_name(field1,field2) ''')
cursor.execute(''' INSERT INTO table_name (values) ''')
cursor.execute(''' DELETE FROM table_name WHERE condition ''')
mysql.connection.commit()
cursor.close()
"""

@app.route('/gpa', methods=['POST','GET'])
def hello():
    user_id = request.cookies.get('user_id')
    if not user_id:
        user_id = None
    
    vote = None

    if request.method == 'POST':
        course1 = request.form['course1']
        course2 = request.form['course2']
        course3 = request.form['course3']
        course4 = request.form['course4']
        course5 = request.form['course5']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(course1,course2,course3,course4,course5))
        mysql.connection.commit()
        cursor.close()
        return render_template('gpa_calc.html'), 201

app.run(host='localhost', app=5000)

if __name__ == "__main__":
    app.run(debug=True)