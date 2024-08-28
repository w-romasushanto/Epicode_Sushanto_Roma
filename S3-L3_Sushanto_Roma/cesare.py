def cesare_cifraio(testo, posizione):
    risultato = ""

    for char in testo:
        if char.isalpha():
           
            cambiamento = ord('A') if char.isupper() else ord('a')
            # spostamento e modulo 26 (lettere alfabeto)
            risultato += chr((ord(char) - cambiamento + posizione) % 26 + cambiamento)
        else:
            risultato += char  # se non è lettera

    return risultato


messaggio = "EPICODE!"
posizione = 3

messaggio_criptato = cesare_cifraio(messaggio, posizione)
print("Messaggio cifrato:", messaggio_criptato)

messaggio_decriptato = cesare_cifraio(messaggio_criptato, -posizione)
print("Messaggio decriptato:", messaggio_decriptato)
