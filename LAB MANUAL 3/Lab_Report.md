# Lab Manual 3: Symmetric Encryption & Hashing

**Course:** Information and Network Security  
**Student Name:** Emran Ahmed  
**Platform Used:** Ubuntu (WSL) + OpenSSL + HxD Hex Editor  

---

# Introduction

This lab focuses on symmetric encryption and hashing using OpenSSL. 
Different AES encryption modes, padding behavior, message digests, HMAC, 
and hash randomness properties were experimentally analyzed.

---

# Task 1: AES Encryption Using Different Modes

## Objective
To encrypt and decrypt a text file using AES-128 in different modes.

## Modes Tested
- AES-128-ECB
- AES-128-CBC
- AES-128-CFB

## Commands Used

Example (ECB):
openssl enc -aes-128-ecb -e -in plain.txt -out ecb.bin -K 00112233445566778899aabbccddeeff

Example (CBC):
openssl enc -aes-128-cbc -e -in plain.txt -out cbc.bin -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10

## Observation

All modes successfully encrypted and decrypted the file using the correct key and IV.

ECB encrypts blocks independently.
CBC uses chaining.
CFB works like a stream cipher.

---

# Task 2: ECB vs CBC (Image Encryption)

## Objective
To compare ECB and CBC encryption using a BMP image.

## Procedure
- Encrypted BMP using ECB and CBC.
- Replaced first 54 bytes (header) with original header.
- Opened encrypted images.

## Observation

ECB Mode:
The encrypted image still revealed the structure and patterns of the original image.

CBC Mode:
The encrypted image appeared completely random with no visible pattern.

## Conclusion

ECB mode is insecure because identical plaintext blocks produce identical ciphertext blocks.
CBC mode provides stronger security by chaining blocks.

---

# Task 3: Corrupted Ciphertext

## Objective
To observe error propagation behavior in different AES modes.

## Modes Tested
- ECB
- CBC
- CFB
- OFB

## Observation

ECB:
Only the corrupted block was affected.

CBC:
The corrupted block was fully destroyed and one byte of the next block was corrupted.

CFB:
Error propagated to several subsequent bytes.

OFB:
Only one byte was corrupted.

## Implication

OFB has minimal error propagation.
CBC provides strong encryption but propagates errors.
ECB is insecure and predictable.

---

# Task 4: Padding

## Objective
To test which AES modes require padding.

## Observation

ECB and CBC require padding because they operate on fixed 16-byte blocks.

CFB and OFB do not require padding because they operate like stream ciphers.

OpenSSL automatically applies PKCS#7 padding when required.

---

# Task 5: Generating Message Digest

## Algorithms Used
- MD5 (128-bit)
- SHA1 (160-bit)
- SHA256 (256-bit)

## Commands Used
openssl dgst -md5 message.txt  
openssl dgst -sha1 message.txt  
openssl dgst -sha256 message.txt  

## Observation

Different algorithms produce different output lengths.
SHA256 provides stronger security compared to MD5 and SHA1.

Even small changes in input produce completely different hashes.

---

# Task 6: Keyed Hash and HMAC

## Algorithms Used
- HMAC-MD5
- HMAC-SHA1
- HMAC-SHA256

## Command Example
openssl dgst -sha256 -hmac "mysecretkey" filename

## Observation

HMAC changes when:
- Message changes
- Key changes

Key length does not need to be fixed.
If the key is longer than block size, it is hashed first.
If shorter, it is padded internally.

HMAC provides both integrity and authentication.

---

# Task 7: Randomness of One-Way Hash

## Objective
To demonstrate the avalanche effect.

## Procedure
- Generated hash H1.
- Modified one bit in input.
- Generated hash H2.
- Compared H1 and H2.

## Observation

A single-bit modification in input resulted in a completely different hash output.

More than 50% of bits changed in the output.

This confirms the avalanche effect and strong randomness property of cryptographic hash functions.

---

# Conclusion

This lab provided hands-on experience with:

- AES encryption modes
- Block cipher behavior
- Error propagation
- Padding schemes
- Hash functions
- HMAC
- Avalanche effect

The experiments clearly demonstrated why ECB is insecure, 
how different modes behave under corruption, 
and how cryptographic hash functions provide strong integrity guarantees.

OpenSSL proved to be a powerful tool for performing practical cryptographic operations.

---
