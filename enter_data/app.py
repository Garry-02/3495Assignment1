"""Code for a flask API to Create, Read, Update, Delete users"""
import os
from flask import jsonify, request, Flask, render_template, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("db_root_password")
app.config["MYSQL_DATABASE_DB"] = os.getenv("db_name")
app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_SERVICE_HOST")
app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("MYSQL_SERVICE_PORT"))
mysql.init_app(app)


@app.route('/')
def home():
    return "Hello world!"


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    msg = ''
    if request.method == 'POST' and 'user' in request.form and 'course1' in request.form:
        conn = mysql.connect()
        cursor = conn.cursor()
        user = request.form['user']
        course1 = request.form['course1']
        course2 = request.form['course2']
        course3 = request.form['course3']
        course4 = request.form['course4']
        course5 = request.form['course5']
        cursor.execute(
            '''INSERT INTO grades VALUES(NULL,%s,%s,%s,%s,%s,%s)''',
            (user, course1, course2, course3, course4, course5))
        conn.commit()
        cursor.close()
        conn.close()
        msg = 'Success'
        return redirect('http://localhost:5005', code=301)
    return render_template('index.html', msg=msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
