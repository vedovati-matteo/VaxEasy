from app import db
from model_utils.prenotazioni import Prenotazione, _placeholderPrenotazione_gen, setPrenotazione, getPrenotazioni
from model_utils.user import Utente, _placeholderUtente_gen, get_user_by_cf, add_user
from model_utils.appuntamenti import Appuntamento, _placeholderAppuntamento_gen, get_appuntamentoByProvincia, get_appuntamento_by_code
from model_utils.centriVaccinali import CentroVaccinale, _placeholderCentroVaccinale_gen
from model_utils.malattie import Malattia, _placeholderMalattia_gen
from model_utils.patologie import Patologia, _placeholderPatologia_gen, get_patologia
from model_utils.patologieUtente import PatologiaUtente, _placeholderPatologiaUtente_gen
from model_utils.patologieVaccino import PatologiaVaccino, _placeholderPatologiaVaccino_gen

from model_utils.vaccinoMalattie import VaccinoMalattia, _placeholderVaccinoMalattia_gen
from model_utils.vaccini import Vaccino, _placeholderVaccino_gen, getVaccini
from model_utils.enti import Ente, _placeholderEnte_gen

from controller_utils.password_handler import Password, _gen_placeholder_passwords
from controller_utils.password_enti_handler import PasswordE, _gen_placeholder_passwordsEnte

db.drop_all()
db.create_all()
db.session.commit()
_placeholderEnte_gen()
_placeholderUtente_gen()
_placeholderCentroVaccinale_gen()
_placeholderVaccino_gen()
_placeholderAppuntamento_gen()
_placeholderPrenotazione_gen()
_placeholderPatologia_gen()
_placeholderPatologiaUtente_gen()
_placeholderPatologiaVaccino_gen()
_placeholderMalattia_gen()
_placeholderVaccinoMalattia_gen()
_gen_placeholder_passwords()
_gen_placeholder_passwordsEnte()
users = Utente.query.all()
enti = Ente.query.all()
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
passwordsEnti = PasswordE.query.all()
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

print("=======")
print(get_user_by_cf("RSSMRC21A01A794Y"))  # OK
print("=======")
print(get_patologia())   #ok
print("=======")
add_user("RSSLSN21A01A794Y", "Alessandro", "Rossi", "alessandro.rossi@unibg.it", "3270810777", "Bergamo")    # ok
print("======= PRINT DI USER========")
for u in users:
    print(u)
print("=======")
print(get_appuntamentoByProvincia("Bergamo"))   # ok
print("=======")
print(get_appuntamento_by_code("36740"))  # ok
print("=== getVaccini====") 
print(getVaccini("RSSMRC21A01A794Y"))  # ok
print("=======")
print(setPrenotazione("RSSMRC21A01A794Y", "26248698", "36740"))   # ok
print("=======")
print(getPrenotazioni("RSSMRC21A01A794Y"))   # ok 


