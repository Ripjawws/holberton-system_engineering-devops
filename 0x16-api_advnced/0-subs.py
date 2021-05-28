#!/usr/bin/python3
""" reddit api """
import requests


def number_of_subscribers(subreddit):
    """function reddit"""
    req = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers={'User-Agent': 'My User Agent'}, allow_redirects=False)

    if(req.status_code == 200):
        req_json = req.json()
        return req.json().get('data').get('subscribers')
    return (0)
