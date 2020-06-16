
"""
# Twitter api documentation available at https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
We will get tweets and then put them in a sqlite file
"""
import csv

import requests

import creds


def get_tweets(search_string, auth=creds.bearer_token):
    """
    Finds the tweets for a given search string
    Arguments:
        :rparam search_string: str- search query
        :rparam auth: str- usually bearer token
    Returns: List???
    """

    search_string = f"?q={search_string}"
    headers = {'Authorization': f'Bearer {creds.bearer_token}'}
    api_endpoint = 'https://api.twitter.com/1.1/search/tweets.json'

    try:
        query = f'{api_endpoint}{search_string}'
        tweets = requests.request(
            method="GET", url=query, headers=headers).json()

        # putting resulting data into a list
        count = int(tweets['search_metadata']['count'])
        print(f'Found {count} tweets containing {search_string} query string')
        tweets_data = [[line['id'], line['created_at'], line['text'],
                        line['retweet_count'], line['favorite_count'],
                        line['user']['screen_name'], line['user']['followers_count'],
                        line['user']['statuses_count'], line['user']['verified'],
                        line['entities']['hashtags'], line['entities']['user_mentions']]
                       for line in tweets['statuses']]
    except Exception as e:
        print(e)
    return tweets_data


if __name__ == "__main__":
    with open('new_tweets.csv', 'w') as tweets_csv:
        writer = csv.writer(tweets_csv)
        header = ['id', 'created_at', 'text', 'retweet_count', 'favorite_count',
                  'user_name', 'followers_count', 'user_tweet_count',
                  'verified', 'hashtags', 'user_mentions']
        writer.writerow(header)
        writer.writerows(get_tweets('smarterbalanced', creds.bearer_token))


# parsing the dictionary to get proper value from dictionary
# user_name = tweets_df.user.apply(lambda x: x["name"])
# get structure of one user dictionary
# one_user = tweets_df['user'][0]
# write the data into a sqlite table called sbtweets
# tweets_df.to_sql('tweets', con=sqlite, if_exists='replace', index=False)

# sqlite.close()


'''
Structure of JSON response
Statuses:
    created_at: tweeted date
    id: tweet_id (might be useful)
    text: the actual tweet
    entities: has 
        hashtags, 
        symbols  
        user_mentions.
    url: [first element choose key to the tweet link ]
    user: could be its own table lots of user data
        like their follower count an all
    geo:
    coordinates:
    retweet_count:
    favorite_count:
    
    

Search_metadata:
    this can be useful to click next link

'''
