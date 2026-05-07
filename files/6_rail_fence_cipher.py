# ============================================================
#  Practical 6 – Rail Fence Cipher (Transposition)
# ============================================================


def rail_fence_encrypt(plaintext: str, rails: int) -> str:
    # Create empty rails
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1  # 1 = down, -1 = up

    for ch in plaintext:
        fence[rail].append(ch)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    # Visualise the fence
    print("\n  Rail Fence Pattern:")
    for i, row in enumerate(fence):
        slots = ['.' for _ in plaintext]
        idx = 0
        r = 0
        d = 1
        for j, ch in enumerate(plaintext):
            if r == i:
                slots[j] = ch
            if r == 0:
                d = 1
            elif r == rails - 1:
                d = -1
            r += d
        print(f"  Rail {i}: {''.join(slots)}")

    return ''.join(''.join(row) for row in fence)


def rail_fence_decrypt(ciphertext: str, rails: int) -> str:
    n = len(ciphertext)
    # Determine the pattern
    pattern = [0] * n
    rail = 0
    direction = 1
    for i in range(n):
        pattern[i] = rail
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    # Sort indices by rail
    indices = sorted(range(n), key=lambda i: pattern[i])
    result = [''] * n
    for char, idx in zip(ciphertext, indices):
        result[idx] = char
    return ''.join(result)


def main():
    print("=" * 50)
    print("     Practical 6 – Rail Fence Cipher")
    print("=" * 50)

    plaintext = input("\nEnter plaintext : ")
    rails = int(input("Enter number of rails: "))

    if rails < 2:
        print("Rails must be at least 2.")
        return

    encrypted = rail_fence_encrypt(plaintext, rails)
    decrypted = rail_fence_decrypt(encrypted, rails)

    print(f"\nOriginal  : {plaintext}")
    print(f"Encrypted : {encrypted}")
    print(f"Decrypted : {decrypted}")


if __name__ == "__main__":
    main()
