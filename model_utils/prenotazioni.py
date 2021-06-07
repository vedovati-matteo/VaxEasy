import jsonpickle
from app import db


# Class representing users
class Prenotazione(db.Model):
    cf = db.Column(db.Text(), db.ForeignKey("User.cf"), primary_key=True)
    vaccino = db.Column(db.Text(), db.ForeignKey("Vaccino.codice"), primary_key=True)
    codice_appuntamento = db.Column(db.Text(), db.ForeignKey("Appuntamento.codice"), primary_key=True)

    def __init__(self, cf, vaccino, codice_appuntamento):
        self.cf = cf
        self.vaccino = vaccino
        self.codice_appuntamento = codice_appuntamento

    def __repr__(self):
        return "Appuntamento-{}: {} - {}".format(self.cf, self.get_full_name(), self.password)

    # Method to get the user full name
    def get_full_name(self):
        return "{nome} {cognome}".format(cognome=self.cognome, nome=self.nome)

    # Method to convert a user in JSON format to store it in session["user"]
    def to_json(self):
        return jsonpickle.encode(self)

    def __setstate__(self, state):
        self.__dict__.update(state)


# Create a User object from its json representation in session["user"]
def get_user_from_json(json):
    return jsonpickle.decode(json)


# Recover all users in the database
def get_users():
    return {user.cf:user for user in Utente.query.all()}


# Recover a user by its CF
def get_user_by_cf(cf):
    return Utente.query.filter_by(cf=cf).first()



# Add a new user to the database
def add_user(new_cf, new_nome, new_cognome, new_email, new_cell, new_prov):
    db.session.add(Utente(new_cf, new_nome, new_cognome, new_email, new_cell, new_prov))
    db.session.commit()


