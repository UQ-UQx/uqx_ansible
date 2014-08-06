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
 - Go to "Settings" (top right)
 - Click "Reset Password"
 - Copy down the new [GENERATED_PASSWORD]
 - Go to "Access and Security"
 - Go to the "API Access"
 - Click "Download OpenStack RC File"
 - Run the script
 ```bash
 source ./[PROJECT_NAME]-openrc.sh
 ```
 - Enter the API [GENERATED_PASSWORD]
 - Run the nectar script
 ```bash
 python startvm.py -k [KEY_NAME]
 ```

Configure VM with Ansible
---------------------
