from model_utils.patologieVaccino import PatologiaVaccino
from model_utils.patologieUtente import PatologiaUtente
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
    __tablename__ = "vaccino"
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
        return "{} - {} - {} - {} - {}".format(self.codice, self.nome, self.casaFarmaceutica, self.richiamo, self.descrizione)

    def __setstate__(self, state):
        self.__dict__.update(state)


def get_vax_from_json(json):    
    return jsonpickle.decode(json)


# Recover all vax in the database
def get_vax():
    return {vaccini.codice:vaccini for vaccini in Vaccino.query.all()}


# Recover a vax by its code
def get_vax_by_code(codice):
    return {vaccino.codice:vaccino for vaccino in Vaccino.query.filter_by(codice=codice).all()}



# Add a new vax to the database
def add_vax(new_code, new_name, new_casaFarmaceutica, new_richiamo, new_descrizione):
    db.session.add(Vaccino(new_code, new_name, new_casaFarmaceutica, new_richiamo, new_descrizione))
    db.session.commit()

def getVaccini(cf):   # ritorna tutti i vaccini possibili per l'utente dato il codice fiscale
    vaccini_tot = {vaccini.codice:vaccini for vaccini in Vaccino.query.all()}
    patologie = []   #tutte le patologie dell'utente
    for pat in PatologiaUtente.query.filter_by(cf=cf).all():
        patologie.append(pat.patologia)

    print("=======patologie utente=======")
    print(patologie)

    noVax = []
    for vacc in PatologiaVaccino.query.all():
        for i in range(len(patologie)):
            if vacc.patologia == patologie[i]:
                flag = True
                break
        if flag == True:
            noVax.append(vacc.codice_vaccino)
        flag = False

    vaccU = []
    
    print("=======lista vaccini da non fare=======")
    print(noVax)

    for tmp in vaccini_tot: 
        flag = False
        c = 0
        for i in range(len(noVax)):
            if noVax[i] in tmp:
                flag = True
                c = i
                break
        if flag == False:
            vaccU.append(get_vax_by_code(tmp))

    return vaccU



