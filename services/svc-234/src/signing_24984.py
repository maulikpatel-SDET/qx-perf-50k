"""Signing module 24984: RSA."""
from cryptography.hazmat.primitives.asymmetric import rsa


def make_keys_24984():
    key_0 = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return True
