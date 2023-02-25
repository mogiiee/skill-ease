import time
import jwt
from decouple import config
from app.responses import response

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return response(True, token, None)


def signJWT(email: str):
    payload = {"email": email, "expiry": time.time() + 1200}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, key=JWT_SECRET, algorithm=JWT_ALGORITHM)
        return (
            decode_token
            if decode_token["expires"] >= time.time()
            else print("invalid token, expired")
        )
    except Exception as e:
        return response(False, e, None)
