# WEB LAB MANUAL 1: Apache Web Server Installation & Maintenance

## Course
Information and Network Security (INS)

## Objective
To install, configure, and maintain an Apache Web Server in Ubuntu Linux and host multiple websites using Virtual Hosts.

---

## Technologies Used

- Ubuntu Linux
- Apache Web Server
- HTML
- JavaScript
- Virtual Hosts
- UFW Firewall

---

## Lab Tasks Overview

### Task 1: Apache Installation
- Installed Apache web server
- Configured firewall
- Verified server using localhost
- Mapped custom domain using /etc/hosts

### Task 2: Virtual Hosts Configuration
- Created example.com virtual host
- Created anothervhost.com virtual host
- Disabled default configuration
- Tested multiple domain hosting on same server

### Task 3: Hosting Dynamic Websites
- Created Calculator website using JavaScript
- Created Grade Checker website using JavaScript
- Hosted both in separate virtual hosts

---

## Virtual Hosts Created

| Domain Name | Type | Description |
|------------|------|-------------|
| example.com | Dynamic | Calculator Website |
| anothervhost.com | Dynamic | Grade Checker Website |

---

## Apache Important Directories

- /var/www/ → Web root directory
- /etc/apache2/ → Apache configuration directory
- /etc/apache2/sites-available/ → Virtual host configs
- /etc/apache2/sites-enabled/ → Enabled sites
- /var/log/apache2/ → Server logs

---

## Learning Outcome

After completing this lab, I learned:

- How Apache works internally
- How to configure virtual hosts
- How multiple websites run on one server
- How to deploy dynamic websites
- Basic Apache maintenance commands

---

## Author
Emran Ahmed  
