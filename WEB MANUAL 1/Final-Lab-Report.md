# WEB LAB MANUAL 1: Apache Web Server Installation & Maintenance

## Course: Information and Network Security
## Environment: Ubuntu Linux

---

# Objective

To install, configure, administer, and maintain an Apache Web Server and host multiple websites using Virtual Hosts.

---

# Task 1: Setting Up Apache Web Server

## Step 1: Install Apache

Command used:

sudo apt update
sudo apt install apache2


Apache service status checked using:

sudo systemctl status apache2


Result: Apache service was running successfully.

## Step 2: Firewall Configuration

Command:

sudo ufw allow 'Apache'
sudo ufw status


Result: Port 80 (HTTP) allowed.

## Step 3: Testing Server

Accessed:
- http://localhost
- http://127.0.0.1

Result: Apache Default Page displayed successfully.

## Step 4: Domain Mapping

Edited:
/etc/hosts


Added:
127.0.0.1 webserverlab.com


Successfully accessed:
http://webserverlab.com


---

# Task 2: Setting Up Virtual Hosts

## Virtual Host 1: example.com

Created directory:
/var/www/example.com/html


Created index.html file.

Created configuration:
/etc/apache2/sites-available/example.com.conf


Enabled site:
sudo a2ensite example.com.conf
sudo systemctl restart apache2


Result: example.com working successfully.

---

## Virtual Host 2: anothervhost.com

Created directory:
/var/www/anothervhost.com/html


Created configuration:
/etc/apache2/sites-available/anothervhost.com.conf


Enabled site and restarted Apache.

Result: anothervhost.com working successfully.

---

# Explanation for Checkpoint 3

When default configuration (000-default.conf) is disabled, Apache serves only enabled virtual hosts.

If a domain does not match any ServerName, Apache cannot serve content for it.

That is why webserverlab.com may not work if it is not configured as a virtual host.

---

# Task 3: Hosting Dynamic Websites

## Website 1: Calculator (example.com)

Features:
- Takes two numbers
- Adds them using JavaScript
- Displays result dynamically

Technology Used:
- HTML
- JavaScript (Client-side)

---

## Website 2: Grade Checker (anothervhost.com)

Features:
- Takes marks input
- Calculates grade using JavaScript
- Displays result dynamically

Technology Used:
- HTML
- JavaScript

---

# Important Apache Commands Used

| Command | Purpose |
|---------|---------|
| sudo systemctl start apache2 | Start server |
| sudo systemctl stop apache2 | Stop server |
| sudo systemctl restart apache2 | Restart server |
| sudo a2ensite | Enable virtual host |
| sudo a2dissite | Disable virtual host |
| sudo apache2ctl configtest | Check configuration |

---

# Important Apache Directories

| Directory | Purpose |
|-----------|----------|
| /var/www/ | Website root directory |
| /etc/apache2/ | Configuration files |
| sites-available | Virtual host configs |
| sites-enabled | Enabled virtual hosts |
| /var/log/apache2/ | Server logs |

---

# Conclusion

In this lab, I successfully:

- Installed Apache Web Server
- Configured firewall settings
- Hosted multiple websites
- Configured virtual hosts
- Deployed dynamic websites
- Learned Apache maintenance commands

The lab helped me understand practical web server configuration and hosting multiple domains in a single server.

---
