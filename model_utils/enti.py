import jsonpickle
from app import bcrypt
from app import db


# Generate fake database
def _placeholderEnte_gen():
    id_ente1 = ("REG156","PROV3546","REG987")
    descrizione1 = ("regione Lombardia", "Provincia di Cuneo", "regione Lazio")
    passwd1 = ("adsfasd", "fadsfasf", "hdffdh", "dfhshd","wt43dff")

    for id_ente, descrizione, passwd in zip(id_ente1, descrizione1, passwd1):
        gen = bcrypt.generate_password_hash(passwd)
        db.session.add(Ente(id_ente, descrizione, gen.decode("ascii")))
        db.session.commit()


# Class representing vax
class Ente(db.Model):
    id_ente = db.Column(db.String(6), unique=True, primary_key=True)
    descrizione = db.Column(db.Text(), nullable=False)    
    password = db.Column(db.Text(), nullable=False)  

    def __init__(self, id_ente, descrizione, password):
        self.id_ente = id_ente
        self.descrizione = descrizione
        self.password = password

    def __repr__(self):
        return "{} - {} - {}".format(self.id_ente, self.descrizione, self.password)

    def __setstate__(self, state):
        self.__dict__.update(state)

    # non vogliamo che nel cookie compaiano le seguente cose
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['password']
        del state["_sa_instance_state"]  # fa parte di db.model
        return state


def get_ente_from_json(json):    
    return jsonpickle.decode(json)


# Recover all ente in the database
def get_ente():
    return {enti.codice:enti for enti in Ente.query.all()}


# Recover a ente by its code
def get_ente_by_code(id_ente):
    return Ente.query.filter_by(id_ente=id_ente)



# Add a new ente to the database
def add_ente(new_id_ente, new_descrizione, new_psw):
    gen = bcrypt.generate_password_hash(new_psw)
    db.session.add(Ente(new_id_ente, new_descrizione, gen.decode("ascii")))
    db.session.commit()


