import requests
import json


"""
    repository_name(str) : the name of the repository
    username(str): your username
    _check if the repository exist_
"""
def check_if_repository_exist(username, repository_name) -> bool:
    url = f"https://api.github.com/repos/{username}/{repository_name}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Repository exists!")
        return True
    elif response.status_code == 404:
        print("Repository does not exist!")
        return False
    else:
        print(f"Failed to check repository existence: {response.text}")
        return False


"""
    repository_name(str) : the name of the repository
    repository_description(str): the description of your repository
    token(str): Your personnal github token to authenticate in github. It is recommended to pass it as an environment variable
    _create a github repository via the api_
"""
def create_repository(repository_name, repository_description, token) -> None:
   
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


"""
    repository_name(str) : the name of the repository
    username(str): your username
    token(str): Your personnal github token to authenticate in github. It is recommended to pass it as an environment variable
    _create a github page via the api_
"""
def create_github_pages(username, repository_name, token) -> None:
    
    if(check_if_repository_exist(username=username, repository_name=repository_name) == False):
        exit(0)

    url = f"https://api.github.com/repos/{username}/{repository_name}/pages"
    headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.switcheroo-preview+json",
    'X-GitHub-Api-Version': '2022-11-28'
    }
    payload = {
    "source": {
        "branch": "main",
        "path": "/"
        }
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print("GitHub Page created successfully!")
    else:
        print(f"Failed to create GitHub Page: {response.text}")
