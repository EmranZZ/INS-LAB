# Lab 5: Securing Apache Web Server
Course: Information & Network Security  
Environment: Ubuntu Linux  
Student Name: __________________  
Student ID: __________________  

---

# Objective

The objective of this lab was to:
- Create a local Certificate Authority (CA)
- Generate SSL certificates using OpenSSL
- Deploy HTTPS on Apache Web Server
- Configure multiple secure virtual hosts
- Understand SSL/TLS security mechanisms

---

# Task 1: Create Certificate Authority (CA)

## Steps Performed:

1. Created CA private key (2048-bit RSA)
2. Created self-signed root certificate
3. Created CA directory structure (demoCA)
   - certs/
   - crl/
   - newcerts/
   - private/
   - index.txt
   - serial

## Commands Used:
openssl genrsa -des3 -out ca.key 2048
openssl req -new -x509 -days 365 -key ca.key -out ca.crt


## Result:
CA successfully created to sign server certificates.

---

# Task 2: Generate Server Certificate (OpenSSL)

## CheckPoint 1 – example.com

### Steps:
1. Generated server private key (2048-bit)
2. Created CSR
3. Signed certificate using CA

### Commands:
openssl genrsa -des3 -out server.key 2048
openssl req -new -key server.key -out server.csr
openssl ca -in server.csr -out server.crt


### Result:
Certificate successfully generated for example.com.

---

## CheckPoint 2 – webserverlab.com

### Steps:
1. Generated new private key
2. Created CSR with CN = webserverlab.com
3. Signed using same CA

### Result:
Second secure certificate created successfully.

---

# Task 3: Deploy HTTPS on Apache

## Steps:

1. Copied certificates to:
   - /etc/ssl/certs/
   - /etc/ssl/private/

2. Edited Apache Virtual Host configuration:
<VirtualHost *:443>
ServerName example.com
DocumentRoot /var/www/html
SSLEngine on
SSLCertificateFile /etc/ssl/certs/server.crt
SSLCertificateKeyFile /etc/ssl/private/server.key
</VirtualHost>


3. Enabled SSL module:
sudo a2enmod ssl

4. Enabled site:
sudo a2ensite example.com.conf

5. Restarted Apache:
sudo systemctl restart apache2

6. Updated /etc/hosts:
127.0.0.1 example.com
127.0.0.1 webserverlab.com


---

# Observations

- Initially faced "key too small" error (1024-bit rejected)
- Regenerated 2048-bit key to fix security issue
- Faced domain mismatch error
- Fixed using correct Common Name (CN) and /etc/hosts mapping
- Successfully deployed two HTTPS virtual hosts

---

# Conclusion

In this lab, we successfully:

- Implemented Public Key Infrastructure (PKI)
- Generated and signed SSL certificates
- Secured Apache using HTTPS
- Hosted multiple secure domains

This lab provided practical understanding of SSL/TLS configuration and web server security.
