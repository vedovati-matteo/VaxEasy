from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt  # flask.ext no longer exists
from flask_hashing import Hashing
from flask_resize import Resize
import os

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def initPage():
    return redirect(url_for("home"))

@app.route('/home')
def home():
	return render_template("basic/home.html")

@app.route('/login')
def login():
	return render_template("user_identification/login.html")

@app.route('/signin')
def signin():
	return render_template("user_identification/signin.html")

@app.route('/landing', methods=["POST"])
def land():
	
	session["user"] = request.form.get("cf")
	return redirect(url_for("home"))

	"""# Recover the user by its username
	logged_user = getUserByCf(request.form.get("cf"))

	# If a user has been recovered
	if logged_user:
		# Check that the provided password its correct
		if checkPassword(logged_user.cf, request.form.get("pw")):
			# Create a Flask session for the logged user
			session["user"] = logged_user.to_json()
			return render_template("login/logged.html", user=logged_user)
	return redirect(url_for("home"))"""

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)





root = app.root_path
app.secret_key = "Very Strong Password"
app.config["UPLOAD_FOLDER"] = os.path.join(root, "uploads")
app.config["RESIZE_URL"] = "/avatars"
app.config["RESIZE_ROOT"] = os.path.join(root, "uploads")
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}/{}'.format(root, "db/vax.db")
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
