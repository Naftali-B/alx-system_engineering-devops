#!/usr/bin/python3
'''
queries the reddit API recursively and counts occurrences
of keywords in hot article titles
'''
import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """prints a sorted count of given keywords
       in hot articles of a subreddit"""

    if subreddit is None or not isinstance(subreddit, str):
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    r = requests.get(url, headers={'User-Agent': 'Particular-Demand377'},
        params={'after': after}).json()
    after = r.get('data', {}).get('after', None)
    posts = r.get('data', {}).get('children', None)

    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
        return

    for post in posts:
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            word = word.lower()
            if word in title:
                word_count[word] = word_count.get(word, 0) + title.count(word)

    return count_words(subreddit, word_list, after, word_count)
