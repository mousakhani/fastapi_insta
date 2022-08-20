import hashlib
from config.settings import settings


def verify_password(plain_password, hashed_password):
    encoded_pass= str(settings.SECRET_KEY + plain_password).encode()
    return hashlib.sha256(encoded_pass).hexdigest() == hashed_password

def get_hashed_password(password: str):
    encoded_pass= str(settings.SECRET_KEY + password).encode()
    return hashlib.sha256(encoded_pass).hexdigest()
