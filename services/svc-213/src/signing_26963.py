"""Signing module 26963: RSA."""
from cryptography.hazmat.primitives.asymmetric import rsa


def make_keys_26963():
    key_0 = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return True
