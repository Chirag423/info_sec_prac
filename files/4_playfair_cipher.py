# ============================================================
#  Practical 4 – Playfair Cipher
# ============================================================

def build_matrix(key: str):
    key = key.upper().replace('J', 'I')
    seen = []
    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.append(ch)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            seen.append(ch)
    matrix = [seen[i*5:(i+1)*5] for i in range(5)]
    return matrix


def find_position(matrix, ch):
    for r, row in enumerate(matrix):
        if ch in row:
            return r, row.index(ch)
    return None


def prepare_text(plaintext: str) -> str:
    text = plaintext.upper().replace('J', 'I')
    text = ''.join(c for c in text if c.isalpha())
    result = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 == len(text):
            result.append(a + 'X')
            i += 1
        elif text[i] == text[i + 1]:
            result.append(a + 'X')
            i += 1
        else:
            result.append(a + text[i + 1])
            i += 2
    return result


def playfair_encrypt(plaintext: str, key: str) -> str:
    matrix = build_matrix(key)
    pairs = prepare_text(plaintext)
    cipher = []
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:                          # Same row
            cipher.append(matrix[r1][(c1 + 1) % 5])
            cipher.append(matrix[r2][(c2 + 1) % 5])
        elif c1 == c2:                        # Same column
            cipher.append(matrix[(r1 + 1) % 5][c1])
            cipher.append(matrix[(r2 + 1) % 5][c2])
        else:                                  # Rectangle
            cipher.append(matrix[r1][c2])
            cipher.append(matrix[r2][c1])
    return ''.join(cipher)


def playfair_decrypt(ciphertext: str, key: str) -> str:
    matrix = build_matrix(key)
    pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    plain = []
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            plain.append(matrix[r1][(c1 - 1) % 5])
            plain.append(matrix[r2][(c2 - 1) % 5])
        elif c1 == c2:
            plain.append(matrix[(r1 - 1) % 5][c1])
            plain.append(matrix[(r2 - 1) % 5][c2])
        else:
            plain.append(matrix[r1][c2])
            plain.append(matrix[r2][c1])
    return ''.join(plain)


def print_matrix(matrix):
    print("\n  Playfair Key Matrix:")
    for row in matrix:
        print("  " + " ".join(row))


def main():
    print("=" * 50)
    print("       Practical 4 – Playfair Cipher")
    print("=" * 50)

    key = input("Enter key      : ")
    plaintext = input("Enter plaintext: ")

    matrix = build_matrix(key)
    print_matrix(matrix)

    pairs = prepare_text(plaintext)
    print(f"\nDigraphs : {' '.join(pairs)}")

    encrypted = playfair_encrypt(plaintext, key)
    decrypted = playfair_decrypt(encrypted, key)

    print(f"\nOriginal  : {plaintext}")
    print(f"Encrypted : {encrypted}")
    print(f"Decrypted : {decrypted}")


if __name__ == "__main__":
    main()
