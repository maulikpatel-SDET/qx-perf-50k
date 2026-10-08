"""Signing module 5084: RSA."""
from cryptography.hazmat.primitives.asymmetric import rsa


def make_keys_5084():
    key_0 = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return True
