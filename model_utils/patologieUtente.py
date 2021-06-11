import jsonpickle
from app import db


# Generate fake database
def _placeholderPatologiaUtente_gen():
    cf1 = ("RSSMRC21A01A794Y","VRDLCU05A01A794I","BNCLSN66M01F205M","BNTCRL93M41B157N")
    patologia1 = ("Diabete", "Ipertensione", "Diabete", "Diabete")

    for cf, patologia in zip(cf1, patologia1):
        db.session.add(PatologiaUtente(cf, patologia))
        db.session.commit()



# Class representing patologia
class PatologiaUtente(db.Model):
    cf = db.Column(db.String(16), db.ForeignKey("Utente.cf"), primary_key=True)
    patologia = db.Column(db.Text(), db.ForeignKey("Patologia.nome"), primary_key=True)

    def __init__(self, cf, patologia):
        self.cf = cf
        self.patologia = patologia

    def __repr__(self):
        return "PatologiaUtente-{}: {} - {}".format(self.cf, self.patologia)

    def to_json(self): 
        return jsonpickle.encode(self)

    def __setstate__(self, state):
        self.__dict__.update(state)


# Add a new patologia to the database
def add_prenotazione(new_cf, new_patologia):
    db.session.add(PatologiaUtente(new_cf, new_patologia))
    db.session.commit()


