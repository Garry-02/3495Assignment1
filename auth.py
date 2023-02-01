import os
from app import app
import urllib.request
import json
from flask import Flask, flash, request, redirect, url_for, render_template


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
        return redirect('http://google.com', 307)
    else:
        flash('Authentication failed')
        return render_template('auth.html')


if __name__ == '__main__':
    app.run(port=5002)