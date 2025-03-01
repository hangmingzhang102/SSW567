import requests
import json

def get_github(id):

    urlRepo = f'https://api.github.com/users/{id}/repos'
    urlCommit = f'https://api.github.com/repos/{id}/'

    try:
        response = requests.get(urlRepo)
        response.raise_for_status()
        res = response.json()
        for repo in res:
            try:
                repoResponse = requests.get(urlCommit + repo['name'] + '/commits')
                repoResponse.raise_for_status()
                repoRes = repoResponse.json()
                print('Repo: ' + repo['name'] + ' Number of commits: ' + str(len(repoRes)))
            except requests.exceptions.HTTPError as err:
                print(err)
            except json.JSONDecodeError:
                print("bad json")
        return None
    except requests.exceptions.HTTPError as err:
        print(err)
        return None
    except json.JSONDecodeError:
        print("bad json")
        return None


if __name__ == '__main__':

    get_github('richkempinski')


