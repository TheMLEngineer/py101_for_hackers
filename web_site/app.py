#!/usr/bin/env python3

from flask import Flask, request, session, render_template_string
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a secret key for session management

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'test' and password == 'test':
            session['logged_in'] = True
            return 'Logged in successfully!'
        else:
            return 'Invalid credentials. Try again.'
    
    # This is the login form using Flask's template rendering
    return render_template_string('''<!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Login Page</title>
    </head>
    <body>
        <form action="" method="post">
            <label for="username">Username:</label>
            <input type="text" name="username" id="username" required>
            <br>
            <label for="password">Password:</label>
            <input type="password" name="password" id="password" required>
            <br>
            <input type="submit" value="Login">
        </form>
    </body>
    </html>''')

if __name__ == '__main__':
    app.run(debug=True, port=5000)