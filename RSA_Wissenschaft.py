from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def wissenschaft(data):
    with open("/home/proj/rsa/test.pem",'rb') as kf:
        pk = serialization.load_pem_private_key(
            kf.read(),
            password='rockyou',
            backend=default_backend()
        )
        dcrp = pk.decrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA1()),
                algorithm=hashes.SHA1(),
                label=None
            )
        )
    return dcrp
            
