# Task 6: Keyed Hash and HMAC

## Algorithms Used
- HMAC-MD5
- HMAC-SHA1
- HMAC-SHA256

## Command Example
openssl dgst -sha256 -hmac "mysecretkey" hmac_message.txt

## Observation

HMAC changes when:
- Message changes
- Key changes

Key length does not need to be fixed.
HMAC internally handles key padding and hashing.
