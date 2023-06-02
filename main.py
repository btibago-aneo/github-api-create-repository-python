import sys
import argparse
from dotenv import dotenv_values

from index import create_repository, create_github_pages

# Loading environment variable file into the script
env_variables = dotenv_values(".env")


if __name__ == "__main__":
    token = env_variables["GITHUB_TOKEN"]
    parser = argparse.ArgumentParser(description='Create a GitHub repository')
    parser.add_argument('repository_name', type=str, help='Name of the repository')
    #parser.add_argument('repository_description', type=str, help='Description of the repository')
    parser.add_argument('username', type=str, help='Your username')

    args = parser.parse_args()
    if(len(sys.argv) <3 ):
        print('You must enter 3 arguments in the command line interface')
    #create_repository(repository_name=args.repository_name, repository_description=args.repository_description, token=token)
    create_github_pages(username=args.username, repository_name=args.repository_name, token=token)
