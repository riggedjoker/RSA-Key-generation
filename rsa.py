#a simple python script that encrypts and decrypts using rsa
#author: riggedjoker

from math import gcd
# Function to find modular inverse
def mod_inverse(a, b):
    a = a % b
    for x in range(1, b):
        if (a * x) % b == 1:
            return x
    return -1

# RSA key generation
def rsa_key_generation(p, q, e):
    n = p * q
    n_phi = (p - 1) * (q - 1)
    # Ensure gcd(e, n_phi) == 1
    if gcd(e, n_phi) != 1:
        raise ValueError("GCD ERROR: e and phi(n) are not coprime.")
    d = mod_inverse(e, n_phi)
    if d == -1:
        raise ValueError("Error finding modular inverse for e.")
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key

# RSA encryption
def rsa_encryption(m, public_key):
    n, e = public_key
    c = pow(m, e, n)
    return c


# Main script
if __name__ == "__main__":
    print("=== RSA Encryption and Decryption ===")

        # User inputs for RSA parameters
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))
    e = int(input("Enter the public exponent (e): "))

    # Generate keys
    public_key, private_key = rsa_key_generation(p, q, e)
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # User input for plaintext
    plaintext = input("Enter the plaintext (text or number): ")

    # Convert plaintext to integer if it's text
    if plaintext.isdigit():
        m = int(plaintext)
    else:
        m = int.from_bytes(plaintext.encode(), "big")

    # Encrypt and decrypt
    ciphertext = rsa_encryption(m, public_key)
    print("Ciphertext:", ciphertext)
