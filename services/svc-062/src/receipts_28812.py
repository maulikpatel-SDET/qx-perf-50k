"""Receipt module 28812: ECDSA."""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

ec_key = ec.generate_private_key(ec.SECP256R1())


def sign_28812():
    sig_0 = ec_key.sign(b'data-0', ec.ECDSA(hashes.SHA256()))
    return True
