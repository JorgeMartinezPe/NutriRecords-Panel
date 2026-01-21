import bcrypt
import os
from dotenv import load_dotenv
load_dotenv()
PEPPER = os.getenv("APP_PEPPER")

def proteccion(password: str) -> bytes:
    password_pepper = (password + PEPPER).encode("utf-8")
    sal = bcrypt.gensalt(14)
    return bcrypt.hashpw(password_pepper, sal)


def verificar_password(password: str, hashed_password) -> bool:
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode("utf-8")

    password_pepper = (password + PEPPER).encode("utf-8")
    return bcrypt.checkpw(password_pepper, hashed_password)
