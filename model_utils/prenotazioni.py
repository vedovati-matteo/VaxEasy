import jsonpickle
from app import db


# Generate fake database
def _placeholderPrenotazione_gen():
    cf1 = ("RSSMRC21A01A794Y","VRDLCU05A01A794I","BNCLSN66M01F205M","BNTCRL93M41B157N")
    vaccino1 = ("26248698", "36890247", "10254976", "26248698")
    codice_appuntamento1 = ("36740", "20506", "13005", "13287")

    for cf, vaccino, codice_appuntamento in zip(cf1, vaccino1, codice_appuntamento1):
        db.session.add(Prenotazione(cf, vaccino, codice_appuntamento))
        db.session.commit()



# Class representing prenotazione
class Prenotazione(db.Model):
    cf = db.Column(db.String(16), db.ForeignKey("Utente.cf"), primary_key=True)
    vaccino = db.Column(db.String(8), db.ForeignKey("Vaccino.codice"), primary_key=True)
    codice_appuntamento = db.Column(db.String(5), db.ForeignKey("Appuntamento.codice"), primary_key=True)

    def __init__(self, cf, vaccino, codice_appuntamento):
        self.cf = cf
        self.vaccino = vaccino
        self.codice_appuntamento = codice_appuntamento

    def __repr__(self):
        return "Prenotazione-{}: {} - {}".format(self.cf, self.vaccino, self.codice_appuntamento)

    def to_json(self): 
        return jsonpickle.encode(self)

    def __setstate__(self, state):
        self.__dict__.update(state)


# recupera tutte le prenotazioni di un utente
def get_prenotazione_by_cf(cf):
    return Prenotazione.query.filter_by(cf=cf)


# Add a new prenotazione to the database
def add_prenotazione(new_cf, new_vaccino, new_codice_appuntamento):
    db.session.add(Prenotazione(new_cf, new_vaccino, new_codice_appuntamento))
    db.session.commit()


