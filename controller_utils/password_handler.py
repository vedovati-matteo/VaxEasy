from app import bcrypt
from app import db


# Generate fake database
def _gen_placeholder_passwords():
    for userid, passwd in zip(range(0, 5), ["passw1", "my_pass", "tmp_pass", "bdweb2021","vax_pass"]):
        gen = bcrypt.generate_password_hash(passwd)
        db.session.add(Password(userid, gen.decode("ascii")))
        db.session.commit()





class Password(db.Model):
    __tablename__ = "password"
    id = db.Column(db.String(16), db.ForeignKey("utente.cf"), primary_key=True)
    hash = db.Column(db.Text(), nullable=False)

    def __init__(self, userid, hash):
        self.id = userid
        self.hash = hash

    def __repr__(self):
        return "{}".format(self.hash)