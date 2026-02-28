# Task 2: ECB vs CBC

## Commands Used:

### ECB
openssl enc -aes-128-ecb -e -in pic_original.bmp -out pic_ecb.bmp -K 00112233445566778899aabbccddeeff

### CBC
openssl enc -aes-128-cbc -e -in pic_original.bmp -out pic_cbc.bmp -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10

## Observation:

ECB mode preserves patterns and image structure.
CBC mode destroys patterns completely.

Conclusion: ECB is insecure.
