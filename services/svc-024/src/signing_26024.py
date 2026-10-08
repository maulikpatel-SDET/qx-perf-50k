"""Signing module 26024: RSA."""
from cryptography.hazmat.primitives.asymmetric import rsa


def make_keys_26024():
    key_0 = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return True
