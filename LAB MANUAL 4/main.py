import os
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# required imports for rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# required imports for rsa digital signature
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# aes encryption and decryption functions
def generate_aes_key(key_size):
    key = get_random_bytes(key_size // 8)
    filename = f"keys/aes_{key_size}.key"
    
    with open(filename, "wb") as f:
        f.write(key)
    
    print(f"AES-{key_size} key generated and saved in {filename}")

def aes_encrypt(key_size, mode):
    filename = f"keys/aes_{key_size}.key"
    
    with open(filename, "rb") as f:
        key = f.read()

    with open("inputs/plain.txt", "rb") as f:
        data = f.read()

    start = time.time()

    if mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))

    elif mode == "CFB":
        cipher = AES.new(key, AES.MODE_CFB)
        ciphertext = cipher.iv + cipher.encrypt(data)

    end = time.time()

    with open("outputs/aes_encrypted.bin", "wb") as f:
        f.write(ciphertext)

    print("Encryption Done.")
    print("Time taken:", end - start, "seconds")


def aes_decrypt(key_size, mode):
    filename = f"keys/aes_{key_size}.key"
    
    with open(filename, "rb") as f:
        key = f.read()

    with open("outputs/aes_encrypted.bin", "rb") as f:
        data = f.read()

    start = time.time()

    if mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
        plaintext = unpad(cipher.decrypt(data), AES.block_size)

    elif mode == "CFB":
        iv = data[:16]
        actual_data = data[16:]
        cipher = AES.new(key, AES.MODE_CFB, iv=iv)
        plaintext = cipher.decrypt(actual_data)

    end = time.time()

    print("Decrypted Text:")
    print(plaintext.decode())

    print("Time taken:", end - start, "seconds")


# rsa encryption and decryption functions
def generate_rsa_keys(key_size):
    key = RSA.generate(key_size)

    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("keys/rsa_private.pem", "wb") as f:
        f.write(private_key)

    with open("keys/rsa_public.pem", "wb") as f:
        f.write(public_key)

    print(f"RSA {key_size}-bit keys generated and saved.")


def rsa_encrypt():
    with open("keys/rsa_public.pem", "rb") as f:
        public_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(public_key)

    with open("inputs/plain.txt", "rb") as f:
        data = f.read()

    start = time.time()
    ciphertext = cipher.encrypt(data)
    end = time.time()

    with open("outputs/rsa_encrypted.bin", "wb") as f:
        f.write(ciphertext)

    print("RSA Encryption Done.")
    print("Time taken:", end - start, "seconds")


def rsa_decrypt():
    with open("keys/rsa_private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(private_key)

    with open("outputs/rsa_encrypted.bin", "rb") as f:
        ciphertext = f.read()

    start = time.time()
    plaintext = cipher.decrypt(ciphertext)
    end = time.time()

    print("Decrypted Text:")
    print(plaintext.decode())

    print("Time taken:", end - start, "seconds")


# rsa digital signature functions
def rsa_sign():
    with open("keys/rsa_private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())

    with open("inputs/plain.txt", "rb") as f:
        data = f.read()

    hash_obj = SHA256.new(data)

    start = time.time()
    signature = pkcs1_15.new(private_key).sign(hash_obj)
    end = time.time()

    with open("outputs/signature.bin", "wb") as f:
        f.write(signature)

    print("Signature generated and saved to outputs/signature.bin")
    print("Time taken:", end - start, "seconds")


def rsa_verify():
    with open("keys/rsa_public.pem", "rb") as f:
        public_key = RSA.import_key(f.read())

    with open("inputs/plain.txt", "rb") as f:
        data = f.read()

    with open("outputs/signature.bin", "rb") as f:
        signature = f.read()

    hash_obj = SHA256.new(data)

    start = time.time()
    try:
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        print("Signature is VALID.")
    except (ValueError, TypeError):
        print("Signature is INVALID.")
    end = time.time()

    print("Time taken:", end - start, "seconds")


if __name__ == "__main__":
    generate_rsa_keys(2048)
    rsa_sign()
    rsa_verify()

