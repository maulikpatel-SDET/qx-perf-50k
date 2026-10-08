"""Signing module 48112: RSA."""
from cryptography.hazmat.primitives.asymmetric import rsa


def make_keys_48112():
    key_0 = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return True
