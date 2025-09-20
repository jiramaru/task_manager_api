from passlib.context import CryptContext


# password hashing context

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# hash a plain password
def hash_password(password) -> str:
    return pwd_context.hash(password)


# verify a plain password against a hashed password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
