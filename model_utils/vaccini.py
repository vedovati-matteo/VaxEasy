import jsonpickle
from app import db


# Class representing users
class Vaccino(db.Model):
    codice = db.Column(db.Text(), unique=True, primary_key=True)
    nome = db.Column(db.Text(), nullable=False)
    descrizione = db.Column(db.Text(), nullable=False)

    def __init__(self, codice, nome, descrizione):
        self.codice = codice
        self.nome = nome
        self.descrizione = descrizione

    def __repr__(self):
        return "Vaccino-{}: {} - {}".format(self.codice, self.nome, self.descrizione)

    def __setstate__(self, state):
        self.__dict__.update(state)


def get_vax_from_json(json):    # lasciare o togliere?
    return jsonpickle.decode(json)


# Recover all vax in the database
def get_vax():
    return {vaccini.codice:vaccini for vaccini in Vaccino.query.all()}


# Recover a vax by its code
def get_vax_by_code(cf):
    return Vaccino.query.filter_by(codice=codice).first()



# Add a new vax to the database
def add_user(new_code, new_nome, new_description):
    db.session.add(Vaccino(new_code, new_nome, new_description))
    db.session.commit()


