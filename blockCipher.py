# Part 1: Basic Block Cipher Implementation

# 1. Define Block and Key Sizes
BLOCK_SIZE = 8 
KEY_SIZE = 8 

# 2. Implement a Simple Substitution Box (S-box)

# A 4x4 substitution box (S-box)
S_BOX = {
    0b0000: 0b1110,  # Example mappings
    0b0001: 0b0100,
    0b0010: 0b1101,
    0b0011: 0b0001,
    0b0100: 0b0010,
    0b0101: 0b1111,
    0b0110: 0b1011,
    0b0111: 0b1000,
    0b1000: 0b0011,
    0b1001: 0b1010,
    0b1010: 0b0110,
    0b1011: 0b1100,
    0b1100: 0b0101,
    0b1101: 0b1001,
    0b1110: 0b0000,
    0b1111: 0b0111
}

# Function to substitute 4-bit values using the S-box
def substitute(nibble):
    return S_BOX[nibble]

# 3. Implement a Simplified Permutation
# Permutation table: Reorders the 8 bits in the block
PERMUTATION_TABLE = [7, 6, 5, 4, 3, 2, 1, 0]  # Example: reverse the bit order

# Function to permute bits in the block
def permute(block):
    permuted_block = 0
    for i, bit_pos in enumerate(PERMUTATION_TABLE):
        permuted_block |= ((block >> bit_pos) & 1) << i
    return permuted_block

# 4. Implement a Basic Feistel Function
# Feistel function using XOR with the key and permutation
def feistel_function(right, key):
    # XOR the right half with the key
    return right ^ (key & 0b1111)  # Assume the Feistel function works on 4 bits

# 5. Combine Components for Encryption

def encrypt_block(block, key):
    # Split the block into left and right halves
    left = (block >> 4) & 0b1111
    right = block & 0b1111
    
    # Feistel function on the right half
    new_right = feistel_function(right, key)
    
    # Substitution on the right half
    new_right = substitute(new_right)
    
    # Permutation
    new_right = permute(new_right)
    
    # Swap left and right and combine them into a single 8-bit block
    encrypted_block = (new_right << 4) | left
    return encrypted_block

# Test the implementation
block = 0b10101100  # Example 8-bit block
key = 0b11001010    # Example 8-bit key

encrypted_block = encrypt_block(block, key)
print(f"Original block: {bin(block)}")
print(f"Encrypted block: {bin(encrypted_block)}")

#Part2 : Extend to modes of operation

# 1.Implement ECB mode
def ecb_encrypt(plaintext, key):
    """Encrypt the plaintext using ECB mode."""
    ciphertext = []
    for block in plaintext:
        encrypted_block = block_cipher_encrypt(block, key)
        ciphertext.append(encrypted_block)
    return ciphertext

def ecb_decrypt(ciphertext, key):
    """Decrypt the ciphertext using ECB mode."""
    decrypted_text = []
    for block in ciphertext:
        decrypted_block = block_cipher_decrypt(block, key)
        decrypted_text.append(decrypted_block)
    return decrypted_text

# 2.Implement CBC mode
def cbc_encrypt(plaintext, key, iv):
    """Encrypt the plaintext using CBC mode."""
    ciphertext = []
    previous_block = iv
    for block in plaintext:
        # XOR with the previous ciphertext block or IV
        xor_block = block ^ previous_block
        encrypted_block = block_cipher_encrypt(xor_block, key)
        ciphertext.append(encrypted_block)
        previous_block = encrypted_block  # Update previous block
    return ciphertext

def cbc_decrypt(ciphertext, key, iv):
    """Decrypt the ciphertext using CBC mode."""
    decrypted_text = []
    previous_block = iv
    for block in ciphertext:
        decrypted_block = block_cipher_decrypt(block, key)
        # XOR with the previous ciphertext block or IV
        plaintext_block = decrypted_block ^ previous_block
        decrypted_text.append(plaintext_block)
        previous_block = block  # Update previous block
    return decrypted_text

# 3.Implement additional mode (counter (CTR) mode)
def ctr_encrypt(plaintext, key, nonce):
    """Encrypt the plaintext using CTR mode."""
    ciphertext = []
    counter = 0
    for block in plaintext:
        # Encrypt the nonce + counter and XOR with plaintext
        counter_block = nonce ^ counter
        keystream = block_cipher_encrypt(counter_block, key)
        encrypted_block = block ^ keystream
        ciphertext.append(encrypted_block)
        counter += 1  # Increment counter for next block
    return ciphertext

def ctr_decrypt(ciphertext, key, nonce):
    """Decrypt the ciphertext using CTR mode (same as encryption)."""
    decrypted_text = []
    counter = 0
    for block in ciphertext:
        counter_block = nonce ^ counter
        keystream = block_cipher_encrypt(counter_block, key)
        decrypted_block = block ^ keystream
        decrypted_text.append(decrypted_block)
        counter += 1
    return decrypted_text

