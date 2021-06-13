from app import bcrypt
from app import db


# Generate fake database
def _gen_placeholder_passwordsEnte():
    for id_ente, passwd in zip(range(0, 5), ["p123", "regABC", "alphaB", "Unibg"]):
        gen = bcrypt.generate_password_hash(passwd)
        db.session.add(PasswordE(id_ente, gen.decode("ascii")))
        db.session.commit()


# Check that the candidate password for the given userid is correct
def check_passwordEnte(id_ente, candidate):
    return bcrypt.check_password_hash(PasswordE.query.filter_by(id=id_ente).first().hash, candidate)


class PasswordE(db.Model):
    id = db.Column(db.Integer, db.ForeignKey("ente.id_ente"), primary_key=True)
    hash = db.Column(db.Text(), nullable=False)

    def __init__(self, id_ente, hash):
        self.id = id_ente
        self.hash = hash

    def __repr__(self):
        return "{}".format(self.hash)