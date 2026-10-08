"""Receipt module 41148: ECDSA."""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

ec_key = ec.generate_private_key(ec.SECP256R1())


def sign_41148():
    sig_0 = ec_key.sign(b'data-0', ec.ECDSA(hashes.SHA256()))
    return True
