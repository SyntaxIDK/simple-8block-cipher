# Cryptography Mini Project - Block Cipher

This repository contains a mini project for the course CSI2108 Cryptographic Concepts, focusing on the implementation of a basic symmetric block cipher. The cipher operates on 8-bit blocks and uses a substitution-permutation network (SPN) structure, incorporating a simple S-box, permutation table, and Feistel function.

## Overview:
This mini-project demonstrates how to implement a block cipher using symmetric encryption. The cipher encrypts 8-bit blocks with an 8-bit key using basic cryptographic techniques like substitution, permutation, and the Feistel function. Two encryption modes, Electronic Codebook (ECB) and Cipher Block Chaining (CBC), can be explored to understand how they affect data encryption.

## Features:
8-bit block encryption using symmetric keys.
Substitution-permutation network (SPN) design.
Simple 4x4 S-box for substitution.
Permutation table for bit shuffling.
Feistel function for encryption transformation.
Single-round encryption to illustrate block cipher functionality.

## Block Cipher Components:
Substitution Box (S-box): A simple 4x4 lookup table that substitutes 4-bit values during encryption.
Permutation Table: A bit shuffling mechanism that reorders the bits in a block.
Feistel Function: A basic function applying XOR operations to a 4-bit block using the key.

## Requirements:
Python 3.x
Ensure Python is installed on your system.

## Installation
Clone the repository:

### `git clone https://github.com/SyntaxIDK/cryptography-miniProject.git`
### `cd cryptography-miniProject`

## Usage
Open the `blockCipher.py` file in a text editor.

Modify the block and key variables in the script to experiment with different inputs.

## Run the Python script:
### `python blockCipher.py`
The program will print the original 8-bit block and the encrypted block as output.

## Example output:
Original block: 0b10101100
Encrypted block: 0b11001110

