"""
This is the new version of the main.py script
Uses the sandbox environment and a different endpoint
API Documentation: https://developer.twitter.com/en/docs/tweets/search/api-reference/premium-search
"""

import requests
import creds


def get_tweets(search_string, auth=creds.bearer_token):
    """Getting 403 error"""
    api_endpoint = 'https://api.twitter.com/1.1/tweets/search/fullarchive/test.json'
    payload = {'query': f'@{search_string} from {search_string}'}
    headers = {'Authorization': f'Bearer {auth}',
               'content-type': 'application/json'}

    response = requests.post(api_endpoint, headers=headers, data=payload)

    return response.status_code, response.json()


if __name__ == '__main__':
    result = get_tweets('smarterbalanced')
    status, data_result = get_tweets('smarterbalanced')
    print(status)
