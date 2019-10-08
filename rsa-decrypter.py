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

#   open the encrypted message as a binary file
ifname = 'encrypted-message.enc'
cipherbytes = bytearray()
with open(dir_path + '/' + ifname,'rb') as infile:
    cipherbytes = infile.read()

#   Decrypt the message
plaintext = private_key.decrypt(cipherbytes,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None )).decode('utf-8')

print( plaintext )
