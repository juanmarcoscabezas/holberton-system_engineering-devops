#!/usr/bin/python3

"""
Queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Get the top ten host posts
    """
    h = {
        'User-Agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0)\
    Gecko/20100101 Firefox/76.0'
    }
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?after={}'.format(after)
    r = requests.get(url, headers=h)
    if r.status_code != 200:
        return None

    response = r.json()
    data = response.get('data')
    posts = data.get('children')
    for post in posts:
        hot_list.append(post.get('data').get('title'))
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
