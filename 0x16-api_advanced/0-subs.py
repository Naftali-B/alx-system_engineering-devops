#!/usr/bin/python3
'''queries the Reddit API and returns the number of subscribers'''
import requests

def number_of_subscribers(subreddit):
    '''returns number of subscribers or 0 if subreddit is invalid'''
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    res = requests.get(url, headers={'User-Agent': 'Particular-Demand377'}).json()
    sub_count = 0
    if 'error' not in res.keys():
        sub_count = res.get('data').get('subscribers')
    return sub_count

