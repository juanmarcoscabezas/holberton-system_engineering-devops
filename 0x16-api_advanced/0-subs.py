#!/usr/bin/python3

"""
Queries the REddit API and returns the number of
subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit
is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers
    """
    h = {
        'User-Agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0)\
 Gecko/20100101 Firefox/76.0'
    }
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, headers=h)
    if r.status_code > 200:
        return 0
    response = r.json()
    data = response.get('data')
    if data:
        subscribers = data.get('subscribers')
        return subscribers
    return 0
