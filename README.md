# Cryptography Mini Project

This repository depicts the design and implementation of a simple 8-bit block cipher providing symmetric encryption using a substitution-permutation network (SPN), including an S-box, permutation table, and Feistel scheme. The cipher implements and evaluates two principal modes of encryption: Electronic Codebook (ECB) and Cipher Block Chaining (CBC). The report also discusses the mathematics of these modes of encryption, examining the complexity and security aspects of the cipher design. The efficiency and strength of the cipher are demonstrated through the testing of encryption and decryption on sample data. This study emphasizes the relevance of secure encryption approaches to support data confidentiality and data integrity in cryptographic systems.

## Overview:
In the current digital era, ensuring that unauthorized individuals cannot access private information is critical in today's organization. The concept of cryptography is essential in establishing this goal. The objective of this project is to develop an uncomplicated block cipher using symmetric cryptography, pertaining that the same key is required to decrypt the available data. The increasing popularity of symmetric ciphers stems from their uncomplicated ability to perform. This report describes the design and assessment of the proposed block cipher with a focus on its two modes of operation, ECB and CBC.

The block cipher manipulates the 8-bit blocks and the presented 8-bit keys in both modes. The design relies on accepted cryptographic concepts. Confusion and diffusion are created through an S-box and a permutation table because the goal is to ensure that even the minimal change in the in-put representation occupies excessive change in the output representation. These two independent components also increase the difficulty of attacking the system by a cryptographical activity.

## Features:
•	Cipher Design: Develop a symmetric block cipher using substitution, permutation, and the Feistel structure.
•	Operational Modes: Implement and compare the functionality of ECB and CBC modes.
•	Encryption and Decryption: Verify the cipher's effectiveness by encrypting and decrypting example inputs.
•	Documentation: Provide a comprehensive analysis of the system’s architecture, complexity, and security considerations.

## Requirements:
Python 3.x
Ensure Python is installed on your system.

## Installation
Clone the repository:

### `git clone https://github.com/SyntaxIDK/cryptography-miniProject.git`
### `cd cryptography-miniProject`

## Usage
Open the .py files in a text editor.

Modify the block and key variables in the script to experiment with different inputs.

## Run the Python script:
### `python <name>.py`
The program will print the original 8-bit block and the encrypted block as output.


