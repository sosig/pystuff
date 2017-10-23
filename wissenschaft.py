import os
from cryptography.hazmat.primitives.ciphers.aead import chacha20poly1305

key = ChaCha20Poly1305.generate_key()
d = 'WasIstHierLos"
hca = ChaCha20Poly1305(key)
nonce = os.urandom(12)

def wissenschaft(data,flg):
    if flg == 0:
        ach = hca.encrypt(nonce, data, d)
    elif flg == 1:
        ach = hca.decrypt(nonce, data, d)
    else:
        return
        
    return ach
    
   
