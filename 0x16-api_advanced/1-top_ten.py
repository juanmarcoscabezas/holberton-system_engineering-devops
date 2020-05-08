#!/usr/bin/python3

"""
Queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Get the top ten host posts
    """
    h = {
        'User-Agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0)\
 Gecko/20100101 Firefox/76.0'
    }
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers=h)
    if r.status_code == 200:
        response = r.json()
        data = response.get('data')
        posts = data.get('children')
        for i, post in enumerate(posts):
            if i < 10:
                print(post.get('data').get('title'))
            else:
                return
