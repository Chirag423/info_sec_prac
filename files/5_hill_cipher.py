# ============================================================
#  Practical 5 – Hill Cipher
# ============================================================
import numpy as np


def mod_inverse(a, m=26):
    """Extended Euclidean algorithm to find modular inverse."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for {a} mod {m}")


def matrix_mod_inverse(matrix, mod=26):
    """Compute the modular inverse of a matrix."""
    det = int(round(np.linalg.det(matrix))) % mod
    det_inv = mod_inverse(det, mod)
    size = matrix.shape[0]

    if size == 2:
        adj = np.array([
            [ matrix[1][1], -matrix[0][1]],
            [-matrix[1][0],  matrix[0][0]]
        ])
    else:
        # General adjugate via cofactor matrix
        cofactors = np.zeros_like(matrix, dtype=int)
        for r in range(size):
            for c in range(size):
                minor = np.delete(np.delete(matrix, r, axis=0), c, axis=1)
                cofactors[r][c] = ((-1) ** (r + c)) * int(round(np.linalg.det(minor)))
        adj = cofactors.T

    inv = (det_inv * adj) % mod
    return inv.astype(int)


def text_to_vector(text: str):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]


def vector_to_text(vec):
    return ''.join(chr(int(round(v)) % 26 + ord('A')) for v in vec)


def hill_encrypt(plaintext: str, key_matrix: np.ndarray) -> str:
    n = key_matrix.shape[0]
    nums = text_to_vector(plaintext)
    # Pad with 'X' if needed
    while len(nums) % n != 0:
        nums.append(ord('X') - ord('A'))

    cipher_nums = []
    for i in range(0, len(nums), n):
        block = np.array(nums[i:i+n])
        result = key_matrix.dot(block) % 26
        cipher_nums.extend(result)
    return vector_to_text(cipher_nums)


def hill_decrypt(ciphertext: str, key_matrix: np.ndarray) -> str:
    inv_key = matrix_mod_inverse(key_matrix)
    return hill_encrypt(ciphertext, inv_key)


def main():
    print("=" * 50)
    print("       Practical 5 – Hill Cipher")
    print("=" * 50)

    print("\nUsing default 2×2 key matrix:")
    print("  [[3, 3], [2, 5]]")
    key_matrix = np.array([[3, 3], [2, 5]])

    plaintext = input("\nEnter plaintext (alphabets only): ")

    encrypted = hill_encrypt(plaintext, key_matrix)
    decrypted = hill_decrypt(encrypted, key_matrix)

    print(f"\nKey Matrix :\n{key_matrix}")
    print(f"Original   : {plaintext.upper()}")
    print(f"Encrypted  : {encrypted}")
    print(f"Decrypted  : {decrypted}")

    # Custom key option
    choice = input("\nWant to enter a custom 2×2 key matrix? (y/n): ").strip().lower()
    if choice == 'y':
        print("Enter 4 values row-by-row (space separated):")
        row1 = list(map(int, input("Row 1: ").split()))
        row2 = list(map(int, input("Row 2: ").split()))
        custom_key = np.array([row1, row2])
        enc = hill_encrypt(plaintext, custom_key)
        dec = hill_decrypt(enc, custom_key)
        print(f"\nCustom Key Matrix :\n{custom_key}")
        print(f"Encrypted  : {enc}")
        print(f"Decrypted  : {dec}")


if __name__ == "__main__":
    main()
