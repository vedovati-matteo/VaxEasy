import jsonpickle
from app import db

# Generate fake database
def _placeholderAppuntamento_gen():
    codice1 = ("36740","20506","13005","13287")
    data1 = ("Covid19", "MeningococcoB", "Pertosse")
    ora1 = ("Somministrazione singola 1mL", "Somministrazione singola 1.3mL", "Somministrazione singola 0.8mL")
    id_centroVacc1 = ("BG160","BS893","MI645","BG160")

    for codice, data, ora, id_centroVacc in zip(codice1, data1, ora1, id_centroVacc1):
        db.session.add(Appuntamento(codice, data, ora, id_centroVacc))
        db.session.commit()



# Class representing appuntamento
class Appuntamento(db.Model):
    codice = db.Column(db.String(5), unique=True, primary_key=True)
    data = db.Column(db.Date(), nullable=False)
    ora = db.Column(db.Time(), nullable=False)
    id_centroVacc = db.Column(db.Text(), db.ForeignKey("centriVaccinali.id_centroVacc"), nullable=False)

    def __init__(self, codice, data, ora, id_centroVacc):
        self.codice = codice
        self.data = data
        self.ora = ora
        self.id_centroVacc = id_centroVacc

    def __repr__(self):
        return "Appuntamento-{}: {} - {}".format(self.codice, self.data, self.ora, self.id_centroVacc)

    def __setstate__(self, state):
        self.__dict__.update(state)

def get_appuntamento_from_json(json): 
    return jsonpickle.decode(json)


# Recover all appuntamento in the database
def get_appuntamento():
    return {appuntamenti.codice:appuntamenti for appuntamenti in Appuntamento.query.all()}


# Recover a appuntamento by its code
def get_appuntamento_by_code(codice):
    return Appuntamento.query.filter_by(codice=codice).first()



# Add a new appuntamento to the database
def add_appuntamento(new_code, new_data, new_ora, new_id_centroVacc):
    db.session.add(Appuntamento(new_code, new_data, new_ora, new_id_centroVacc))
    db.session.commit()


