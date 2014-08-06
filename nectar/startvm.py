#!/usr/bin/python

# Graciously adapted from https://github.com/eResearchSA/nectar-ansible/

# TODO
# - use a service for allocating hostnames

import sys, os, time, socket, argparse, random, urllib2

from novaclient.v1_1 import client

#default_image = urllib2.urlopen("https://swift.rc.nectar.org.au:8888/v1/AUTH_6f3b184bcf194672a55d258620e732db/deploy/nectar-zfs-image").read().strip()
default_image = '198869c6-d8f5-4972-8085-e2a5dc1e139d'
default_setup_script = None
default_security_group = "default"
default_auth_url = "https://keystone.rc.nectar.org.au:5000/v2.0/"
default_zone = 'QRIScloud'
default_size = 'm1.large'

def progress(s):
  sys.stdout.write(s)
  sys.stdout.flush()

def main(image, zone, auth_url, size, key, security_group, setup_script):
  name = random.sample(open("vmnames.txt").read().split(), 1)[0]
  user_data = None
  if setup_script is not None:
    user_data = open(setup_script).read()
  nectar = client.Client(username = os.environ["OS_USERNAME"], api_key = os.environ["OS_PASSWORD"], project_id = os.environ["OS_TENANT_NAME"], auth_url = auth_url)
  flavor = nectar.flavors.find(name = size)
  vm = nectar.servers.create(availability_zone = zone, name = name, image = image, flavor = flavor, userdata = user_data, security_groups = [security_group], key_name = key)
  progress("Waiting for VM (" + name + ") to activate ")
  while not vm.status == 'ACTIVE':
    progress(".")
    time.sleep(2)
    vm.get()
  ip = vm.networks.values()[0][0]
  rip = socket.gethostbyaddr(ip)[0]
  print "", rip

if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    description = "Fire up a VM on NeCTAR (default image: " + default_image + ")",
    epilog = "Required OpenStack environment variables: OS_USERNAME, OS_PASSWORD, OS_TENANT_NAME.")
  parser.add_argument("-z", "--zone", help = "Zone, e.g. melbourne (default none)", default = default_zone)
  parser.add_argument("-s", "--size", help = "VM flavour/size, e.g. m1.small", default = default_size)
  parser.add_argument("-i", "--image", help = "Image (default " + default_image + ")", default = default_image)
  parser.add_argument("-k", "--key", help = "Key name", required = True)
  parser.add_argument("-a", "--auth-url", help = "OpenStack Auth URL (default " + default_auth_url + ")", default = default_auth_url)
  parser.add_argument("-g", "--security-group", help = "Security group (default " + default_security_group + ")", default = default_security_group)
  parser.add_argument("-S", "--setup-script", help = "Setup script (default none)", default = default_setup_script)

  args = parser.parse_args()

  main(args.image, args.zone, args.auth_url, args.size, args.key, args.security_group, args.setup_script)