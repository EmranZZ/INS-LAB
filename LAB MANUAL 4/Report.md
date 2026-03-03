# Lab 4: Programming Symmetric & Asymmetric Cryptography

**Course:** CSE-478 Introduction to Computer Security  
**Student:** Emran Ahmed  
**Environment:** Ubuntu (WSL), Python 3.12  
**Libraries Used:** PyCryptodome, Matplotlib  

---

## 1. Objective

The objective of this lab is to implement symmetric and asymmetric cryptographic operations programmatically and study their internal behavior and execution performance.

The implemented functionalities include:

- AES Encryption/Decryption (128 & 256 bit, ECB & CFB mode)
- RSA Encryption/Decryption
- RSA Digital Signature
- SHA-256 Hashing
- Execution time measurement
- Graph plotting for key size vs execution time

---

## 2. Tools & Technologies Used

- Python 3.12
- PyCryptodome Library
- Matplotlib (for plotting graphs)
- Ubuntu Linux (WSL)

---

## 3. Program Design

A single Python program (`main.py`) was developed with a command-line menu system allowing users to select cryptographic operations similar to OpenSSL.

Keys are:
- Generated at first use
- Stored inside the `keys/` directory
- Loaded from files when required

Encrypted outputs and signatures are stored in the `outputs/` directory.

---

## 4. AES Implementation

### Key Features:
- Supports 128-bit and 256-bit keys
- Supports ECB and CFB modes
- Uses PKCS padding (for ECB)
- Encryption output stored in file
- Decryption displays plaintext

### Observations:
- ECB mode does not use IV
- CFB mode uses IV for randomness
- AES execution time increases slightly with key size

---

## 5. RSA Implementation

### Features:
- Key pair generation (private & public key)
- RSA encryption using OAEP padding
- RSA decryption using private key

### Observations:
- RSA encryption is slower than AES
- Execution time increases significantly with larger key sizes
- 4096-bit key noticeably slower than 1024-bit

---

## 6. RSA Digital Signature

### Process:
1. SHA-256 hash of input file generated
2. Hash signed using private key
3. Signature stored in file
4. Verification performed using public key

### Observation:
If even one character of the input file is changed, signature verification fails, demonstrating integrity protection and authenticity.

---

## 7. SHA-256 Hashing

The program generates a SHA-256 hash of a file and displays it on the console.

### Avalanche Effect:
Changing a single character in the input file produces a completely different hash output, proving strong diffusion property of cryptographic hash functions.

---

## 8. Execution Time Analysis

Execution time was measured using Python's `time` module.

Two graphs were plotted:

- AES Key Size vs Execution Time
- RSA Key Size vs Execution Time

### Results:

- AES execution time increases slightly as key size increases.
- RSA execution time increases exponentially with key size.
- RSA is computationally much heavier than AES.

### Security vs Performance Tradeoff:

- Larger key size → stronger security
- Larger key size → higher computational cost

---

## 9. How to Execute the Program

1. Activate virtual environment:
    source venv/bin/activate

2. Run program:
    python3 main.py


3. Follow menu instructions.

---

## 10. Folder Structure

```text
Lab-4-Programming-Crypto/
│
├── main.py
├── keys/
├── inputs/
├── outputs/
├── screenshots/
├── Lab_Report.md
└── README.md
```


---

## 11. References

The following resources were used while implementing this program:

1. PyCryptodome Official Documentation  
   https://pycryptodome.readthedocs.io

2. Python Cryptography Tutorial  
   https://www.laurentluce.com/posts/python-and-cryptography-with-pycrypto/

3. RSA & AES Concepts  
   William Stallings, Cryptography and Network Security (Textbook)

All code snippets were adapted and customized for academic implementation.

---

## 12. Conclusion

This lab provided hands-on experience in implementing symmetric and asymmetric cryptography from scratch using Python.

The study demonstrated:

- Practical encryption and decryption
- Digital signature creation and verification
- Cryptographic hashing
- Performance comparison between AES and RSA

The experiment clearly shows the tradeoff between security strength and computational cost.
