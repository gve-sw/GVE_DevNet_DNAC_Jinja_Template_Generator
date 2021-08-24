# Copyright (c) 2021 Cisco and/or its affiliates.

# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.0 (the "License"). You may obtain a copy of the
# License at

#                https://developer.cisco.com/docs/licenses

# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

import requests
import json
import csv
from datetime import datetime
from requests.auth import HTTPBasicAuth
from config import PI, USER, PASSWORD
import pprint
from netmiko import ConnectHandler
from dnacentersdk import api
import sys

base_url = 'https://' + PI + '/webacs/api/v4/data'

option = input("Query by device ip address (I) or by device hostname (H) : ")
if str(option).lower() == 'i':
    value = input("Enter device ip address : ")
    url = base_url + '/BulkSanitizedConfigArchives.json?deviceIpAddress=' + str(value)
elif str(option).lower() == 'h':
    value = input("Enter device hostname : ")
    url = base_url + '/BulkSanitizedConfigArchives.json?deviceName=' + str(value)
else:
    print("wrong input")
    sys.exit()

payload = {}
headers = {
}

response = requests.request('GET', url,auth=HTTPBasicAuth(USER, PASSWORD),verify=False, headers=headers, data = payload)

response = json.loads(response.text)

file = response['queryResponse']["entityId"][0]
file_request = requests.request('GET', file["@url"]+".json",auth=HTTPBasicAuth(USER, PASSWORD),verify=False, headers=headers, data = payload)
file_request = json.loads(file_request.text)
files = file_request['queryResponse']['entity'][0]['bulkSanitizedConfigArchivesDTO']['files']['file']
for x in files :
    if x['fileState'] == 'STARTUPCONFIG':
        with open('config.txt', 'w') as f:
            f.write(x['data'])