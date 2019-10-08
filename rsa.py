#
#   From pyca/cryptography.  pip install cryptography
#   https://cryptography.io/en/latest/
#   This is a crypto library for rsa
#   https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
#
#
#

import cryptography
import binascii
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
#
#   From https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/?highlight=rsa
#
private_key = rsa.generate_private_key(public_exponent = 65537,
    key_size=2048, backend=default_backend()
    )

message = b'Here is my message'
signature = private_key.sign(message,
padding.PSS( mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
hashes.SHA256() )


public_key = private_key.public_key()

public_key.verify(signature, message,padding.PSS( mgf=padding.MGF1(hashes.SHA256()),
 salt_length=padding.PSS.MAX_LENGTH),hashes.SHA256() )


#---
message = b"encrypted data"
ciphertext = public_key.encrypt(
     message,
     padding.OAEP(
         mgf=padding.MGF1(algorithm=hashes.SHA256()),
         algorithm=hashes.SHA256(),
         label=None
     )
 )

plaintext = private_key.decrypt(
     ciphertext,
     padding.OAEP(
         mgf=padding.MGF1(algorithm=hashes.SHA256()),
         algorithm=hashes.SHA256(),
         label=None
     )
 )
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
 )
print(pem)
print(private_key)
print(message)
print(ciphertext)
print(plaintext)
