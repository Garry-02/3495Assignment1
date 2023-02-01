from flask import Flask, render_template, request, make_response, g
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import os
import socket
import random
import json
import logging

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass'
app.config['MYSQL_DB'] = 'grades'

mysql = MySQL(app)

cursor = mysql.connection.cursor()

cursor.execute('''  CREATE TABLE table_name(field1,field2) ''')
cursor.execute(''' INSERT INTO table_name (values) ''')
cursor.execute(''' DELETE FROM table_name WHERE condition ''')




mysql.connection.commit()

cursor.close()