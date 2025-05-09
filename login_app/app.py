from flask import Flask, render_template, request

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "pass123"

@app.route("/", methods=["GET"])
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    user = request.form["username"]
    pwd = request.form["password"]
    if user == USERNAME and pwd == PASSWORD:
        return "<h1>Login Successful! Welcome to the dashboard.</h1>"
    else:
        return "<h1>Login Failed. Try Again.</h1>"

if __name__ == "__main__":
    app.run(debug=True)
