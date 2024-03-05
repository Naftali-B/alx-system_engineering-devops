#!/usr/bin/python3
'''
queries the Reddit API and returns a list
containing the titles of all hot articles
'''
import requests

def recurse(subreddit, hot_list=[], after=None):
    """returns a list of all hot post titles for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return None
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    r = requests.get(url, headers={'User-Agent': 'Particular-Demand377'},
        params={'after': after}).json()
    after = r.get('data', {}).get('after', None)
    posts = r.get('data', {}).get('children', None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get('data', {}).get('title', None))
    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
