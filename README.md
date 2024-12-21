# Simple RSA Encryption Script

This repository contains a simple Python script that implements RSA encryption and decryption. It allows users to input their own prime numbers and public exponent, generating corresponding RSA keys, encrypting a plaintext message, and displaying the ciphertext.

## Features

- **RSA Key Generation**:
  - Generate public and private keys using user-provided prime numbers \( p \) and \( q \), and public exponent \( e \).
  - Ensures that \( e \) is coprime with \( \phi(n) \), where \( n = p \times q \) and \( \phi(n) = (p - 1) \times (q - 1) \).
- **Encryption**:
  - Encrypts plaintext (text or numeric input) using the generated public key.

## How It Works

The RSA algorithm in this script operates as follows:

1. **Key Generation**:
   - Calculates \( n \) (the modulus) as \( p \times q \).
   - Computes \( \phi(n) \) (Euler's totient function) as \( (p - 1) \times (q - 1) \).
   - Ensures \( \text{gcd}(e, \phi(n)) = 1 \).
   - Finds \( d \), the modular multiplicative inverse of \( e \) modulo \( \phi(n) \).
2. **Encryption**:
   - Uses the formula \( c = m^e \mod n \), where \( m \) is the plaintext and \( c \) is the ciphertext.

## Prerequisites

- **Python 3.x** is required to run the script.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/simple-rsa-script.git
   cd simple-rsa-script
   ```

2. Run the script:
   ```bash
   python3 rsa.py
   ```

3. Follow the prompts to:
   - Enter two prime numbers \( p \) and \( q \).
   - Provide a public exponent \( e \) that is coprime with \( \phi(n) \).
   - Input a plaintext message (as text or a numeric value).

## Example Usage

Here's a quick example of how to use the script:

```plaintext
=== RSA Encryption and Decryption ===
Enter a prime number (p): 61
Enter another prime number (q): 53
Enter the public exponent (e): 17
Public Key: (3233, 17)
Private Key: (3233, 2753)
Enter the plaintext (text or number): Hello
Ciphertext: 869
```

## Script Structure

### Functions

- **`mod_inverse(a, b)`**: Calculates the modular multiplicative inverse of \( a \) modulo \( b \).
- **`rsa_key_generation(p, q, e)`**:
  - Generates the RSA public and private keys.
  - Returns keys as tuples: `(n, e)` for the public key and `(n, d)` for the private key.
- **`rsa_encryption(m, public_key)`**:
  - Encrypts plaintext \( m \) using the public key \( (n, e) \).

### Main Script
The main script allows users to:
1. Input prime numbers \( p \), \( q \), and public exponent \( e \).
2. Generate and display the public and private keys.
3. Encrypt plaintext and display the resulting ciphertext.

## Limitations

- **Decryption Functionality**: This version of the script only includes encryption. Adding decryption functionality using the private key is straightforward.
- **Prime Number Input**: Users must ensure that \( p \) and \( q \) are prime numbers.

## Author

Created by **riggedjoker**.
