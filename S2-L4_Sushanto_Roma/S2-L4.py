import math

a = int(input("Premi 1 per il perimetro del quadrato\n2 per il perimetro del cerchio\n3 per il perimetro del rettangolo\n"))

if a == 1:
    lato = float(input("Inserisci la lunghezza del lato: "))
    perimetro = lato * 4
    print(f"Il perimetro del quadrato è: {perimetro}")
    
elif a == 2:
    raggio = float(input("Inserisci il raggio del cerchio: "))
    perimetro = 2 * math.pi * raggio
    print(f"Il perimetro del cerchio è: {perimetro}")
    
elif a == 3:
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    perimetro = (base * 2) + (altezza * 2)
    print(f"Il perimetro del rettangolo è: {perimetro}")
else:
    print("⚠️ Scelta non valida. Per favore, inserisci 1, 2 o 3.")

    
