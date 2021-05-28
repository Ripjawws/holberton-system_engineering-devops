#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import requests

    req = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit),
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)
    if req.status_code == 200:
        req_json = req.json()
        list_hot = req_json['data']['children']
        for i in range(len(list_hot)):
            title = list_hot[i]['data']['title']
            print(title)
    else:
        print('None')
