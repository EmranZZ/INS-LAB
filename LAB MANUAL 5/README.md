# 🔐 Lab 5: Securing Apache Web Server

This project demonstrates securing Apache Web Server using SSL/TLS with a locally created Certificate Authority (CA).

---

# 📂 Project Structure

LAB MANUAL 5/
│
├── Task1_CA/
├── Task2_OpenSSL_Server/
├── Task3_Apache_SSL/
│   ├── CheckPoint1_example.com/
│   ├── CheckPoint2_webserverlab.com/
│
├── LAB_REPORT.md
└── README.md

---

# 🚀 Features Implemented

✔ Created custom Certificate Authority  
✔ Generated 2048-bit RSA keys  
✔ Created CSR and signed certificates  
✔ Configured Apache HTTPS  
✔ Hosted multiple secure domains  
✔ Resolved SSL domain mismatch issues  

---

# 🌍 Secure Domains

- https://example.com
- https://webserverlab.com

---

# 🔧 Technologies Used

- Ubuntu Linux
- Apache2
- OpenSSL
- SSL/TLS
- Virtual Hosts

---

# ⚠ Important Notes

- 1024-bit keys are rejected by modern OpenSSL
- Domain name must match Certificate Common Name (CN)
- /etc/hosts must map domain to localhost for local testing

---

# 🎯 Learning Outcomes

After completing this lab, the following concepts were understood:

- Public Key Infrastructure (PKI)
- Certificate Authority (CA)
- CSR generation
- Apache SSL configuration
- HTTPS deployment
- Multi-domain secure hosting

---

