import jsonpickle
from app import db


# Class representing users
class Prenotazione(db.Model):
    cf = db.Column(db.Text(), db.ForeignKey("User.cf"), primary_key=True)
    vaccino = db.Column(db.Text(), db.ForeignKey("Vaccino.codice"), primary_key=True)
    codice_appuntamento = db.Column(db.Integer(), db.ForeignKey("Appuntamento.codice"), primary_key=True)

    def __init__(self, cf, vaccino, codice_appuntamento):
        self.cf = cf
        self.vaccino = vaccino
        self.codice_appuntamento = codice_appuntamento

    def __repr__(self):
        return "Prenotazione-{}: {} - {}".format(self.cf, self.vaccino, self.codice_appuntamento)

    def to_json(self):    # lasciare o togliere?
        return jsonpickle.encode(self)

    def __setstate__(self, state):
        self.__dict__.update(state)


