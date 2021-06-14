from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt  # flask.ext no longer exists
from flask_hashing import Hashing
from flask_resize import Resize



import os

app = Flask(__name__)
app.secret_key = "super secret key"

root = app.root_path
app.config["RESIZE_URL"] = "/avatars"
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}/{}'.format(root, "db/vax.db")
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)





# ______funz da fare

def getUserByCf(cf): # ritorna i campi dato il cf   -> FUNZIONA user.py get_user_by_cf() (torno lista sennò dizionario crea problemi)
	patologie = {}
	for a in getPatologie():
		patologie[a] = False
	
	campi = {
		"cf": cf,
		"nome": "",
		"cognome": "",
		"provincia": "",
		"tel": "",
		"email": "",
		"patologie": patologie
	}
	return campi # se non c'è: return False

def checkPassword(cf, pw): # controlla la password (con hash)   -> password_handler.py - check_password()
	return True

def getPatologie (): # ritorna la lista di patologie (solo nome) -> FUNZIONA patologie.py - get_patologia()
	return ('Prova1', 'Pippo', 'foo')

def createUser(campi): # crea un user con i campi specificati e ritorna True se è avvenuto con successo, altrimenti False  -> user.py - add_user()
	return True

def getAppuntamenti (provincia): # ritorna tutti gli appuntamenti disponibili per una provincia  -> FUNZIONA appuntamenti.py - get_appuntamentoByProvincia()
	return (
		{ "codice": "BG123","luogo": "fiera", "provincia":"BG", "data": "17/08/2021", "ora":"17.30" },
		{ "codice": "BG134","luogo": "fiera", "provincia":"BG", "data": "30/08/2021", "ora":"9.30" },
		{ "codice": "BG236","luogo": "albino", "provincia":"BG", "data": "02/09/2021", "ora":"19.00" },
		{ "codice": "BG401","luogo": "trescore", "provincia":"BG", "data": "06/09/2021", "ora":"12.00" }
	)

def getAppuntamento(codice): # ritorna il singolo appuntamento dato il codice   -> FUNZIONA appuntamenti.py - get_appuntamento_by_code()
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

def getVaccini(cf): # ritorna tutti i vaccini possibili per l'utente dato il codice fiscale
	# controllo cf    -> FUNZIONA vaccini.py - getVaccini()
	return (
		{ "codice": "CZ234", "nome": "COVID-19", "casaFarmaceutica":"Moderna", "descrizione": "prova prova", "richiamo": "1 mese"},
		{ "codice": "PF347", "nome": "COVID-19", "casaFarmaceutica":"Pfizer", "descrizione": "prova pippo", "richiamo": "1 mese"},
		{ "codice": "CZ586", "nome": "Tetano", "casaFarmaceutica": "Moderna", "descrizione": "17/08/2021", "richiamo": False},
		{ "codice": "MZ234", "nome": "Streptococco", "casaFarmaceutica":"Moderna", "descrizione": "17/08/2021", "richiamo": False}
	)

def setPrenotazione(cf, codPren, codVaccino): # dato il codice fiscale, codice della prenotazione e codice del vaccino crea una prenotazione, ritorna True se avvenuta altrimenti False
	return True    # -> FUNZIONA prenotazioni.py - setPrenotazione()

def getPrenotazioni(cf): # ritorna le prenotazione dell'utente dato codice fiscale   -> FUNZIONA prenotazione.py - getPrenotazioni()	
	return (
		{ "codiceAppuntamento": "BG134","luogo": "fiera", "provincia":"BG", "data": "30/08/2021", "ora":"9.30", "codiceVaccino": "PF347", "nome": "COVID-19", "casaFarmaceutica":"Pfizer", "descrizione": "prova pippo", "richiamo": "1 mese" },
	)

# ______fine funz da fare

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

	campi = get_user_by_cf(request.form.get("cf"))

	if len(campi[0]) > 0:
		# check password
		if check_password(campi[0][0].cf, request.form.get("pw")):
			par = {
				"cf": campi[0][0].cf,
				"nome": campi[0][0].nome,
				"cognome": campi[0][0].cognome,
				"provincia": campi[0][0].provincia,
				"tel": campi[0][0].telefono,
				"email": campi[0][0].mail,
				"patologie": campi[1]
			}
			session["user"] = par
			return redirect(url_for("home"))
	
	return redirect(url_for("login"))


# ====> SIGNIN
@app.route('/signin')
def signin():
	return render_template("user_identification/signin.html", patologie = get_patologia())

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
		"patologie": patologie
	}

	add_user(
		request.form.get("cf"),
		request.form.get("nome"),
		request.form.get("cognome"),
		request.form.get("email"),
		request.form.get("tel"),
		request.form.get("provincia"),
		request.form.get("pw"),
		patologie
	)
	return redirect(url_for("login"))	
	"""
	if createUser(campi):
		return redirect(url_for("login"))
	else:
		return redirect(url_for("signin"))
	"""

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
	print("=============Z")
	print(get_appuntamentoByProvincia("Bergamo"))
	return render_template("prenotazione/listaAppuntamenti.html", appuntamenti=getAppuntamenti(session["user"]["provincia"]))

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
	from model_utils.patologie import get_patologia
	from model_utils.user import get_user_by_cf, check_password, add_user
	from model_utils.appuntamenti import get_appuntamentoByProvincia
	app.run(host='127.0.0.1', port=5000, debug=True)
	







