from model_utils.patologie import Patologia
from model_utils.patologieUtente import PatologiaUtente
import jsonpickle
from app import db

# Generate fake database
def _placeholderUtente_gen():
    cf1 = ("RSSMRC21A01A794Y","VRDLCU05A01A794I","BNCLSN66M01F205M","BNTCRL93M41B157N")
    nome1 = ("Marco", "Luca", "Alessandro", "Carla")
    cognome1 = ("Rossi", "Verdi", "Bianchi", "Bonetti")
    email1 = ("marco.rossi@unibg.it", "luca.verdi@unibg.it", "alessandro.bianchi@unibg.it", "carlo.bonetti@unibg.it")
    telefono1 = ("3270811789", "3364569875", "3394896573", "3452169574")
    provincia1 = ("Bergamo","Bergamo","Milano","Brescia")

    for cf, nome, cognome, email, telefono, provincia in zip(cf1, nome1, cognome1, email1, telefono1, provincia1):
        db.session.add(Utente(cf, nome, cognome, email, telefono, provincia))
        db.session.commit()




# Class representing users
class Utente(db.Model):
    __tablename__ = "utente"
    cf = db.Column(db.String(16), unique=True, primary_key=True)
    nome = db.Column(db.Text(), nullable=False)
    cognome = db.Column(db.Text(), nullable=False)
    password = db.relationship("Password", backref="utente", cascade="all,delete",lazy=False, uselist=False)
    mail = db.Column(db.Text(), nullable=False)
    telefono = db.Column(db.String(10), nullable=False)
    provincia = db.Column(db.Text(), nullable=False)

    def __init__(self, cf, nome, cognome, mail, telefono, provincia):
        self.cf = cf
        self.nome = nome
        self.cognome = cognome
        self.mail = mail
        self.telefono = telefono
        self.provincia = provincia

    def __repr__(self):
        return "Utente-{}: {} - {}".format(self.cf, self.get_full_name(), self.password)

    # Method to get the user full name
    def get_full_name(self):
        return "{nome} {cognome}".format(cognome=self.cognome, nome=self.nome)

    # Method to convert a user in JSON format to store it in session["user"]
    def to_json(self):
        return jsonpickle.encode(self)

    def __setstate__(self, state):
        self.__dict__.update(state)

    # non vogliamo che nel cookie compaiano le seguente cose
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['password']
        del state["_sa_instance_state"]  # fa parte di db.model
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)


# Create a User object from its json representation in session["user"]
def get_user_from_json(json):   
    return jsonpickle.decode(json)


# Recover all users in the database
def get_users():
    return {user.cf:user for user in Utente.query.all()}


# Recover a user by its CF with patologie
def get_user_by_cf(cf1):
    patologie = {Patologia.nome:nome for nome in Patologia.query.select(Patologia.nome)}
    for pat in Utente.query(Patologia.nome).join(Utente,PatologiaUtente.cf).filter_by(cf=cf1):
        if(PatologiaUtente.query.filter_by(cf = cf1)!=None):
            patologie[pat.nome] = True
        else:
            patologie[pat.nome] = False
        
    return {Utente.query.filter_by(cf=cf1).all(),patologie}



# Add a new user to the database
def add_user(new_cf, new_nome, new_cognome, new_email, new_cell, new_prov):
    db.session.add(Utente(new_cf, new_nome, new_cognome, new_email, new_cell, new_prov))
    db.session.commit()


