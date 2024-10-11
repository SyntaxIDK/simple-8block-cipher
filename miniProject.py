import random

# Block and Key Sizes
BLOCK_SIZE = 8  # 8-bit block
KEY_SIZE = 8    # 8-bit key

# Create a 4x4 substitution box
S_BOX = {
    0b0000: 0b1110, 0b0001: 0b0100, 0b0010: 0b1101, 0b0011: 0b0001,
    0b0100: 0b0010, 0b0101: 0b1111, 0b0110: 0b1011, 0b0111: 0b1000,
    0b1000: 0b0011, 0b1001: 0b1010, 0b1010: 0b0110, 0b1011: 0b1100,
    0b1100: 0b0101, 0b1101: 0b1001, 0b1110: 0b0000, 0b1111: 0b0111
}

# Permutation table that shuffles the bits in the block
PERMUTATION = [1, 5, 2, 0, 3, 7, 4, 6]

# Function to substitute 4-bit input using the S-box
def substitute(nibble):
    return S_BOX[nibble]

# Function to permute bits according to the permutation table
def permute(block):
    permuted_block = 0
    for i, bit_pos in enumerate(PERMUTATION):
        permuted_block |= ((block >> bit_pos) & 1) << i
    return permuted_block

# Implement a Basic Feistel Function
# Feistel function using XOR with the key
def feistel(right, key):
    return right ^ key

# Combine Components for Encryption
# Function to encrypt a single 8-bit block using the block cipher (1 round)
def block_cipher_encrypt(block, key):
    # Split block into left and right 4-bit halves
    left = (block & 0xF0) >> 4  # Extract left 4 bits
    right = block & 0x0F        # Extract right 4 bits

    # Apply the Feistel function and substitution
    right = substitute(right)
    left ^= feistel(right, key)

    # Recombine left and right halves after substitution and permutation
    combined = (left << 4) | right
    return permute(combined)

# Decryption using the block cipher
def block_cipher_decrypt(block, key):
    # Inverse permutation
    inverse_permuted = permute(block)  # Permutation is symmetrical

    # Split block into left and right 4-bit halves
    left = (inverse_permuted & 0xF0) >> 4
    right = inverse_permuted & 0x0F

    # Reverse Feistel function and substitution
    left ^= feistel(right, key)
    right = substitute(right)

    # Recombine left and right halves
    return (left << 4) | right

# Implement Electronic Codebook (ECB) Mode
def ecb_encrypt(plaintext, key):
    return [block_cipher_encrypt(block, key) for block in plaintext]

def ecb_decrypt(ciphertext, key):
    return [block_cipher_decrypt(block, key) for block in ciphertext]

# Implement Cipher Block Chaining (CBC) Mode
def cbc_encrypt(plaintext, key, iv):
    ciphertext = []
    prev_block = iv
    for block in plaintext:
        block ^= prev_block  # XOR with previous ciphertext (or IV)
        encrypted_block = block_cipher_encrypt(block, key)
        ciphertext.append(encrypted_block)
        prev_block = encrypted_block
    return ciphertext

def cbc_decrypt(ciphertext, key, iv):
    plaintext = []
    prev_block = iv
    for block in ciphertext:
        decrypted_block = block_cipher_decrypt(block, key)
        plaintext_block = decrypted_block ^ prev_block  # XOR with previous ciphertext (or IV)
        plaintext.append(plaintext_block)
        prev_block = block
    return plaintext

# Prepare Sample Input
# Helper function to convert a string to binary (8-bit blocks)
def string_to_binary(text):
    return [ord(c) for c in text]

# Helper function to convert binary (8-bit blocks) back to string
def binary_to_string(binary_data):
    return ''.join([chr(b) for b in binary_data])

# Main function for testing
def main():
    plaintext = string_to_binary("HELLO")  # Provide plaintext message and key
    key = 0b10101010  # Example 8-bit key
    iv = 0b01010101   # Example 8-bit IV for CBC mode

    print("Original plaintext (binary):", [bin(block) for block in plaintext])

    # Encrypt using ECB mode
    ciphertext_ecb = ecb_encrypt(plaintext, key)
    print("Ciphertext (ECB mode):", [bin(block) for block in ciphertext_ecb])

    # Decrypt using ECB mode
    decrypted_ecb = ecb_decrypt(ciphertext_ecb, key)
    print("Decrypted plaintext (ECB mode):", binary_to_string(decrypted_ecb))

    # Encrypt using CBC mode
    ciphertext_cbc = cbc_encrypt(plaintext, key, iv)
    print("Ciphertext (CBC mode):", [bin(block) for block in ciphertext_cbc])

    # Decrypt using CBC mode
    decrypted_cbc = cbc_decrypt(ciphertext_cbc, key, iv)
    print("Decrypted plaintext (CBC mode):", binary_to_string(decrypted_cbc))

if __name__ == "__main__":
    main()
