import jsonpickle
from app import db


# Generate fake database
def _placeholderVaccinoMalattia_gen():
    codice_vaccino1 = ("26248698","36890247","36890247","10254976")
    malattia1 = ("Covid19", "MeningococcoB", "Pertosse", "Covid19")

    for codice_vaccino, malattia in zip(codice_vaccino1, malattia1):
        db.session.add(VaccinoMalattia(codice_vaccino, malattia))
        db.session.commit()



# Class representing vaccinoMalattia
class VaccinoMalattia(db.Model):
    __tablename__ = "vaccinoMalattia"
    codice_vaccino = db.Column(db.String(8), db.ForeignKey("vaccino.codice"), primary_key=True)
    malattia = db.Column(db.Text(), db.ForeignKey("malattia.nome"), primary_key=True)

    def __init__(self, codice_vaccino, malattia):
        self.codice_vaccino = codice_vaccino
        self.malattia = malattia

    def __repr__(self):
        return "VaccinoMalattia-{}: {}".format(self.codice_vaccino, self.malattia)

    def to_json(self): 
        return jsonpickle.encode(self)

    def __setstate__(self, state):
        self.__dict__.update(state)


# Add a new vaccinoMalattia to the database
def add_vaccinoMalattia(new_codice_vaccino, new_malattia):
    db.session.add(VaccinoMalattia(new_codice_vaccino, new_malattia))
    db.session.commit()


