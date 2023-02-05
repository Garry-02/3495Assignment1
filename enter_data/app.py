from typing import List, Dict
from flask import Flask, request, render_template
import mysql.connector
import json

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/', methods=['GET','POST'])
def submit():
    msg = ''
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3307',
        'database': 'grades'
    }
    connection = mysql.connector.connect(**config)
    if request.method == 'POST' and 'user' in request.form and 'course1' in request.form:
        user = request.form['user']
        course1 = request.form['course1']
        course2 = request.form['course2']
        course3 = request.form['course3']
        course4 = request.form['course4']
        course5 = request.form['course5']
        cursor = connection.cursor()
        cursor.execute(''' INSERT INTO grades VALUES(NULL,%s,%s,%s,%s,%s,%s)''',(user,course1,course2,course3,course4,course5))
        connection.commit()
        cursor.close()
        msg = 'Success'
        return render_template('index.html', msg=msg), 201
    return render_template('index.html', msg=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
