#!/usr/bin/python3
'''queries the Reddit API and prints the titles of the first 10 hot posts'''
import requests

def top_ten(subreddit):
    '''prints the titles of the first 10 hot posts listed for a given subreddit'''
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    res = requests.get(url, headers={'User-Agent': 'Particular-Demand377'}).json()
    if 'error' in res.keys():
        print(None)
        return
    all_posts = res.get('data').get('children')
    for i in range(10):
        print(all_posts[i].get('data').get('title'))
