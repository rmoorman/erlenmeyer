from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt", "pbkdf2_sha512"],
    default="pbkdf2_sha512",
)
