# Task 1: Apache Web Server Installation

## Objective
To install and configure Apache Web Server in Ubuntu Linux.

---

## Steps Performed

1. Updated package repository:
   sudo apt update

2. Installed Apache:
   sudo apt install apache2

3. Checked service status:
   sudo systemctl status apache2

4. Allowed firewall access:
   sudo ufw allow 'Apache'

5. Tested server in browser:
   http://localhost
   http://127.0.0.1

6. Mapped custom domain in /etc/hosts:
   127.0.0.1 webserverlab.com

---

## Result

- Apache installed successfully.
- Service running properly.
- Default Apache page displayed.
- Custom domain working locally.


---

## Learning Outcome

- Learned how to install Apache
- Understood firewall configuration
- Learned how domain mapping works
