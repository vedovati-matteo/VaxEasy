import jsonpickle
from app import db

# Generate fake database
def _placeholderMalattia_gen():
    nome1 = ("Covid19", "MeningococcoB", "Pertosse")
    descr1 = ("Alta contagiosità" , "Media contagiosità" , "Bassa contagiosità")

    for nome, descr in zip(nome1, descr1):
        db.session.add(Malattia(nome,descr))
        db.session.commit()



# Class representing malattia
class Malattia(db.Model):
    __tablename__ = "malattia"
    nome = db.Column(db.Text(), unique=True, primary_key=True)
    descr = db.Column(db.Text(), nullable=False)

    def __init__(self, nome, descr):
        self.nome = nome
        self.descr = descr

    def __repr__(self):
        return "Malattia-{}: {}".format(self.nome, self.descr)

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
def add_malattia(new_nome, new_descr):
    db.session.add(Malattia(new_nome, new_descr))
    db.session.commit()


