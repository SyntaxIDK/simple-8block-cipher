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
