def load_key(key_file: str) -> list[str]:
    """Load substitution key rows from a file. Each row maps A-Z to encoded characters."""
    with open(key_file) as f:
        rows = [line.strip() for line in f if line.strip()]
    if not rows:
        raise ValueError("Key file is empty.")
    if not all(len(row) == 26 for row in rows):
        raise ValueError("Each key row must contain exactly 26 characters.")
    return rows


def encode(message: str, key_rows: list[str]) -> str:
    """Encode a message using the polyalphabetic substitution key."""
    period = len(key_rows)
    result = []
    pos = 0
    for ch in message.upper():
        if ch.isalpha():
            row = key_rows[pos % period]
            result.append(row[ord(ch) - ord('A')])
            pos += 1
        else:
            result.append(ch)
    return ''.join(result)


def decode(message: str, key_rows: list[str]) -> str:
    """Decode a message by inverting the polyalphabetic substitution key."""
    period = len(key_rows)

    # Build inverse lookup table for each key row
    inverse_rows = []
    for row in key_rows:
        inverse = {ch: chr(ord('A') + i) for i, ch in enumerate(row)}
        inverse_rows.append(inverse)

    result = []
    pos = 0
    for ch in message.upper():
        if ch.isalpha():
            inv = inverse_rows[pos % period]
            if ch not in inv:
                raise ValueError(f"Character '{ch}' not found in key row {pos % period + 1}.")
            result.append(inv[ch])
            pos += 1
        else:
            result.append(ch)
    return ''.join(result)
