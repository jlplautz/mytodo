"""Token based auth"""

from datetime import datetime, timedelta
from functools import partial
from typing import Callable, Optional, Union

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel

from todo.config import settings
from todo.models import User, get_user
from todo.security import verify_password

SECRET_KEY = settings.security.SECRET_KEY
ALGORITHM = settings.security.ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


# Models
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class RefreshToken(BaseModel):
    refresh_token: str


class TokenData(BaseModel):
    username: Optional[str] = None


# functions
def create_access_token(
    data: dict, expires_delta: timedelta = None, scope: str = 'access_token'
) -> str:

    """Creates a JWT Token from user data"""
    to_encode = data.copy()
    # Caso seja definido um timedelta diferente
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp': expire, 'scope': scope})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


# neste caso será gerado um refresh_token, recebe todos os paremetros
# access_token, mas vai mudar o escopo para refresh
# funcionalidade da functools
create_refresh_token = partial(create_access_token, scope='refresh_token')


def authenticate_user(
    get_user: Callable, username: str, password: str
) -> Union[User, bool]:
    """Authenticate the user"""
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def get_current_user(
    token: str = Depends(oauth2_scheme), request: Request = None, fresh=False
) -> User:
    """Get current user autehnticated"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials.',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    if request:
        if authorization := request.headers.get('authorization'):
            try:
                token = authorization.split(' ')[1]
            except IndexError:
                raise credentials_exception

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')

        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = get_user(user_name=token_data.username)

    if user is None:
        raise credentials_exception
    if fresh and (not payload['fresh']):
        raise credentials_exception

    return user


# FastAPI dependencies
async def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """Wraps the sync get_active_user for sync calls"""
    return current_user


AuthenticatedUser = Depends(get_current_active_user)


def validate_token(token: str) -> User:
    """Validate user Token"""
    user = get_current_user(token=token)
    return user
