from typing import List, Dict
from flask import Flask, request, render_template, redirect
import mysql.connector.pooling
import os

app = Flask(__name__)
app.secret_key = 'secret key'
config = {
    'user': 'root',
    'password': 'root',
    'host': 'mysql-db',
    'port': '3306',
    'auth_plugin': 'mysql_native_password',
    'database': os.environ.get('MYSQL_DB')
}
cnxpool = pooling.MySQLConnectionPool(**config)


@app.route('/')
def home():
    return "Hello world!"


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    msg = ''
    if request.method == 'POST' and 'user' in request.form and 'course1' in request.form:
        try:
            cnx = cnxpool.get_connection()
            cursor = cnx.cursor()
            user = request.form['user']
            course1 = request.form['course1']
            course2 = request.form['course2']
            course3 = request.form['course3']
            course4 = request.form['course4']
            course5 = request.form['course5']
            cursor.execute(
                '''INSERT INTO grades VALUES(NULL,%s,%s,%s,%s,%s,%s)''',
                (user, course1, course2, course3, course4, course5))
            cnx.commit()
            cursor.close()
            cnx.close()
            msg = 'Success'
            return redirect('http://localhost:5005', code=301)
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            msg = 'Error: {}'.format(err)
    return render_template('index.html', msg=msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
