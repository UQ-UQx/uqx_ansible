UQx Configuration Script
===========

Ansible scripts for UQx

Usage
---------------------

Launch NECTAR VM (optional)
---------------------
 - Adapted from https://github.com/eResearchSA/nectar-ansible
 - Login to the Nectar Dashboard (https://dashboard.rc.nectar.org.au)
 - Choose the correct [PROJECT_NAME]
 - Create a keypair in "Access and Security" and note the [KEY_NAME]
 - Download the key-pair and add it to your ~/.ssh/
 - Go to "Settings" (top right)
 - Click "Reset Password"
 - Copy down the new [GENERATED_PASSWORD]
 - Go to "Access and Security"
 - Go to the "API Access"
 - Click "Download OpenStack RC File"
 - Run the script
 ```
 source ./[PROJECT_NAME]-openrc.sh
 ```
 - Enter the API [GENERATED_PASSWORD]
 - Run the nectar script
 ```
 python startvm.py -k [KEY_NAME]
 ```
(note that KEY_NAME is not a path to a key)

Configure VM with Ansible
---------------------
 - Edit "vm_list" to contain your machine name/s
 - Run script
```bash
ansible-playbook -i vm_list --private-key=[SSH_PRIVATE_KEY] -u [SSH_USERNAME] uqx_ansible/site.yml
```
 - Bugs
 	- The first run will fail, you need to edit /etc/nginx/sites-enabled/default and delete the line in the middle of the comments on line 53, "root /var/www/html/dashboard;"
 	- The server requires a domain name so that api.[HOSTNAME] works
