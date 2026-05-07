# ============================================================
#  Practical 8 – Product Cipher (Substitution + Transposition)
# ============================================================
#  A product cipher applies multiple ciphers in sequence.
#  Here we combine:
#    Round 1 → Vigenère (substitution)
#    Round 2 → Columnar Row Transposition
#  Decryption reverses the order.
# ============================================================
import math


# ── Vigenère ────────────────────────────────────────────────
def vigenere_encrypt(text: str, key: str) -> str:
    key = key.upper()
    result, ki = [], 0
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[ki % len(key)]) - ord('A')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            ki += 1
        else:
            result.append(ch)
    return ''.join(result)


def vigenere_decrypt(text: str, key: str) -> str:
    key = key.upper()
    result, ki = [], 0
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[ki % len(key)]) - ord('A')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
            ki += 1
        else:
            result.append(ch)
    return ''.join(result)


# ── Columnar Transposition ───────────────────────────────────
def col_encrypt(text: str, key: str) -> str:
    n_cols = len(key)
    pad_len = math.ceil(len(text) / n_cols) * n_cols
    padded = text.upper().ljust(pad_len, 'X')
    n_rows = pad_len // n_cols
    grid = [list(padded[i * n_cols:(i + 1) * n_cols]) for i in range(n_rows)]
    order = sorted(range(n_cols), key=lambda i: key.upper()[i])
    return ''.join(grid[r][c] for c in order for r in range(n_rows))


def col_decrypt(text: str, key: str) -> str:
    n_cols = len(key)
    n_rows = len(text) // n_cols
    order = sorted(range(n_cols), key=lambda i: key.upper()[i])
    grid = [[''] * n_cols for _ in range(n_rows)]
    idx = 0
    for c in order:
        for r in range(n_rows):
            grid[r][c] = text[idx]
            idx += 1
    return ''.join(''.join(row) for row in grid)


# ── Product Cipher ───────────────────────────────────────────
def product_encrypt(plaintext: str, sub_key: str, trans_key: str) -> str:
    step1 = vigenere_encrypt(plaintext, sub_key)
    step2 = col_encrypt(step1, trans_key)
    return step2


def product_decrypt(ciphertext: str, sub_key: str, trans_key: str) -> str:
    step1 = col_decrypt(ciphertext, trans_key)
    step2 = vigenere_decrypt(step1, sub_key)
    return step2


# ── Main ─────────────────────────────────────────────────────
def main():
    print("=" * 60)
    print("  Practical 8 – Product Cipher")
    print("  (Vigenère Substitution → Columnar Transposition)")
    print("=" * 60)

    plaintext = input("\nEnter plaintext          : ")
    sub_key   = input("Enter substitution key   : ")
    trans_key = input("Enter transposition key  : ")

    encrypted = product_encrypt(plaintext, sub_key, trans_key)
    decrypted = product_decrypt(encrypted, sub_key, trans_key)

    print(f"\nPlaintext        : {plaintext}")
    print(f"After Vigenère   : {vigenere_encrypt(plaintext, sub_key)}")
    print(f"Final Ciphertext : {encrypted}")
    print(f"\nDecrypted        : {decrypted}")


if __name__ == "__main__":
    main()
