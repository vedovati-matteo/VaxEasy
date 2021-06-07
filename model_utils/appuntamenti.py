import jsonpickle
from app import db


# Class representing users
class Appuntamento(db.Model):
    codice = db.Column(db.String(), unique=True, primary_key=True)
    data = db.Column(db.Date(), nullable=False)
    id_centroVacc = db.Column(db.Text(), nullable=False)

    def __init__(self, codice, data, id_centroVacc):
        self.codice = codice
        self.data = data
        self.id_centroVacc = id_centroVacc

    def __repr__(self):
        return "Appuntamento-{}: {} - {}".format(self.codice, self.data, self.id_centroVacc)

    def __setstate__(self, state):
        self.__dict__.update(state)

def get_appuntamento_from_json(json):    # lasciare o togliere?
    return jsonpickle.decode(json)


# Recover all appuntamento in the database
def get_appuntamento():
    return {appuntamenti.codice:appuntamenti for appuntamenti in Appuntamento.query.all()}


# Recover a appuntamento by its code
def get_appuntamento_by_code(codice):
    return Appuntamento.query.filter_by(codice=codice).first()



# Add a new appuntamento to the database
def add_user(new_code, new_data, new_id_centroVacc):
    db.session.add(Appuntamento(new_code, new_data, new_id_centroVacc))
    db.session.commit()


