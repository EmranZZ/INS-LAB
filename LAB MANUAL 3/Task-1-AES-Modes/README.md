# Task 1: AES Encryption Using Different Modes

## Algorithms Used:
- AES-128-ECB
- AES-128-CBC
- AES-128-CFB

## Commands Used:

### AES-128-ECB
openssl enc -aes-128-ecb -e -in plain.txt -out ecb.bin -K 00112233445566778899aabbccddeeff

### AES-128-CBC
openssl enc -aes-128-cbc -e -in plain.txt -out cbc.bin -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10

### AES-128-CFB
openssl enc -aes-128-cfb -e -in plain.txt -out cfb.bin -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10

## Observation:
All modes successfully encrypted and decrypted the file correctly using the same key and IV.
