import requests
import json
import unittest

def get_github(id):

    urlRepo = f'https://api.github.com/users/{id}/repos'
    urlCommit = f'https://api.github.com/repos/{id}/'
    returnString = ""

    try:
        response = requests.get(urlRepo)
        response.raise_for_status()
        res = response.json()
        for repo in res:
            try:
                repoResponse = requests.get(urlCommit + repo['name'] + '/commits')
                repoResponse.raise_for_status()
                repoRes = repoResponse.json()
                returnLine = 'Repo: ' + repo['name'] + ' Number of commits: ' + str(len(repoRes))
                returnString += returnLine + '\n'
            except requests.exceptions.HTTPError as err:
                return err
            except json.JSONDecodeError as err:
                return err
        return returnString
    except requests.exceptions.HTTPError as err:
        return err
    except json.JSONDecodeError:
        return err

class TestGetGit(unittest.TestCase):
    def test_get_github(self):
        results = get_github('richkempinski')
        self.assertEqual(results, 'Repo: csp Number of commits: 2\n'
                                  'Repo: hellogitworld Number of commits: 30\n'
                                  'Repo: helloworld Number of commits: 6\n'
                                  'Repo: Mocks Number of commits: 10\n'
                                  'Repo: Project1 Number of commits: 2\n'
                                  'Repo: richkempinski.github.io Number of commits: 9\n'
                                  'Repo: threads-of-life Number of commits: 1\n'
                                  'Repo: try_nbdev Number of commits: 2\n'
                                  'Repo: try_nbdev2 Number of commits: 5\n')

    def test_get_error(self):
        results = get_github('bad_user')
        print(results)

if __name__ == '__main__':
    unittest.main()


