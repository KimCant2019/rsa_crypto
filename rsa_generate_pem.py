#
#   From pyca/cryptography.  pip install cryptography
#   https://cryptography.io/en/latest/
#   This is a crypto library for rsa
#   https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
#
#
#
import cryptography
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization



def generate_my_keys( ofname_private, ofname_public  ):
    """
    This generates the public/private key pair
    and then saves it to files
    using the parameters
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))


    #
    #   Private Key
    #
    private_key = rsa.generate_private_key(public_exponent = 65537,
        key_size=2048, backend=default_backend()
        )
    pem_private_key_as_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption())

    #
    #   Now do the Public Key stuff
    #
    public_key = private_key.public_key()
    pem_public_key_as_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo)

    #
    #   Save the public and private keys to file
    #   public.pem and private.pem
    #
    # ofname_private = 'private.pem'
    # ofname_public = 'public.pem'

    #   "\" char is line separator character
    with open(dir_path + '/' + ofname_private, 'w') as private, \
        open(dir_path +'/' + ofname_public, 'w') as public:
        for pemline in pem_private_key_as_bytes.splitlines():
            private.write(pemline.decode('utf-8'))
            private.write('\n')
        for pemline in pem_public_key_as_bytes.splitlines():
            public.write(pemline.decode('utf-8'))
            public.write('\n')
