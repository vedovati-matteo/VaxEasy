from flask import Flask, render_template, request, session, redirect, url_for

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
