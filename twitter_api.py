import requests
import creds

#getting 422 error here
#post consumer key & secret and get bearer token
API_key = creds.api_key
API_secret_key = creds.api_secret

url = 'https://api.twitter.com/'
auth_token = 'oauth2/token'
response = requests.post(url+auth_token,
    auth=(API_key, API_secret_key),
    data={'grant_type': 'client_credentials'})

access_token = response.json()['access_token']

search_url = '1.1/tweets/serach/'
product = 'fullarchive'
label = 'dev2'
# {"query":"smarterbalanced OR smarter balanced OR sbac","maxResults":"500","fromDate":"202001010000"}
query = {"query": "smarter balanced \"search api\"",
         "fromDate":"201001010000",
         "toDate":"202006040000"}
tweets = requests.post("https://api.twitter.com/1.1/tweets/search/fullarchive/dev2.json",
        headers={"Authorization": f"Bearer {access_token}"},
        data=query
        )
print(tweets.status_code)

# query['next'] = tweets.json()['next']
print(access_token)
tweet_results = tweets.json()['results']