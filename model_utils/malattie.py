import jsonpickle
from app import db

# Generate fake database
def _placeholderMalattia_gen():
    nome1 = ("Covid19", "MeningococcoB", "Pertosse")

    for nome, descrizione in zip(nome1):
        db.session.add(Malattia(nome))
        db.session.commit()



# Class representing malattia
class Malattia(db.Model):
    nome = db.Column(db.Text(), unique=True, primary_key=True)

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return "Malattia-{}: {} - {}".format(self.nome)

    def __setstate__(self, state):
        self.__dict__.update(state)

def get_malattia_from_json(json):    
    return jsonpickle.decode(json)


# Recover all malattia in the database
def get_malattia():
    return {malattie.nome:malattie for malattie in Malattia.query.all()}


# Recover a malattia by its code
def get_malattia_by_name(nome):
    return Malattia.query.filter_by(nome=nome)



# Add a new malattia to the database
def add_malattia(new_nome):
    db.session.add(Malattia(new_nome))
    db.session.commit()


