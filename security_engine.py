import os

from cryptography.fernet import Fernet

KEY_FILE = "secret.key"


def load_or_generate_key():
    """
    Checks if a key exists. If not, generates one.
    Returns the Key bytes.
    """
    if not os.path.exists(KEY_FILE):
        # Generate and Save new key
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)
    else:
        # Load existing key
        with open(KEY_FILE, "rb") as file:
            key = file.read()

    return key


def get_cipher():
    """
    Returns a ready-to-use Fernet engine.
    """
    key = load_or_generate_key()
    return Fernet(key)


def encrypt_content(cipher, text):
    """
    Takes a string, encrypts it, returns encrypted string.
    """
    return cipher.encrypt(text.encode()).decode()


def decrypt_content(cipher, encrypted_text):
    """
    Takes encrypted string, decrypts it, returns normal string.
    """
    return cipher.decrypt(encrypted_text.encode()).decode()
