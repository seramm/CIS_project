import hashlib
from os import urandom
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305


def encrypt_msg(msg: str, key: str) -> str:

    secure_key = hashlib.sha256(key.encode("utf-8")).digest()
    nonce = urandom(12)
    msg_bytes = msg.encode("utf-8")
    encrypt_msg = ChaCha20Poly1305(secure_key).encrypt(nonce, msg_bytes, None)

    result = nonce + encrypt_msg

    return result.hex()


def decrypt_msg(msg: str, key: str) -> str:
    try:
        secure_key = hashlib.sha256(key.encode("utf-8")).digest()
        result_bytes = bytes.fromhex(msg)
        nonce = result_bytes[:12]
        encrypted_msg = result_bytes[12:]

        msg_bytes = ChaCha20Poly1305(secure_key).decrypt(nonce, encrypted_msg, None)

        return msg_bytes.decode("utf-8")
    except Exception:
        raise ValueError("Error at decrypting: No key provided")
