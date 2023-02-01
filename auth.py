import os
from app import app
import urllib.request
import json
from flask import Flask, flash, request, redirect, url_for, render_template

app.secret_key = "secret_key"

@app.route('/authenticate', methods=['GET'])
def show_form():
    return render_template('auth.html')
       

@app.route('/authenticate', methods=['POST'])
def authenticate():
    with open('users.json', 'r') as f:
            data = json.load(f)
    username = request.form['user']
    password = request.form['pass']
    usernames = []
    passwords = []
    for user in data:
        uname = data[user]['user']
        passw = data[user]['password']
        usernames.append(uname)
        passwords.append(passw)

    if username in usernames and password in passwords:
        return redirect('/submit', 307) #redirect to the app page once its ready 
    else:
        flash('Authentication failed')
        return render_template('auth.html') # for incorrect authentication


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['pass']
        with open('users.json', 'r') as f:
            data = json.load(f)
        user_ids = data.keys()
        int_user_ids = []
        for id in user_ids:
            int_user_ids.append(int(id))
        new_user = max(int_user_ids) + 1
        data[new_user] = {"user": username, "password": password}
        json_string = json.dumps(data)
        with open('users.json', 'w') as f:
            f.write(json_string)
        flash('User created!')
        return render_template('auth.html')



if __name__ == '__main__':
    app.run(port=5002)