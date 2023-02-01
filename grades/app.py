from flask import Flask, render_template, request, make_response, g
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import os
import socket
import random
import json
import logging

app = Flask(__name__, template_folder='./templates', static_folder='./static')

app.secret_key = 'secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Password'
app.config['MYSQL_DB'] = 'grades'

mysql = MySQL(app)

""" 
cursor.execute('''  CREATE TABLE table_name(field1,field2) ''')
cursor.execute(''' INSERT INTO table_name (values) ''')
cursor.execute(''' DELETE FROM table_name WHERE condition ''')
mysql.connection.commit()
cursor.close()
"""

@app.route('/')
@app.route('/submit', methods=['GET','POST'])
def submit():
#    user_id = request.cookies.get('user_id')
#    if not user_id:
#        user_id = None
    msg = ''
    if request.method == 'POST' and 'user' in request.form and 'course1' in request.form:
        user = request.form['user']
        course1 = request.form['course1']
        course2 = request.form['course2']
        course3 = request.form['course3']
        course4 = request.form['course4']
        course5 = request.form['course5']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO grades VALUES(NULL,%s,%s,%s,%s,%s,%s)''',(user,course1,course2,course3,course4,course5))
        mysql.connection.commit()
        cursor.close()
        msg = 'Success'
        return render_template('index.html', msg=msg), 201

    return render_template('index.html'), 201


if __name__ == "__main__":
    app.run(host='localhost', app=5000, debug=True)
