from model_utils.patologieVaccino import PatologiaVaccino
from model_utils.patologieUtente import PatologiaUtente
from model_utils.prenotazioni import Prenotazione
from model_utils.user import Utente
import jsonpickle
from app import db


# Generate fake database
def _placeholderVaccino_gen():
    codice1 = ("26248698","36890247","10254976")
    nome1 = ("Covid19", "Tetano","Pertosse")
    casaFarmatceutica1 = ("Pfizer", "Moderna", "Moderna")
    richiamo1 = (5, 15, -1)    # mesi dopo il quale è da fare il richiamo (-1 significa che non c'è richiamo)
    descrizione1 = ("Somministrazione singola 1mL", "Somministrazione singola 1.3mL", "Somministrazione singola 0.8mL")

    for codice, nome, casaFarmaceutica, richiamo, descrizione in zip(codice1, nome1, casaFarmatceutica1, richiamo1, descrizione1):
        db.session.add(Vaccino(codice, nome, casaFarmaceutica, richiamo, descrizione))
        db.session.commit()


# Class representing vax
class Vaccino(db.Model):
    codice = db.Column(db.String(8), unique=True, primary_key=True)
    nome = db.Column(db.Text(), nullable=False)
    casaFarmaceutica = db.Column(db.Text(), nullable=False)
    richiamo = db.Column(db.Integer(), nullable=False)
    descrizione = db.Column(db.Text(), nullable=False)

    def __init__(self, codice, nome, casaFarmaceutica, richiamo, descrizione):
        self.codice = codice
        self.nome = nome
        self.casaFarmaceutica = casaFarmaceutica
        self.richiamo = richiamo
        self.descrizione = descrizione

    def __repr__(self):
        return "Vaccino-{}: {} - {}".format(self.codice, self.nome, self.casaFarmaceutica, self.richiamo, self.descrizione)

    def __setstate__(self, state):
        self.__dict__.update(state)


def get_vax_from_json(json):    
    return jsonpickle.decode(json)


# Recover all vax in the database
def get_vax():
    return {vaccini.codice:vaccini for vaccini in Vaccino.query.all()}


# Recover a vax by its code
def get_vax_by_code(codice):
    return Vaccino.query.filter_by(codice=codice)



# Add a new vax to the database
def add_vax(new_code, new_name, new_casaFarmaceutica, new_richiamo, new_descrizione):
    db.session.add(Vaccino(new_code, new_name, new_casaFarmaceutica, new_richiamo, new_descrizione))
    db.session.commit()

def getVaccini(cf):   # ritorna tutti i vaccini possibili per l'utente dato il codice fiscale
    vaccini_tot = {vaccini.codice:vaccini for vaccini in Vaccino.query.all()}
    patologie = {cf:pat for pat in PatologiaUtente.query(PatologiaUtente.patologia).join(Utente, PatologiaUtente.cf).filter_by(cf=cf)}
    for vacc in PatologiaVaccino.query.join(Vaccino, PatologiaVaccino.codice_vaccino).all():
        if vacc.patologia not in patologie:
            vaccini_tot = True
        else:
            vaccini_tot = False
    
    vaccU = {}
    for tmp in vaccini_tot:    #corretto?
        if vaccini_tot[tmp] == True:
            vaccU[tmp] = Vaccino.query.filter_by(codice=tmp).all()

    return vaccU



