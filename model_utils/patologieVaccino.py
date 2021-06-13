import jsonpickle
from app import db


# Generate fake database
def _placeholderPatologiaVaccino_gen():
    codice_vaccino1 = ("26248698","36890247","36890247","10254976")
    patologia1 = ("Diabete", "Ipertensione", "Diabete", "Diabete")

    for codice_vaccino, patologia in zip(codice_vaccino1, patologia1):
        db.session.add(PatologiaVaccino(codice_vaccino, patologia))
        db.session.commit()



# Class representing patologia
class PatologiaVaccino(db.Model):
    codice_vaccino = db.Column(db.String(8), db.ForeignKey("vaccino.codice"), primary_key=True)
    patologia = db.Column(db.Text(), db.ForeignKey("patologia.nome"), primary_key=True)

    def __init__(self, codice_vaccino, patologia):
        self.codice_vaccino = codice_vaccino
        self.patologia = patologia

    def __repr__(self):
        return "PatologiaVaccino-{}: {}".format(self.codice_vaccino, self.patologia)

    def to_json(self): 
        return jsonpickle.encode(self)

    def __setstate__(self, state):
        self.__dict__.update(state)


# Add a new patologia to the database
def add_prenotazione(new_codice_vaccino, new_patologia):
    db.session.add(PatologiaVaccino(new_codice_vaccino, new_patologia))
    db.session.commit()


