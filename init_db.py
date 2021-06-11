from app import db
from model_utils.user import Utente, _placeholderUtente_gen
from model_utils.appuntamenti import Appuntamento, _placeholderAppuntamento_gen
from model_utils.centriVaccinali import CentroVaccinale, _placeholderCentroVaccinale_gen
from model_utils.malattie import Malattia, _placeholderMalattia_gen
from model_utils.patologie import Patologia, _placeholderPatologia_gen
from model_utils.patologieUtente import PatologiaUtente, _placeholderPatologiaUtente_gen
from model_utils.patologieVaccino import PatologiaVaccino, _placeholderPatologiaVaccino_gen
from model_utils.prenotazioni import Prenotazione, _placeholderPrenotazione_gen
from model_utils.vaccinoMalattie import VaccinoMalattia, _placeholderVaccinoMalattia_gen
from model_utils.vaccini import Vaccino, _placeholderVaccino_gen

from controller_utils.password_handler import Password, _gen_placeholder_passwords

db.drop_all()
db.create_all()
db.session.commit()
_placeholderUtente_gen()
_placeholderCentroVaccinale_gen
_placeholderAppuntamento_gen
_placeholderVaccino_gen
_placeholderPrenotazione_gen
_placeholderPatologia_gen
_placeholderPatologiaUtente_gen
_placeholderPatologiaVaccino_gen
_placeholderMalattia_gen
_placeholderVaccinoMalattia_gen

_gen_placeholder_passwords()
users = Utente.query.all()
centriVaccinali = CentroVaccinale.query.all()
appuntamenti = Appuntamento.query.all()
vaccini = Vaccino.query.all()
prenotazioni = Prenotazione.query.all()
patologie = Patologia.query.all()
patologieUtenti = PatologiaUtente.query.all()
patologieVaccini = PatologiaVaccino.query.all()
malattie = Malattia.query.all()
vacciniMalattie = VaccinoMalattia.query.all()

passwords = Password.query.all()
for u in users:
    print(u)
print("=======")
for u in centriVaccinali:
    print(u)
print("=======")
for u in appuntamenti:
    print(u)
print("=======")
for u in vaccini:
    print(u)
print("=======")
for u in prenotazioni:
    print(u)
print("=======")
for u in patologie:
    print(u)
print("=======")
for u in patologieUtenti:
    print(u)
print("=======")
for u in patologieVaccini:
    print(u)
print("=======")
for u in malattie:
    print(u)
print("=======")
for u in vacciniMalattie:
    print(u)
