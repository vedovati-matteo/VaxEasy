from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt  # flask.ext no longer exists
from flask_hashing import Hashing
from flask_resize import Resize
import os

app = Flask(__name__)
app.secret_key = "super secret key"

# funz da fare
def getPatologie ():
	return ('Prova1', 'Pippo', 'foo')

def getAppuntamenti ():
	return (
		{ "codice": "BG123","luogo": "fiera", "provincia":"BG", "data": "17/08/2021", "ora":"17.30" },
		{ "codice": "BG134","luogo": "fiera", "provincia":"BG", "data": "30/08/2021", "ora":"9.30" },
		{ "codice": "BG236","luogo": "albino", "provincia":"BG", "data": "02/09/2021", "ora":"19.00" },
		{ "codice": "BG401","luogo": "trescore", "provincia":"BG", "data": "06/09/2021", "ora":"12.00" }
	)

def getAppuntamento(codice):
	appuntamenti = (
		{ "codice": "BG123","luogo": "fiera", "provincia":"BG", "data": "17/08/2021", "ora":"17.30" },
		{ "codice": "BG134","luogo": "fiera", "provincia":"BG", "data": "30/08/2021", "ora":"9.30" },
		{ "codice": "BG236","luogo": "albino", "provincia":"BG", "data": "02/09/2021", "ora":"19.00" },
		{ "codice": "BG401","luogo": "trescore", "provincia":"BG", "data": "06/09/2021", "ora":"12.00" }
	)

	for a in appuntamenti:
		if a["codice"] == codice:
			return a
		return None

def getVaccini(cf):
	# controllo cf
	return (
		{ "codice": "CZ234", "nome": "COVID-19", "casaFarmaceutica":"Moderna", "descrizione": "prova prova", "richiamo": "1 mese"},
		{ "codice": "PF347", "nome": "COVID-19", "casaFarmaceutica":"Pfizer", "descrizione": "prova pippo", "richiamo": "1 mese"},
		{ "codice": "CZ586", "nome": "Tetano", "casaFarmaceutica": "Moderna", "descrizione": "17/08/2021", "richiamo": False},
		{ "codice": "MZ234", "nome": "Streptococco", "casaFarmaceutica":"Moderna", "descrizione": "17/08/2021", "richiamo": False}
	)

def setPrenotazione(cf, codPren, codVaccino):
	return True

def getPrenotazioni(cf):
	return (
		{ "codiceAppuntamento": "BG134","luogo": "fiera", "provincia":"BG", "data": "30/08/2021", "ora":"9.30", "codiceVaccino": "PF347", "nome": "COVID-19", "casaFarmaceutica":"Pfizer", "descrizione": "prova pippo", "richiamo": "1 mese" },
	)



# ====> HOME
@app.route('/')
def initPage():
    return redirect(url_for("home"))

@app.route('/home')
def home():
	return render_template("basic/home.html")


# ====> LOGIN
@app.route('/login')
def login():
	return render_template("user_identification/login.html")

@app.route('/landingLogin', methods=["POST"])
def landLogin():
	patologie = {}
	for a in getPatologie():
		patologie[a] = False

	campi = {
		"cf": request.form.get("cf"),
		"nome": "",
		"cognome": "",
		"provincia": "",
		"tel": "",
		"email": "",
		"pw": request.form.get("pw"),
		"patologie": patologie
	}
	session["user"] = {"cf": request.form.get("cf")}
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


# ====> SIGNIN
@app.route('/signin')
def signin():
	return render_template("user_identification/signin.html", patologie = getPatologie())

@app.route('/landingSignin', methods=["POST"])
def landSignin():
	
	patologie = {}
	for a in getPatologie():
		patologie[a] = (request.form.get(a) == 'on')

	campi = {
		"cf": request.form.get("cf"),
		"nome": request.form.get("nome"),
		"cognome": request.form.get("cognome"),
		"provincia": request.form.get("provincia"),
		"tel": request.form.get("tel"),
		"email": request.form.get("email"),
		"pw": request.form.get("pw"),
		"patologie": patologie
	}
	session["user"] = campi
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

# ====> PROFILO
@app.route('/profilo')
def profilo():
	return render_template("basic/profilo.html")


# ====> LOGOUT
@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for("home"))


# ====> PRENOTAZIONE
@app.route('/listaAppuntamenti')
def listaAppuntamenti():

	return render_template("prenotazione/listaAppuntamenti.html", appuntamenti=getAppuntamenti())

@app.route('/prenotazione', methods=["GET"])
def prenotazione():
	codice = request.args.get('codice')
	appuntamento = getAppuntamento(codice)

	if appuntamento is None:
		return redirect(url_for("listaAppuntamenti"))
	vaccini = getVaccini(session["user"]["cf"])
	return render_template("prenotazione/prenotazione.html", appuntamento = appuntamento, vaccini = vaccini)

@app.route('/prenota', methods=["POST", "GET"])
def prenota():
	codicePrenotazione = request.args.get('codice')
	codiceVaccino = request.form.get("codiceVaccino")
	if setPrenotazione(session["user"]["cf"], codicePrenotazione, codiceVaccino):
		return redirect(url_for("home"))
	else:
		return redirect(url_for("prenotazione"))
	
@app.route('/listaPrenotazioni')
def listaPrenotazioni():
	return render_template("prenotazione/listaPrenotazioni.html", prenotazioni=getPrenotazioni(session["user"]["cf"]))

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)





root = app.root_path
app.secret_key = "Very Strong Password"
app.config["RESIZE_URL"] = "/avatars"
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}/{}'.format(root, "db/vax.db")
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)


