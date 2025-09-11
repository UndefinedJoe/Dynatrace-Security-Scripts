import requests
import json
import os
import sys

DT_API_TOKEN = os.environ.get('DT_API_TOKEN')
DT_ENV_URL = os.environ.get('DT_ENV_URL')

# Validate that required environment variables are set
if not DT_API_TOKEN:
    print("Error: DT_API_TOKEN environment variable is not set")
    print("Please set it using: export DT_API_TOKEN='your-token-here'")
    sys.exit(1)

if not DT_ENV_URL:
    print("Error: DT_ENV_URL environment variable is not set")
    print("Please set it using: export DT_ENV_URL='https://your-environment.live.dynatrace.com'")
    sys.exit(1)

HEADERS = {
    'Authorization': f'Api-Token {DT_API_TOKEN}',
    'Content-Type': 'application/json'
}

def get_hosts():
    url = f'{DT_ENV_URL}/api/v2/entities'
    params = {
        'pageSize': 100,
        'entitySelector': 'type("HOST")',
        'fields': '+properties.monitoringMode'
    }
    hosts = []
    
    while True:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json()
        
        for host in data.get('entities', []):
            # The monitoring mode is in the properties field
            properties = host.get('properties', {})
            mode = properties.get('monitoringMode')
            if mode in ['DISCOVERY']:
                hosts.append(host['entityId'])
        
        # Check for next page
        next_key = data.get('nextPageKey')
        if next_key:
            # Clear other params when using nextPageKey
            params = {'nextPageKey': next_key}
        else:
            break
    
    return hosts

def enable_code_module_injection(host_id):
    url = f'{DT_ENV_URL}/api/v2/settings/objects'
    payload = [{
        "schemaId": "builtin:host.monitoring.advanced",
        "scope": host_id,
        "value": {
            "codeModuleInjection": True,
            "processAgentInjection": True
        }
    }]
    response = requests.post(url, headers=HEADERS, data=json.dumps(payload))
    if response.status_code == 200 or response.status_code == 201:
        print(f'Enabled CodeModule injection on host: {host_id}')
    else:
        print(f'Failed to update host {host_id}: {response.text}')

def main():
    print(f"Using Dynatrace environment: {DT_ENV_URL}")
    print(f"API Token: {'*' * 10}{DT_API_TOKEN[-4:] if len(DT_API_TOKEN) > 4 else '****'}")
    print("-" * 50)
    
    hosts = get_hosts()
    print(f'Found {len(hosts)} hosts in DISCOVERY mode.')
    
    for host_id in hosts:
        enable_code_module_injection(host_id)

if __name__ == '__main__':
    main()
