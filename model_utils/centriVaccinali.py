import jsonpickle
from app import db

# Generate fake database
def _placeholderCentroVaccinale_gen():
    id_centroVacc1 = ("BG160","BS893","MI645")
    indirizzo1 = ("Covid19", "MeningococcoB", "Pertosse")
    provincia1 = ("Bergamo", "Brescia", "Milano")
    id_ente1 = ("REG156","PROV3546","REG987")

    for id_centroVacc, indirizzo, provincia, id_ente in zip(id_centroVacc1, indirizzo1, provincia1, id_ente1):
        db.session.add(CentroVaccinale(id_centroVacc, indirizzo, provincia, id_ente))
        db.session.commit()



# Class representing centroVaccinale
class CentroVaccinale(db.Model):
    __tablename__ = "centroVaccinale"
    id_centroVacc = db.Column(db.String(5), unique=True, primary_key=True)
    indirizzo = db.Column(db.Text(), nullable=False)
    provincia = db.Column(db.Text(), nullable=False)
    id_ente = db.Column(db.String(6), db.ForeignKey("ente.id_ente"),nullable=False)

    def __init__(self, id_centroVacc, indirizzo, provincia, id_ente):
        self.id_centroVacc = id_centroVacc
        self.indirizzo = indirizzo
        self.provincia = provincia
        self.id_ente = id_ente

    def __repr__(self):
        return "{} - {} - {} - {}".format(self.id_centroVacc, self.indirizzo, self.provincia, self.id_ente)

    def to_json(self):
        return jsonpickle.encode(self)

    def __setstate__(self, state):
        self.__dict__.update(state)

def get_centroVaccinale_from_json(json):    
    return jsonpickle.decode(json)


# Recover all centroVaccinale in the database
def get_centroVaccinale():
    return {centriVaccinali.id_centroVacc:centriVaccinali for centriVaccinali in CentroVaccinale.query.all()}


# Recover a centroVaccinale by its code
def get_centroVaccinale_by_code(id_centroVacc):
    return CentroVaccinale.query.filter_by(id_centroVacc=id_centroVacc)



# Add a new centroVaccinale to the database
def add_centroVaccinale(new_id_centroVacc, new_indirizzo, new_provincia, new_id_ente):
    db.session.add(CentroVaccinale(new_id_centroVacc, new_indirizzo, new_provincia, new_id_ente))
    db.session.commit()


