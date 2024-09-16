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
