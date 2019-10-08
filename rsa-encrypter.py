import cryptography
import binascii
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

#
#   From pyca/cryptography.  pip install cryptography
#   https://cryptography.io/en/latest/
#   This is a crypto library for rsa
#   https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
#
#
#

dir_path = os.path.dirname(os.path.realpath(__file__))

#   Load the public key from file
ifname_public = 'public.pem'
with open(dir_path + '/' + ifname_public, 'r') as key_file_public :
    public_key = serialization.load_pem_public_key(
        key_file_public.read().encode('utf-8'),
        backend=default_backend()
    )


#   Set the message
message_text = 'this is my first attempt at a test'
message_bytes = message_text.encode('utf-8')


#   Encrypt the message using the Public Key
ciphertext = public_key.encrypt(
     message_bytes,
     padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
         algorithm=hashes.SHA256(),
         label=None))

print('----')
print(ciphertext, type(ciphertext))


# Save the cipher text as binary data to file
cipherbytes = bytearray(ciphertext)
ofname = 'encrypted-message.enc'
with open(dir_path + '/' + ofname,'wb') as outfile:
    outfile.write(cipherbytes)

# or perhaps as Base64
cipherbytes_as_b64 = base64.b64encode(cipherbytes)

print(cipherbytes_as_b64)
#
# original = base64.b64decode(cipherbytes_as_b64)
# print(original)
