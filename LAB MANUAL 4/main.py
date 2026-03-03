import os
import time
import matplotlib.pyplot as plt # automated time measurement and graphing

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# required imports for rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# required imports for rsa digital signature
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# aes encryption and decryption
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


# rsa encryption and decryption
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


# rsa signature generation and verification
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


# SHA-256 Hashing
def sha256_hash():
    with open("inputs/plain.txt", "rb") as f:
        data = f.read()

    start = time.time()
    hash_obj = SHA256.new(data)
    digest = hash_obj.hexdigest()
    end = time.time()

    print("SHA-256 Hash:")
    print(digest)
    print("Time taken:", end - start, "seconds")


# automated time measurement aes and rsa
def measure_aes_time():
    key_sizes = [128, 192, 256]
    times = []

    for size in key_sizes:
        generate_aes_key(size)
        start = time.time()
        aes_encrypt(size, "ECB")
        end = time.time()
        times.append(end - start)

    plt.plot(key_sizes, times)
    plt.xlabel("AES Key Size (bits)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("AES Key Size vs Execution Time")
    plt.savefig("outputs/aes_time_graph.png")
    plt.show()


def measure_rsa_time():
    key_sizes = [1024, 2048, 3072, 4096]
    times = []

    for size in key_sizes:
        generate_rsa_keys(size)
        start = time.time()
        rsa_encrypt()
        end = time.time()
        times.append(end - start)

    plt.plot(key_sizes, times)
    plt.xlabel("RSA Key Size (bits)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("RSA Key Size vs Execution Time")
    plt.savefig("outputs/rsa_time_graph.png")
    plt.show()


def menu():
    while True:
        print("\n====== Lab 4 Crypto Toolkit ======")
        print("1. Generate AES Key")
        print("2. AES Encrypt")
        print("3. AES Decrypt")
        print("4. Generate RSA Keys")
        print("5. RSA Encrypt")
        print("6. RSA Decrypt")
        print("7. RSA Sign")
        print("8. RSA Verify")
        print("9. SHA-256 Hash")
        print("10", "Measure AES Time")
        print("11", "Measure RSA Time")
        print("12. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            size = int(input("Enter AES key size (128 or 256): "))
            generate_aes_key(size)

        elif choice == "2":
            size = int(input("Enter AES key size (128 or 256): "))
            mode = input("Enter mode (ECB or CFB): ")
            aes_encrypt(size, mode)

        elif choice == "3":
            size = int(input("Enter AES key size (128 or 256): "))
            mode = input("Enter mode (ECB or CFB): ")
            aes_decrypt(size, mode)

        elif choice == "4":
            size = int(input("Enter RSA key size (e.g., 1024, 2048): "))
            generate_rsa_keys(size)

        elif choice == "5":
            rsa_encrypt()

        elif choice == "6":
            rsa_decrypt()

        elif choice == "7":
            rsa_sign()

        elif choice == "8":
            rsa_verify()

        elif choice == "9":
            sha256_hash()

        elif choice == "10":
            measure_aes_time()

        elif choice == "11":
            measure_rsa_time()

        elif choice == "12":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()