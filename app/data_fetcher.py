import requests

API_KEY = ' '
BASE_URL = ' '

def fetch_services():
    headers = {
        'Authorization': f'Token token={API_KEY}',
        'Accept': 'application/vnd.pagerduty+json;version=2'
    }
    response = requests.get(f'{BASE_URL}/services', headers=headers)
    return response.json()
