import secrets
from core.hashing import gen_sha256


def calc_signature(msg: str) -> str:
    if not msg:
        raise ValueError("Error: missing message")

    signature = gen_sha256(msg)

    return signature


def verify_signature(msg: str, signature: str) -> bool:
    expected_signature = gen_sha256(msg)

    return secrets.compare_digest(expected_signature, signature)
