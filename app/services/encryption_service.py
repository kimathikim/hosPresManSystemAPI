import random
import secrets


def generate_unique_code():
    return random.randint(10000000, 99999999)


def prescription_code():
    return secrets.token_hex(4)
