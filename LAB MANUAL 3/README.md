# Lab Manual 3: Symmetric Encryption & Hashing

**Course:** Information and Network Security  
**Student:** Emran Ahmed  
**Platform:** Ubuntu (WSL), OpenSSL, HxD Hex Editor  

---

## 📌 Overview

This lab focuses on practical implementation of symmetric encryption and cryptographic hashing using OpenSSL.

The experiments demonstrate:

- AES encryption using different modes
- Comparison between ECB and CBC
- Error propagation in different modes
- Padding behavior
- Message digest generation
- HMAC (Keyed hash)
- Avalanche effect in hash functions

All tasks are organized in separate folders for clarity and reproducibility.

---

## 📂 Folder Structure

Lab-Manual-3-Symmetric-Encryption-Hashing/
│
├── Task-1-AES-Modes/
├── Task-2-ECB-vs-CBC/
├── Task-3-Corrupted-Ciphertext/
├── Task-4-Padding/
├── Task-5-Message-Digest/
├── Task-6-HMAC/
├── Task-7-Hash-Randomness/
│
├── Lab_Report.md
└── README.md


Each task folder contains:
- Input files
- Encrypted/Generated outputs
- Commands used
- Task-specific README

---

## 🧪 Tasks Summary

### 🔐 Task 1: AES Encryption Modes
AES-128 encryption using:
- ECB
- CBC
- CFB

---

### 🖼 Task 2: ECB vs CBC (Image Encryption)
Demonstrated why ECB is insecure by encrypting a BMP image and observing visible patterns.

---

### ⚠ Task 3: Corrupted Ciphertext
Analyzed how different AES modes behave when one bit of ciphertext is corrupted.

---

### 📦 Task 4: Padding
Studied which encryption modes require padding and why.

---

### 🔎 Task 5: Message Digest
Generated hashes using:
- MD5
- SHA1
- SHA256

---

### 🔑 Task 6: HMAC
Generated keyed hashes using:
- HMAC-MD5
- HMAC-SHA1
- HMAC-SHA256

---

### 🎲 Task 7: Hash Randomness
Demonstrated avalanche effect by flipping one bit in input and observing drastic hash change.

Bonus:
C++ program implemented to count bit differences between two hashes.

---

## 🛠 Tools Used

- OpenSSL
- Ubuntu (WSL)
- HxD Hex Editor
- g++
- Nano Editor

---

## 🎯 Key Learning Outcomes

- Understanding AES encryption modes
- Difference between ECB and CBC
- Error propagation in block cipher modes
- Padding schemes
- Hashing algorithms
- HMAC authentication
- Avalanche effect in cryptographic hashes

---

## 📌 Conclusion

This lab provided practical hands-on experience with symmetric encryption and hashing techniques. The experiments reinforced theoretical concepts and demonstrated the security implications of different cryptographic modes.

---

