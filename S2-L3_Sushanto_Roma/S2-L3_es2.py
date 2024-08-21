import re
from collections import Counter

testo = "Ciao, ciao! Come stai? Stai bene?"

testopiccolo = testo.lower()
print(f"Testo in minuscolo: {testopiccolo}")

testosenzapunteggiatura = re.sub(r'[.,!\'?]', '', testopiccolo)
print(f"Testo senza punteggiatura: {testosenzapunteggiatura}")

parole = testosenzapunteggiatura.split()
print(f"Parole: {parole}")

conta = Counter(parole)
print(f"Conteggio delle parole: {conta}")

dizionario = dict(conta)
print(f"Dizionario delle parole: {dizionario}")