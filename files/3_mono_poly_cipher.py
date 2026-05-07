# ============================================================
#  Practical 3 – Monoalphabetic & Polyalphabetic Cipher
# ============================================================
import random
import string


# ──────────────────────────────────────────────
#  PART A : Monoalphabetic Cipher
# ──────────────────────────────────────────────
def generate_mono_key() -> dict:
    """Randomly shuffle the alphabet to form a substitution key."""
    shuffled = list(string.ascii_uppercase)
    random.shuffle(shuffled)
    return {string.ascii_uppercase[i]: shuffled[i] for i in range(26)}


def mono_encrypt(plaintext: str, key: dict) -> str:
    result = []
    for ch in plaintext.upper():
        if ch.isalpha():
            result.append(key[ch])
        else:
            result.append(ch)
    return ''.join(result)


def mono_decrypt(ciphertext: str, key: dict) -> str:
    reverse_key = {v: k for k, v in key.items()}
    result = []
    for ch in ciphertext.upper():
        if ch.isalpha():
            result.append(reverse_key[ch])
        else:
            result.append(ch)
    return ''.join(result)


# ──────────────────────────────────────────────
#  PART B : Polyalphabetic Cipher (Vigenère)
# ──────────────────────────────────────────────
def vigenere_encrypt(plaintext: str, key: str) -> str:
    key = key.upper()
    result = []
    ki = 0
    for ch in plaintext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[ki % len(key)]) - ord('A')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            ki += 1
        else:
            result.append(ch)
    return ''.join(result)


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    key = key.upper()
    result = []
    ki = 0
    for ch in ciphertext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[ki % len(key)]) - ord('A')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
            ki += 1
        else:
            result.append(ch)
    return ''.join(result)


# ──────────────────────────────────────────────
#  MAIN
# ──────────────────────────────────────────────
def main():
    print("=" * 55)
    print("  Practical 3 – Monoalphabetic & Polyalphabetic Cipher")
    print("=" * 55)

    # --- Monoalphabetic ---
    print("\n[A] Monoalphabetic Cipher")
    plaintext = input("Enter plaintext : ")
    key = generate_mono_key()
    print("Substitution Key (A→?):")
    print("  Plain :", ''.join(string.ascii_uppercase))
    print("  Cipher:", ''.join(key[c] for c in string.ascii_uppercase))

    enc = mono_encrypt(plaintext, key)
    dec = mono_decrypt(enc, key)
    print(f"\nOriginal  : {plaintext}")
    print(f"Encrypted : {enc}")
    print(f"Decrypted : {dec}")

    # --- Vigenère ---
    print("\n[B] Polyalphabetic Cipher (Vigenère)")
    plaintext2 = input("Enter plaintext : ")
    vkey = input("Enter keyword   : ")

    enc2 = vigenere_encrypt(plaintext2, vkey)
    dec2 = vigenere_decrypt(enc2, vkey)
    print(f"\nOriginal  : {plaintext2}")
    print(f"Encrypted : {enc2}")
    print(f"Decrypted : {dec2}")


if __name__ == "__main__":
    main()
