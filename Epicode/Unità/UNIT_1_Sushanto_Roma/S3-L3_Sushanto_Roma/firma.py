from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import base64

# Carica la chiave privata dal file
with open('private_key.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None  # Inserisci qui la password se la chiave privata è protetta
    )

# Carica la chiave pubblica dal file
with open('public_key.pem', 'rb') as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

# Messaggio da firmare
message = 'Ciao, Epicode spacca!'

# Firma con la chiave privata
signed = private_key.sign(
    message.encode(),
    padding.PKCS1v15(),
    hashes.SHA256()
)

try:
    # Codifica la firma in base64
    encrypted_b64 = base64.b64encode(signed).decode('utf-8')
    
    # Verifica della firma con la chiave pubblica
    public_key.verify(
        signed,
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    
    # Se la verifica ha successo
    print("Base64 della firma:", encrypted_b64)
    print("Messaggio originale da confrontare:", message)
    print("La firma è valida.")
except Exception as e:
    # Se la verifica fallisce
    print("La firma non è valida.", str(e))
