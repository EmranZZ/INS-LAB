# Task 2: Setting Up Virtual Hosts

## Objective
To configure multiple virtual hosts in a single Apache web server.

---

## Virtual Host 1: example.com

- Created directory: /var/www/example.com/html
- Created index.html file
- Created config file in:
  /etc/apache2/sites-available/example.com.conf
- Enabled site using:
  sudo a2ensite example.com.conf
- Restarted Apache server

Result: example.com working successfully.

---

## Virtual Host 2: anothervhost.com

- Created directory: /var/www/anothervhost.com/html
- Created index.html file
- Created config file in:
  /etc/apache2/sites-available/anothervhost.com.conf
- Enabled site
- Restarted Apache

Result: anothervhost.com working successfully.

---

## Checkpoint 3 Explanation

When default site (000-default.conf) is disabled:

- Apache only serves enabled virtual hosts.
- If a domain is not configured, it will not load.
- Apache matches domain using ServerName.


---

## Learning Outcome

- Learned how multiple websites run on one server
- Understood Apache configuration structure
- Learned a2ensite and a2dissite commands
