#
#   From pyca/cryptography.  pip install cryptography
#   https://cryptography.io/en/latest/
#   This is a crypto library for rsa
#   https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
#
#
#
import base64
import cryptography
import binascii
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

dir_path = os.path.dirname(os.path.realpath(__file__))

#   Load the Private Key from file
ifname_private = 'private.pem'
with open(dir_path + '/' + ifname_private, 'r') as key_file_private :
    private_key = serialization.load_pem_private_key(
        key_file_private.read().encode('utf-8'),
        password=None,
        backend=default_backend()
    )


plaintext = 'this is the main message i want to sign'
plaintext_as_bytes= plaintext.encode('utf-8')

signature = private_key.sign(
    plaintext_as_bytes,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
    salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

b64 = base64.b64encode(signature)
print(b64.decode('utf-8'))

# now verify

public_key = private_key.public_key()
public_key.verify(
    signature,
    plaintext_as_bytes,
    padding.PSS( mgf=padding.MGF1(hashes.SHA256()),
    salt_length=padding.PSS.MAX_LENGTH),hashes.SHA256()
    )
