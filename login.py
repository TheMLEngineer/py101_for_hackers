from flask import Flask, request, session; import os; app = Flask(__name__); app.secret_key = os.urandom(24); @app.route("/", methods=["GET", "POST"]) def login(): if request.method == "POST": username = request.form["username"] password = request.form["password"] if username == "test" and password == "test": session["logged_in"] = True return "Logged in successfully!" else: return "Invalid credentials. Try again." return """ <form action="" method="post"> <input type="text" name="username" placeholder="Username" required> <input type="password" name="password" placeholder="Password" required> <input type="submit" value="Login"> </form> """; if __name__ == "__main__": app.run(debug=True, port=5000)