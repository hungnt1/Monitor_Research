
'''
Author: hungnt1
License: GPLv3
'''
from keystoneauth1.identity import v3 
from keystoneauth1 import loading
from keystoneauth1 import session
from keystoneclient.v3 import client as keystone
from novaclient import client as nova_auth
from novaclient.v2.servers import ServerManager
from neutronclient.v2_0 import client as neutron_auth
from neutronclient.neutron.v2_0 import network
import json
import requests
import datetime

auth_url = 'http://192.168.100.32:5000/v3'
username = 'monitor'
user_domain_name = 'Default'
project_name = 'monitor'
project_domain_name = 'Default'
password = 'monitor123'

auth = v3.Password(auth_url=auth_url,  username=username, password=password, user_domain_name=user_domain_name, project_name=project_name, project_domain_name=project_domain_name)
sess = session.Session(auth=auth)
keystone_auth = keystone.Client(session=sess)
nova_auth.Client(2, session=sess)
neutron_auth.Client(session=sess)
netw = network.ListExternalNetwork()

## map service_name vao service_id
# service_id_name_map = {}
# for service in keystone_auth.services.list():
#     service_dict = service.to_dict()
#     service_id_name_map[service_dict['id']] = service_dict['name']

## map service_name vao service_endpoint_url
# service_endpoint_map = {}
# for endpoint in keystone_auth.endpoints.list():
#     endpoint_dict = endpoint.to_dict()
#     if endpoint_dict['interface'] != 'public':
#         continue
#     service_id = endpoint_dict['service_id']
#     service_name = service_id_name_map[service_id]
#     service_endpoint_map[service_name] = endpoint_dict['url']
#     response = requests.get(endpoint_dict['url'])
#     print(response.status_code)

# print(service_endpoint_map) 
# ServerManager.create(name="zabbix-test", image="cirros", flavor="m1.monitor", nics="")
