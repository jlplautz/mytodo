"""Security utilities"""

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a hash against a plain_password."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Generae a hash from plain text

    Args:
        password(str): Plain Text Password

    Returns:
       str: Hased Passwod
    """
    return pwd_context.hash(password)


class HashedPassword(str):
    """Takes a plain text password and hashes it.
    We can use it a field on our SQLModel
    class User(SQLModel, table=True):
        user_name= str
        password = HashedPassword
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        """Accepts a plain password and returns a hashed password."""
        if not isinstance(v, str):
            raise TypeError('String required')

        hashed_password = get_password_hash(v)
        return cls(hashed_password)
