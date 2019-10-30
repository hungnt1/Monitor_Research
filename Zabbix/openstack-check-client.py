
#! /usr/bin/python

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
from glanceclient.v2 import client as glance_client
from novaclient import client as nova_client
from neutronclient.v2_0  import client as neutron_client
from novaclient.exceptions import NotFound
from keystoneauth1.exceptions.http import Unauthorized
import random
import json
import time
import sys
import os

## authencation

auth = v3.Password(auth_url="http://192.168.100.32:5000/v3", username="monitor",
                   password="monitor123", project_name="monitor",
                   user_domain_id="default", project_domain_id="default")
sess = session.Session(auth=auth)
keystone = client.Client(session=sess)
glance = glance_client.Client(session=sess)
nova = nova_client.Client(2, session=sess)
neutron = neutron_client.Client(session=sess)

## get ID image cirros
for image in glance.images.list():
    if image["name"] == "cirros":
        image_cirros_id  = image["id"]
        break

## get ID flavor
for flavor in nova.flavors.list():
    if flavor.to_dict()["name"] == "m1.monitor":
        flavor_monitor_id = flavor.to_dict()["id"]
        break


name = "zabbix_test_vm"
image = image_cirros_id
flavor = flavor_monitor_id

## delete old VM
try:
    while True:
        server = nova.servers.find(name=name)
        server.delete()
except NotFound:
    pass

## get network list
network_list = []
for network_dict in neutron.list_networks()["networks"]:
    network_list.append(network_dict["id"])

## create vm
nova.servers.create(name, image, flavor, meta=None, files=None, reservation_id=True, min_count=None, max_count=None, security_groups=None, userdata=None, key_name=None, availability_zone=None, block_device_mapping=None, block_device_mapping_v2=None,  nics=[{"net-id": random.choice(network_list)}] , scheduler_hints=None, config_drive=None, disk_config=None, admin_pass=None, access_ip_v4=None, access_ip_v6=None, trusted_image_certificates=None, host=None, hypervisor_hostname=None)


## check status vm
while True:
    if len(nova.servers.list(search_opts={'status': 'BUILD'})) == 0:
        break

## get IPADDR VM
for instance in nova.servers.list(search_opts={'status': 'ACTIVE'}):
    for i in instance.to_dict()["addresses"].values():
        vm_addr = i[0]["addr"]
        response = os.system('ping -c4 ' + vm_addr +" >/dev/null")
        if response == 0:
            print("UP")


