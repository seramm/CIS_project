import hashlib


def gen_sha256(msg: str) -> str:
    if not msg:
        raise ValueError("Missing message to hash")
    return hashlib.sha256(msg.encode()).hexdigest()
