import requests
import json
import os
import subprocess
import sys
version = "2"

global_version = int(requests.get('https://raw.githubusercontent.com/ShadowStorm1218/Main/main/version.txt').text)

#Check if were on current version
if int(version) == global_version:
    print("No Update Avalible")
    pass
else:
    print("Incompatible Version, Auto Updating.")
    url = 'https://raw.githubusercontent.com/ShadowStorm1218/Main/main/updated%20version.py'
    filename = 'main.py'

    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
            os.remove(__file__)
    else:
        print(f'Error updating code: HTTP status code {response.status_code}')







print("End Of Code")
