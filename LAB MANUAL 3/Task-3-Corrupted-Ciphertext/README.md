# Task 3: Corrupted Ciphertext Experiment

## Objective
To observe error propagation in different AES modes.

## Modes Tested
- AES-128-ECB
- AES-128-CBC
- AES-128-CFB
- AES-128-OFB

## Commands Used

Encryption example:
openssl enc -aes-128-cbc -e -in plain.txt -out cbc.bin -K ...

Decryption example:
openssl enc -aes-128-cbc -d -in cbc_corrupt.bin -out cbc_decrypted.txt -K ...

## Observation
ECB: Only one block corrupted.
CBC: One block fully corrupted + partial next block.
CFB: Error propagates partially.
OFB: Only one byte affected.
