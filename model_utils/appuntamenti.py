from datetime import date, time
import datetime
from model_utils.centriVaccinali import CentroVaccinale
import jsonpickle
from app import db

# Generate fake database
def _placeholderAppuntamento_gen():
    codice1 = ("36740","20506","13005","13287")
    data1 = (date.fromisoformat("2021-05-18"), date.fromisoformat("2021-06-08"), date.fromisoformat("2021-06-19"), date.fromisoformat("2021-07-19"))
    ora1 = (time.fromisoformat("09:30"), time.fromisoformat("10:45"), time.fromisoformat("11:20"), time.fromisoformat("12:30"))
    id_centroVacc1 = ("BG160","BS893","MI645","BG160")

    for codice, data, ora, id_centroVacc in zip(codice1, data1, ora1, id_centroVacc1):
        db.session.add(Appuntamento(codice, data, ora, id_centroVacc))
        db.session.commit()



# Class representing appuntamento
class Appuntamento(db.Model):
    codice = db.Column(db.String(5), unique=True, primary_key=True)
    data = db.Column(db.Date(), nullable=False)
    ora = db.Column(db.Time(), nullable=False)
    id_centroVacc = db.Column(db.String(5), db.ForeignKey("centroVaccinale.id_centroVacc"), nullable=False)

    def __init__(self, codice, data, ora, id_centroVacc):
        self.codice = codice
        self.data = data
        self.ora = ora
        self.id_centroVacc = id_centroVacc

    def __repr__(self):
        return "{} - {} - {} - {}".format(self.codice, self.data, self.ora, self.id_centroVacc)

    def __setstate__(self, state):
        self.__dict__.update(state)
    
    def to_json(self):
        return jsonpickle.encode(self)

def get_appuntamento_from_json(json): 
    return jsonpickle.decode(json)


# Recover all appuntamento in the database
def get_appuntamentoByProvincia(provincia):
    return {appuntamenti.codice:appuntamenti for appuntamenti in Appuntamento.query.join(CentroVaccinale).filter_by(provincia=provincia).all()}


# Recover a appuntamento by its code
def get_appuntamento_by_code(code):
    return {appuntamenti.codice:appuntamenti for appuntamenti in Appuntamento.query.filter_by(codice=code).all()}



# Add a new appuntamento to the database
def add_appuntamento(new_code, new_data, new_ora, new_id_centroVacc):
    db.session.add(Appuntamento(new_code, date.fromisoformat(new_data), time.fromisoformat(new_ora), new_id_centroVacc))
    db.session.commit()


