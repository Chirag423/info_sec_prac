# ============================================================
#  Practical 2 – Caesar Cipher (Substitution)
# ============================================================

def caesar_encrypt(plaintext: str, shift: int) -> str:
    result = []
    for ch in plaintext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)


def caesar_decrypt(ciphertext: str, shift: int) -> str:
    return caesar_encrypt(ciphertext, -shift)


def main():
    print("=" * 50)
    print("       Caesar Cipher")
    print("=" * 50)

    plaintext = input("Enter plaintext : ")
    shift = int(input("Enter shift (key): "))

    encrypted = caesar_encrypt(plaintext, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print(f"\nOriginal  : {plaintext}")
    print(f"Encrypted : {encrypted}")
    print(f"Decrypted : {decrypted}")

    # Demo with all shifts (brute force)
    print("\n--- Brute-Force (all 26 shifts) ---")
    for s in range(26):
        print(f"Shift {s:2d} : {caesar_decrypt(encrypted, s)}")


if __name__ == "__main__":
    main()
