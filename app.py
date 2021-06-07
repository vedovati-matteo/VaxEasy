from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("basic/home.html")

@app.route('/login')
def login():
	return render_template("user_identification/login.html")

@app.route('/signin')
def signin():
	return render_template("user_identification/signin.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
