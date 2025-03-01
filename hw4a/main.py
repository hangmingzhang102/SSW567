from unittest import mock
import requests
import json
import unittest

from requests.cookies import MockResponse


def get_github(id):

    urlRepo = f'https://api.github.com/users/{id}/repos'
    urlCommit = f'https://api.github.com/repos/{id}/'
    returnString = ""

    try:
        response = requests.get(urlRepo)
        print(response)
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
    @mock.patch('requests.get')
    def test_get_github(self, mockedReq):
        data = {
            "name": "test1",
            "commits": 2,
        }
        jsonData = json.dumps(data)
        mockedReq.return_value = MockResponse('[{"sha":1},{"sha":2}…{"sha":8}]')
        results = get_github('richkempinski')
        self.assertEqual(results, 'Repo: test1 Number of commits: 2\n')

    def test_get_error(self):
        results = get_github('bad_user')
        print(results)

if __name__ == '__main__':
    unittest.main()


