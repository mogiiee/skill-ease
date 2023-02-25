from fastapi import Request, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from .jwt_handler import decodeJWT


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invavlid user pls log in again"
                )
            else:
                return credentials.credentials
        else:

            raise HTTPException(
                status_code=403, detail="Invavlid user pls log in again"
            )

    def verify_jwt(self, jwtoken: str):
        IsTokenValid: bool = False
        payload = decodeJWT(jwtoken)
        if payload:
            IsTokenValid: True
        return IsTokenValid
