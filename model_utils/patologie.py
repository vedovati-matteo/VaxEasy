import jsonpickle
from app import db

# Generate fake database
def _placeholderPatologia_gen():
    nome1 = ("Diabete","Ipertensione")
    descrizione1 = ("Possibile rischio per alcuni vaccini covid", "Possibile rischio per vaccini pertosse")

    for nome, descrizione in zip(nome1, descrizione1):
        db.session.add(Patologia(nome, descrizione))
        db.session.commit()



# Class representing patologia
class Patologia(db.Model):
    nome = db.Column(db.Text(), unique=True, primary_key=True)
    descrizione = db.Column(db.Text(), nullable=False)

    def __init__(self, nome, descrizione,):
        self.nome = nome
        self.descrizione = descrizione

    def __repr__(self):
        return "Patologia-{}: {}".format(self.nome, self.descrizione)

    def __setstate__(self, state):
        self.__dict__.update(state)

def get_patologia_from_json(json):    
    return jsonpickle.decode(json)


# Recover all patologia in the database
def get_patologia():
    lista = []
    for patologia in Patologia.query.all():
        lista.append(patologia.nome)
    return  lista



# Recover a patologia by its code
def get_patologia_by_name(nome):
    return Patologia.query.filter_by(nome=nome).first()



# Add a new patologia to the database
def add_patologia(new_nome, new_descrizione):
    db.session.add(Patologia(new_nome, new_descrizione))
    db.session.commit()


