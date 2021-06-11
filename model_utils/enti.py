import jsonpickle
from app import db


# Generate fake database
def _placeholderEnte_gen():
    id_ente1 = ("REG156","PROV3546","REG987")
    descrizione1 = ("regione Lombardia", "Provincia di Cuneo", "regione Lazio")

    for id_ente, descrizione in zip(id_ente1, descrizione1):
        db.session.add(Ente(id_ente, descrizione))
        db.session.commit()


# Class representing vax
class Ente(db.Model):
    id_ente = db.Column(db.String(6), unique=True, primary_key=True)
    descrizione = db.Column(db.Text(), nullable=False)

    def __init__(self, id_ente, descrizione):
        self.id_ente = id_ente
        self.descrizione = descrizione

    def __repr__(self):
        return "Ente-{}: {} - {}".format(self.id_ente, self.descrizione)

    def __setstate__(self, state):
        self.__dict__.update(state)


def get_ente_from_json(json):    
    return jsonpickle.decode(json)


# Recover all ente in the database
def get_ente():
    return {enti.codice:enti for enti in Ente.query.all()}


# Recover a ente by its code
def get_ente_by_code(id_ente):
    return Ente.query.filter_by(id_ente=id_ente)



# Add a new ente to the database
def add_ente(new_id_ente, new_descrizione):
    db.session.add(Ente(new_id_ente, new_descrizione))
    db.session.commit()


