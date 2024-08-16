#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API and returns a list of titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.
        after (str): The "after" parameter for pagination.

    Returns:
        list: A list containing the titles of all hot articles, or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-custom-agent/0.1'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data['data']['children']
            after = data['data']['after']

            # Append the titles to the hot_list
            hot_list.extend([child['data']['title'] for child in children])

            # If there is a next page, recurse
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
