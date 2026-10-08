"""Signing module 1505: RSA."""
from cryptography.hazmat.primitives.asymmetric import rsa


def make_keys_1505():
    key_0 = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return True
