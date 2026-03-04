# 🔐 Information and Network Security Lab

A comprehensive collection of practical implementations and experiments covering fundamental concepts in **Information Security**, **Cryptography**, and **Web Server Security**.

[![License](https://img.shields.io/badge/License-Academic-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Ubuntu%20%7C%20WSL-orange.svg)](https://ubuntu.com/)
[![Language](https://img.shields.io/badge/Language-C%2B%2B%20%7C%20Python-green.svg)](https://www.python.org/)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Lab Manuals](#lab-manuals)
  - [Lab Manual 2: Classical Cryptography Attacks](#lab-manual-2-attacking-classic-crypto-systems)
  - [Lab Manual 3: Symmetric Encryption & Hashing](#lab-manual-3-symmetric-encryption--hashing)
  - [Lab Manual 4: Programming Cryptographic Operations](#lab-manual-4-programming-symmetric--asymmetric-crypto)
  - [Lab Manual 5: SSL/TLS & Apache Security](#lab-manual-5-securing-apache-web-server)
  - [Web Manual 1: Apache Web Server Administration](#web-manual-1-apache-web-server-installation--maintenance)
- [Technologies Used](#technologies-used)
- [Learning Outcomes](#learning-outcomes)
- [Repository Structure](#repository-structure)
- [How to Use This Repository](#how-to-use-this-repository)
- [Author](#author)

---

## 🎯 Overview

This repository contains complete implementations and detailed documentation of security lab experiments conducted as part of the **CSE-478: Introduction to Computer Security** and **Information and Network Security** courses. The labs cover both theoretical and practical aspects of:

- **Classical & Modern Cryptography**
- **Symmetric & Asymmetric Encryption**
- **Cryptographic Hash Functions**
- **Digital Signatures**
- **SSL/TLS Infrastructure**
- **Web Server Security**

Each lab manual includes source code, detailed reports, screenshots, and README files explaining the implementation and findings.

---

## 📚 Lab Manuals

### Lab Manual 2: Attacking Classic Crypto Systems

**Topics Covered:**
- Caesar Cipher Brute Force Attack
- Substitution Cipher Frequency Analysis
- Pattern Recognition Techniques
- Statistical Cryptanalysis

**Key Implementations:**
- C++ program for brute-force attack on Caesar cipher (25 possible keys)
- Frequency analysis tool for breaking substitution ciphers
- Automated letter frequency counting and sorting

**Security Insights:**
- Demonstrated vulnerability of classical ciphers to computational attacks
- Proved inadequacy of small key spaces (Caesar: only 25 keys)
- Showed how frequency preservation makes substitution ciphers insecure

**Technologies:** C++, Statistical Analysis

📁 [View Lab Manual 2](LAB%20MANUAL%202/)

---

### Lab Manual 3: Symmetric Encryption & Hashing

**Topics Covered:**
- AES encryption modes (ECB, CBC, CFB, OFB)
- Block cipher behavior and error propagation
- Padding schemes (PKCS#7)
- Cryptographic hash functions (MD5, SHA-1, SHA-256)
- HMAC (Hash-based Message Authentication Code)
- Avalanche effect demonstration

**Key Experiments:**

**Task 1:** AES encryption/decryption using multiple modes  
**Task 2:** ECB vs CBC comparison using image encryption  
**Task 3:** Error propagation analysis in corrupted ciphertext  
**Task 4:** Padding requirement study for different modes  
**Task 5:** Message digest generation using MD5, SHA-1, SHA-256  
**Task 6:** HMAC generation and key sensitivity analysis  
**Task 7:** Hash randomness and avalanche effect measurement  

**Notable Results:**
- ECB mode revealed image patterns (insecure)
- CBC mode provided complete randomness
- Single bit flip in input caused >50% hash output change
- C++ program implemented to count bit differences between hashes

**Technologies:** OpenSSL, Ubuntu (WSL), HxD Hex Editor, C++

📁 [View Lab Manual 3](LAB%20MANUAL%203/)

---

### Lab Manual 4: Programming Symmetric & Asymmetric Crypto

**Topics Covered:**
- AES implementation (128-bit & 256-bit keys, ECB & CFB modes)
- RSA encryption/decryption with OAEP padding
- RSA digital signatures
- SHA-256 hashing
- Execution time analysis
- Key size vs performance tradeoff

**Key Implementations:**
- Complete Python cryptographic library wrapper
- AES symmetric encryption with multiple modes
- RSA asymmetric encryption and key generation
- Digital signature creation and verification
- Performance benchmarking tools
- Graphical analysis (Key Size vs Execution Time)

**Performance Analysis:**
- AES execution time increases linearly with key size
- RSA execution time increases exponentially
- 4096-bit RSA significantly slower than 1024-bit
- Demonstrated security vs performance tradeoff

**Technologies:** Python 3.12, PyCryptodome, Matplotlib

📁 [View Lab Manual 4](LAB%20MANUAL%204/)

---

### Lab Manual 5: Securing Apache Web Server

**Topics Covered:**
- Public Key Infrastructure (PKI)
- Certificate Authority (CA) creation
- Certificate Signing Request (CSR) generation
- SSL/TLS certificate management
- Apache HTTPS configuration
- Multi-domain secure hosting

**Key Implementations:**

**Task 1:** Custom Certificate Authority setup  
**Task 2:** Server certificate generation using OpenSSL  
**Task 3:** Apache SSL/TLS deployment  

**Secure Domains Deployed:**
- `https://example.com`
- `https://webserverlab.com`

**Challenges Resolved:**
- 1024-bit key rejection (upgraded to 2048-bit)
- Domain mismatch errors (CN configuration)
- Virtual host SSL configuration
- Certificate chain validation

**Technologies:** Ubuntu Linux, Apache2, OpenSSL, SSL/TLS

📁 [View Lab Manual 5](LAB%20MANUAL%205/)

---

### Web Manual 1: Apache Web Server Installation & Maintenance

**Topics Covered:**
- Apache web server installation and configuration
- Virtual hosts management
- Domain mapping using `/etc/hosts`
- Dynamic website hosting
- UFW firewall configuration

**Key Implementations:**

**Task 1:** Apache installation and basic configuration  
**Task 2:** Multiple virtual hosts setup  
**Task 3:** Dynamic JavaScript-based websites  

**Websites Deployed:**
- **Calculator Website** (`example.com`) - JavaScript-based calculator
- **Grade Checker Website** (`anothervhost.com`) - Dynamic grade calculation

**Concepts Demonstrated:**
- Single server hosting multiple domains
- Virtual host configuration
- Client-side dynamic content
- Apache directory structure and maintenance

**Technologies:** Apache2, HTML, JavaScript, Ubuntu Linux

📁 [View Web Manual 1](WEB%20MANUAL%201/)

---

## 🛠 Technologies Used

### Programming Languages
- **C++** - Classical cryptography attacks
- **Python 3.12** - Modern cryptographic implementations

### Cryptographic Tools
- **OpenSSL** - Encryption, hashing, certificate management
- **PyCryptodome** - Python cryptography library

### Web Technologies
- **Apache2** - Web server
- **HTML/CSS** - Frontend
- **JavaScript** - Client-side scripting
- **SSL/TLS** - Secure communications

### Development Environment
- **Ubuntu Linux (WSL)** - Primary platform
- **HxD Hex Editor** - Binary file analysis
- **Matplotlib** - Performance visualization
- **g++** - C++ compiler
- **Nano/Vim** - Text editors

---

## 🎓 Learning Outcomes

After completing these lab manuals, the following competencies were developed:

### Cryptography
✅ Understanding of classical cipher vulnerabilities  
✅ Proficiency in symmetric encryption algorithms (AES)  
✅ Knowledge of asymmetric encryption (RSA)  
✅ Digital signature implementation and verification  
✅ Hash function properties and HMAC usage  
✅ Error propagation behavior in block cipher modes  

### Security
✅ Public Key Infrastructure (PKI) concepts  
✅ Certificate Authority operations  
✅ SSL/TLS protocol implementation  
✅ Web server security hardening  
✅ Secure multi-domain hosting  

### Programming
✅ Cryptographic library integration (PyCryptodome)  
✅ Performance analysis and benchmarking  
✅ Security-focused software development  
✅ System administration and configuration  

---

## 📂 Repository Structure

```
INS-LAB/
│
├── README.md                                    # Main repository documentation
├── .gitignore
├── .gitattributes
│
├── LAB MANUAL 2/                                # Classical Cryptography Attacks
│   ├── README.md                                # Lab 2 overview
│   ├── Report.md                                # Detailed lab report
│   │
│   ├── CheckPoint1/                             # Caesar Cipher Attack
│   │   ├── CheckPoint1.cpp                      # C++ brute force implementation
│   │   ├── cp1                                  # Compiled executable
│   │   └── screenshots/                         # Execution screenshots
│   │
│   └── CheckPoint2/                             # Substitution Cipher Attack
│       ├── CheckPoint2.cpp                      # Frequency analysis program
│       ├── cipher1.txt                          # First cipher text
│       ├── cipher2.txt                          # Second cipher text
│       ├── cp2                                  # Compiled executable
│       └── screenshots/                         # Execution screenshots
│
├── LAB MANUAL 3/                                # Symmetric Encryption & Hashing
│   ├── README.md                                # Lab 3 overview
│   ├── Lab_Report.md                            # Detailed lab report
│   ├── Lab Manual - 3.pdf                       # Original lab manual
│   │
│   ├── Task-1-AES-Modes/                        # AES Encryption Modes
│   │   ├── README.md                            # Task instructions
│   │   ├── plain.txt                            # Original plaintext
│   │   ├── ecb.bin                              # ECB encrypted output
│   │   ├── ecb_decrypted.txt                    # ECB decrypted output
│   │   ├── cbc.bin                              # CBC encrypted output
│   │   ├── cbc_decrypted.txt                    # CBC decrypted output
│   │   ├── cfb.bin                              # CFB encrypted output
│   │   ├── cfb_decrypted.txt                    # CFB decrypted output
│   │   └── screenshots/                         # Command execution screenshots
│   │
│   ├── Task-2-ECB-vs-CBC/                       # Image Encryption Comparison
│   │   ├── README.md                            # Task instructions
│   │   ├── pic_original.bmp                     # Original image
│   │   ├── pic_ecb.bmp                          # ECB encrypted image
│   │   ├── pic_cbc.bmp                          # CBC encrypted image
│   │   └── screenshots/                         # Visual comparison screenshots
│   │
│   ├── Task-3-Corrupted-Ciphertext/             # Error Propagation Analysis
│   │   ├── README.md                            # Task instructions
│   │   ├── plain.txt                            # Original plaintext
│   │   ├── ecb.bin                              # ECB encrypted
│   │   ├── ecb_corrupt.bin                      # Corrupted ECB ciphertext
│   │   ├── ecb_decrypted.txt                    # Decrypted corrupted ECB
│   │   ├── cbc.bin                              # CBC encrypted
│   │   ├── cbc_corrupt.bin                      # Corrupted CBC ciphertext
│   │   ├── cbc_decrypted.txt                    # Decrypted corrupted CBC
│   │   ├── cfb.bin                              # CFB encrypted
│   │   ├── cfb_corrupt.bin                      # Corrupted CFB ciphertext
│   │   ├── cfb_decrypted.txt                    # Decrypted corrupted CFB
│   │   ├── ofb.bin                              # OFB encrypted
│   │   ├── ofb_corrupt.bin                      # Corrupted OFB ciphertext
│   │   ├── ofb_decrypted.txt                    # Decrypted corrupted OFB
│   │   └── screenshots/                         # Analysis screenshots
│   │
│   ├── Task-4-Padding/                          # Padding Schemes Study
│   │   ├── README.md                            # Task instructions
│   │   ├── small.txt                            # Small text file
│   │   ├── ecb.bin                              # ECB with padding
│   │   ├── cbc.bin                              # CBC with padding
│   │   ├── cfb.bin                              # CFB without padding
│   │   ├── ofb.bin                              # OFB without padding
│   │   └── screenshots/                         # Padding analysis screenshots
│   │
│   ├── Task-5-Message-Digest/                   # Hash Function Analysis
│   │   ├── README.md                            # Task instructions
│   │   ├── message.txt                          # Input message
│   │   ├── md5.txt                              # MD5 hash output
│   │   ├── sha1.txt                             # SHA-1 hash output
│   │   ├── sha256.txt                           # SHA-256 hash output
│   │   └── screenshots/                         # Hash generation screenshots
│   │
│   ├── Task-6-HMAC/                             # Keyed Hash Analysis
│   │   ├── README.md                            # Task instructions
│   │   ├── hmac_message.txt                     # Input message
│   │   ├── hmac_md5.txt                         # HMAC-MD5 output
│   │   ├── hmac_sha1.txt                        # HMAC-SHA1 output
│   │   ├── hmac_sha256.txt                      # HMAC-SHA256 output
│   │   └── screenshots/                         # HMAC generation screenshots
│   │
│   └── Task-7-Hash-Randomness/                  # Avalanche Effect Study
│       ├── README.md                            # Task instructions
│       ├── compare.cpp                          # Bit difference calculator
│       ├── compare                              # Compiled executable
│       ├── original.txt                         # Original text
│       ├── modified.txt                         # Modified text (1-bit diff)
│       ├── md5_h1.txt                           # MD5 of original
│       ├── md5_h2.txt                           # MD5 of modified
│       ├── sha256_h1.txt                        # SHA256 of original
│       ├── sha256_h2.txt                        # SHA256 of modified
│       └── screenshots/                         # Avalanche effect screenshots
│
├── LAB MANUAL 4/                                # Programming Crypto Operations
│   ├── README.md                                # Lab 4 overview
│   ├── Report.md                                # Detailed lab report
│   ├── Lab Manual - 4.pdf                       # Original lab manual
│   ├── main.py                                  # Main Python implementation
│   │
│   ├── inputs/                                  # Input files
│   │   └── plain.txt                            # Sample plaintext
│   │
│   ├── keys/                                    # Generated cryptographic keys
│   │   ├── aes_128.key                          # AES 128-bit key
│   │   ├── aes_192.key                          # AES 192-bit key
│   │   ├── aes_256.key                          # AES 256-bit key
│   │   ├── aes_320.key                          # AES 320-bit key
│   │   ├── rsa_private.pem                      # RSA private key
│   │   └── rsa_public.pem                       # RSA public key
│   │
│   ├── outputs/                                 # Encrypted outputs & graphs
│   │   ├── aes_encrypted.bin                    # AES encrypted file
│   │   ├── rsa_encrypted.bin                    # RSA encrypted file
│   │   ├── signature.bin                        # RSA digital signature
│   │   ├── aes_time_graph.png                   # AES performance graph
│   │   └── rsa_time_graph.png                   # RSA performance graph
│   │
│   ├── screenshots/                             # Program execution screenshots
│   ├── __pycache__/                             # Python cache files
│   └── venv/                                    # Virtual environment
│
├── LAB MANUAL 5/                                # SSL/TLS & Apache Security
│   ├── README.md                                # Lab 5 overview
│   ├── Report.md                                # Detailed lab report
│   ├── Lab Manual - 5.pdf                       # Original lab manual
│   │
│   ├── Task1_CA/                                # Certificate Authority Setup
│   │   ├── ca.key                               # CA private key
│   │   ├── ca.crt                               # CA certificate
│   │   ├── openssl.cnf                          # OpenSSL configuration
│   │   ├── index.txt                            # Certificate database
│   │   ├── serial                               # Serial number tracker
│   │   ├── screenshots/                         # CA creation screenshots
│   │   │
│   │   └── demoCA/                              # CA directory structure
│   │       ├── index.txt                        # Certificate index
│   │       ├── index.txt.old                    # Previous index
│   │       ├── index.txt.attr                   # Index attributes
│   │       ├── index.txt.attr.old               # Previous attributes
│   │       ├── serial                           # Current serial number
│   │       ├── serial.old                       # Previous serial
│   │       └── newcerts/                        # Issued certificates folder
│   │
│   ├── Task2_OpenSSL_Server/                    # Server Certificate Generation
│   │   ├── server.key                           # Server private key
│   │   ├── server.csr                           # Server certificate request
│   │   ├── server.crt                           # Signed server certificate
│   │   ├── server.pem                           # PEM format certificate
│   │   ├── webserverlab.key                     # Webserverlab private key
│   │   ├── webserverlab.csr                     # Webserverlab CSR
│   │   ├── webserverlab.crt                     # Webserverlab certificate
│   │   │
│   │   ├── Checkpoint1/                         # First checkpoint
│   │   │   └── screenshots/                     # Process screenshots
│   │   │
│   │   └── CheckPoint2/                         # Second checkpoint
│   │       ├── webserver.key                    # Alternative server key
│   │       ├── webserver.csr                    # Alternative server CSR
│   │       ├── webserver.crt                    # Alternative server cert
│   │       ├── webserver.pem                    # PEM format
│   │       └── screenshots/                     # Process screenshots
│   │
│   └── Task3_Apache_SSL/                        # Apache HTTPS Configuration
│       ├── example.com/                         # First secure domain
│       │   └── screenshots/                     # HTTPS testing screenshots
│       │
│       └── webserverlab.com/                    # Second secure domain
│           ├── webserverlab.key                 # Domain private key
│           └── screenshots/                     # HTTPS testing screenshots
│
└── WEB MANUAL 1/                                # Apache Web Server Admin
    ├── README.md                                # Web Lab 1 overview
    ├── Report.md                                # Detailed lab report
    ├── Web Lab Manual - 1.pdf                   # Original lab manual
    │
    ├── Task-1-Apache-Web-Server/                # Apache Installation
    │   ├── Report.md                            # Task report
    │   └── screenshots/                         # Installation screenshots
    │
    ├── Task-2-Virtual-Hosts/                    # Virtual Hosts Configuration
    │   ├── Report.md                            # Task report
    │   │
    │   ├── example.com/                         # First virtual host
    │   │   └── screenshots/                     # Configuration screenshots
    │   │
    │   ├── anothervhost.com/                    # Second virtual host
    │   │   └── screenshots/                     # Configuration screenshots
    │   │
    │   └── webserverlab.com/                    # Third virtual host
    │       └── screenshots/                     # Configuration screenshots
    │
    └── Task-3-Dynamic-Websites/                 # Dynamic Content Hosting
        ├── Report.md                            # Task report
        │
        ├── calculator/                          # Calculator website
        │   └── screenshots/                     # Website screenshots
        │
        └── grade-checker/                       # Grade checker website
            └── screenshots/                     # Website screenshots
```

---

## 🚀 How to Use This Repository

### Prerequisites

**For C++ Labs:**
```bash
sudo apt update
sudo apt install g++ build-essential
```

**For Python Labs:**
```bash
sudo apt install python3 python3-pip python3-venv
pip install pycryptodome matplotlib
```

**For OpenSSL Labs:**
```bash
sudo apt install openssl
```

**For Apache Labs:**
```bash
sudo apt install apache2
sudo ufw allow 'Apache Full'
```

---

### Running the Labs

#### Lab Manual 2 (C++ Cryptanalysis)
```bash
cd "LAB MANUAL 2/CheckPoint1"
g++ CheckPoint1.cpp -o cp1
./cp1
```

#### Lab Manual 3 (OpenSSL Operations)
```bash
cd "LAB MANUAL 3/Task-1-AES-Modes"
# Follow commands in README.md
openssl enc -aes-128-ecb -e -in plain.txt -out ecb.bin -K [key]
```

#### Lab Manual 4 (Python Crypto)
```bash
cd "LAB MANUAL 4"
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install pycryptodome matplotlib
python3 main.py
```

#### Lab Manual 5 & Web Manual 1 (Apache)
```bash
# Follow step-by-step instructions in respective README.md files
sudo systemctl start apache2
sudo a2ensite example.com.conf
sudo systemctl restart apache2
```

---

## 📊 Key Findings Summary

| Lab | Main Discovery | Security Implication |
|-----|---------------|---------------------|
| **Lab 2** | Caesar cipher broken in <1s | Classical ciphers are obsolete |
| **Lab 3** | ECB reveals patterns in encrypted images | Never use ECB mode for real data |
| **Lab 3** | Single bit flip changes 50%+ of hash | Confirms avalanche effect |
| **Lab 4** | RSA 4096-bit is 10x slower than 1024-bit | Performance vs security tradeoff |
| **Lab 5** | 1024-bit keys rejected by modern OpenSSL | Industry moving to 2048-bit minimum |

---

## 📝 Documentation

Each lab manual contains:
- **README.md** - Quick reference and commands
- **Report.md** - Detailed analysis and observations
- **screenshots/** - Visual evidence of execution
- Source code with inline comments

---

## ⚠️ Important Notes

- All experiments conducted in isolated Ubuntu/WSL environment
- Certificates and keys are for educational purposes only
- Do not use these implementations in production systems
- Always follow current security best practices and standards

---

## 🔗 References

### Books
- William Stallings, *Cryptography and Network Security*
- Bruce Schneier, *Applied Cryptography*

### Documentation
- [OpenSSL Documentation](https://www.openssl.org/docs/)
- [PyCryptodome Documentation](https://pycryptodome.readthedocs.io/)
- [Apache HTTP Server Documentation](https://httpd.apache.org/docs/)

### Standards
- NIST Special Publications on Cryptography
- RFC 5280 (X.509 Certificate Standards)
- RFC 2818 (HTTP Over TLS)

---

## 👤 Author

**Emran Ahmed**  
*BSc in Software Engineering*
**Shahjalal University of Science and Technology**

**Course:** Information and Network Security Lab
**Academic Year:** 2025

---

## 📄 License

This project is licensed for **Academic Use Only**. 

All code and documentation are provided as-is for educational purposes. Not intended for production use.

---

## 🤝 Contributing

This is an academic project repository. If you find any issues or have suggestions:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request with detailed description

---

## 📧 Contact

For questions or discussions about the implementations:
- Open an issue in this repository
- Contact through university email

---

## ⭐ Acknowledgments

- Course instructors for lab manual design
- OpenSSL and PyCryptodome communities
- Apache Foundation
- Ubuntu/Canonical documentation team

---

<div align="center">

**🔐 Security is not a product, but a process. 🔐**

*Last Updated: March 2026*

</div>
