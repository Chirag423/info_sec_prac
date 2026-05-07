# ============================================================
#  Practical 7 – Row Transposition Cipher (Columnar)
# ============================================================
import math


def row_transposition_encrypt(plaintext: str, key: str) -> str:
    key = key.upper()
    n_cols = len(key)
    # Pad plaintext with 'X'
    pad_len = math.ceil(len(plaintext) / n_cols) * n_cols
    padded = plaintext.upper().ljust(pad_len, 'X')

    n_rows = pad_len // n_cols
    # Fill grid row by row
    grid = [list(padded[i * n_cols:(i + 1) * n_cols]) for i in range(n_rows)]

    # Column order based on alphabetical order of key characters
    order = sorted(range(n_cols), key=lambda i: key[i])

    print("\n  Grid (row-filled):")
    header = "  Key : " + " ".join(key)
    print(header)
    print("  " + "-" * (n_cols * 2 + 6))
    for row in grid:
        print("        " + " ".join(row))

    ciphertext = ''
    for col in order:
        for row in grid:
            ciphertext += row[col]
    return ciphertext


def row_transposition_decrypt(ciphertext: str, key: str) -> str:
    key = key.upper()
    n_cols = len(key)
    n_rows = len(ciphertext) // n_cols

    order = sorted(range(n_cols), key=lambda i: key[i])

    # Determine column lengths (all equal here)
    grid = [[''] * n_cols for _ in range(n_rows)]

    idx = 0
    for col in order:
        for row in range(n_rows):
            grid[row][col] = ciphertext[idx]
            idx += 1

    return ''.join(''.join(row) for row in grid)


def main():
    print("=" * 55)
    print("    Practical 7 – Row Transposition Cipher")
    print("=" * 55)

    plaintext = input("\nEnter plaintext : ")
    key = input("Enter key word  : ")

    encrypted = row_transposition_encrypt(plaintext, key)
    decrypted = row_transposition_decrypt(encrypted, key)

    print(f"\nOriginal  : {plaintext}")
    print(f"Key       : {key.upper()}")
    print(f"Encrypted : {encrypted}")
    print(f"Decrypted : {decrypted}")


if __name__ == "__main__":
    main()
