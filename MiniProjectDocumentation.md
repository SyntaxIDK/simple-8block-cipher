# Basic Block Cipher Implementation (Part 1)

> Objective: Implement a simple symmetric block cipher that encrypts an
> 8-bit block using a basic substitution-permutation structure.

## Define Block and Key Sizes

> • Block Size: 8 bits.
>
> • Key Size: 8 bits.

## Implement a Simple Substitution Box (S-box)

> • Create a 4x4 substitution box.
>
> • Define a function that substitutes 4-bit input values according to
> the S-box.

## Implement a Simplified Permutation

> • Define a permutation table that shuffles the bits in the block.
>
> • Implement a function to permute bits according to the table.

## Implement a Basic Feistel Function

> • Create a basic Feistel function using XOR operations.
>
> • The function should take 4 bits as input and return a transformed 4
> bits.

## Combine Components for Encryption

> • Implement a single-round encryption function using the substitution
> box,
>
> permutation, and Feistel function.
>
> • Ensure the function can encrypt an 8-bit block using a given 8-bit
> key.

### Github link to code : <https://github.com/SyntaxIDK/cryptography-miniProject>. {#github-link-to-code-httpsgithub.comsyntaxidkcryptography-miniproject.}

### Brief explanation:

I.  **Substitution box (S-box)**

> The S-box operates as a simple substitution table that is a necessary
> part of block ciphers. An S-box takes several input bits and
> substitutes them with output bits, using a substitution table, with
> each small block of input bits being substituted for a corresponding
> block of output bits. The function of an S-box is to introduce
> non-linearity in an encryption process. When an S-box is implemented
> into a block cipher, it can make the system more tolerant to
> cryptanalytic tests.
>
> Examples of a simplified S-boxes is a 4x4 S-box that takes in 4-bits
> of input and substitutes them for four bits of output. Thus, the S-box
> helps to obscure the relationship between the plain-text, key, and
> cipher-text.

II. **Permutation**

> Another fundamental cryptographic operation is permutation which
> rearranges the order of bits within the entire block. Just as
> substitution follows after permutation, the permute operation
> rearranges elements according to an associated permutation table. This
> operation accomplishes another goal in cryptographic systems:
> diffusion, or spreading out the effect of designated changes to the
> plaintext input over the ciphertext output, which makes it difficult
> for an attacker to find a one-to-one pattern between the plaintext
> input and ciphertext output.

III. **Feistel function**

> The Feistel function comprises a crucial framework in Feistel-type
> block ciphers which function by breaking the block in half so one half
> can be be applied to the Feistel function (that might involve, among
> other things, XORing it with part of the key), and combining the
> result with the other half of the block, again potentially completing
> an XOR. The upper and lower halves are switched at the end of the
> round and the whole process is repeated for some number of rounds.
>
> In the context of my project I am treating a simple Feistel function
> whereby you input 4 bits, the Feistel function transforms those bits
> using an XOR operation with the key/stuff. It outputs, or returns, the
> transformed 4 bits. This structure appears in many block ciphers to
> accomplish the requirement of performing confusion and diffusion
> across multiple rounds and achieve security by doing so.

# Extend to Modes of Operation (Part 2)

Objective: Implement two basic modes of operation using the block
cipher.

## Implement Electronic Codebook (ECB) Mode

> **How ECB Mode Works:**
>
> In **ECB mode**, the plaintext is divided into fixed-size blocks (8
> bits in your case), and each block is encrypted independently using
> the block cipher. Decryption follows the same process, where each
> block is decrypted individually. The main downside of ECB is that
> identical plaintext blocks will produce identical ciphertext blocks,
> making it susceptible to pattern analysis.

## Implement Cipher Block Chaining (CBC) Mode

> **How CBC Mode Works:**
>
> In **CBC mode**, the first plaintext block is XORed with an
> initialization vector (IV) before encryption. Each subsequent
> plaintext block is XORed with the previous ciphertext block before
> encryption. This ensures that even identical plaintext blocks result
> in different ciphertexts. For decryption, the ciphertext blocks are
> decrypted and then XORed with the previous ciphertext block (or IV for
> the first block) to retrieve the plaintext.

## Bonus Marks: Implement an Additional Mode of Operation

> **Example: Counter (CTR) Mode**
>
> In **CTR mode**, instead of chaining blocks, a counter value is
> encrypted for each block, and the result is XORed with the plaintext.
> This mode allows parallel encryption and decryption, as each block is
> independent of the others. CTR mode is resistant to error propagation
> and does not require padding.

### Github link to code : <https://github.com/SyntaxIDK/cryptography-miniProject>. {#github-link-to-code-httpsgithub.comsyntaxidkcryptography-miniproject.-1}

### Differences between ECB and CBC modes:

- **ECB Mode**:

<!-- -->

- Processes each block independently.

- Identical plaintext blocks will produce identical ciphertext blocks.

- Susceptible to pattern analysis and not secure for large amounts of
  data.

<!-- -->

- **CBC Mode**:

<!-- -->

- Each block is XORed with the previous ciphertext block, making it more
  secure.

- The same plaintext blocks will produce different ciphertext due to
  chaining.

- More resistant to certain attacks but slower since blocks are
  processed sequentially.

# Encryption and decryption of sample input (Part 3)

Objective: Demonstrate the use of your block cipher and modes of
operation by encrypting and decrypting sample input.

### Github link to code : <https://github.com/SyntaxIDK/cryptography-miniProject>. {#github-link-to-code-httpsgithub.comsyntaxidkcryptography-miniproject.-2}
