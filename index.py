import requests
import json
from dotenv import dotenv_values

# Loading environment variable file into the script
env_variables = dotenv_values(".env")

username = 'btibago-aneo'
token = env_variables["GITHUB_TOKEN"]
repository_name = 'repository-test'
repository_description = 'this is a test to create a repository'

payload = {
    'name': repository_name,
    'description': repository_description,
    'private': False
}
payload = json.dumps(payload)

url = f"https://api.github.com/user/repos"
headers = {
    'Content-Type': 'application/json',
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.post(url, headers=headers, data=payload)

if response.status_code == 201:
    print('Repository created successfully')
else:
    print(f'Error creating repository: {response.text}')

