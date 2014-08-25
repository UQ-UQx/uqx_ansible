#!/bin/sh
## setup_users
## this is where the script goes to setup your users

# /usr/sbin/useradd -u 500 -c "John Doe" -m -s /bin/bash -p 'hashedpass' username

## echo Adding users to /etc/group
# sed -i.backup "/wheel/s/$/,username,username2/" /etc/group
# sed -i.backup "/sudo/s/$/,username,username2/" /etc/group
# sed -i.backup "/apache/s/$/,username,username2/" /etc/group