from app import bcrypt
from app import db


# Generate fake database
def _gen_placeholder_passwords():
    for userid, passwd in zip(range(0, 4), ["secret", "my_pass", "tmp_pass", "bdweb2021"]):
        gen = bcrypt.generate_password_hash(passwd)
        db.session.add(Password(userid, gen.decode("ascii")))
        db.session.commit()


# Check that the candidate password for the given userid is correct
def check_password(userid, candidate):
    return bcrypt.check_password_hash(Password.query.filter_by(id=userid).first().hash, candidate)


class Password(db.Model):
    id = db.Column(db.Integer, db.ForeignKey("user.cf"), primary_key=True)
    hash = db.Column(db.Text(), nullable=False)

    def __init__(self, userid, hash):
        self.id = userid
        self.hash = hash

    def __repr__(self):
        return "{}".format(self.hash)