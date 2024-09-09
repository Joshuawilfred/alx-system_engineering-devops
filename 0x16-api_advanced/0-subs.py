#!/usr/bin/python3
import requests

subreddit = '/marvelmemes/'
x = requests.get('https://www.reddit.com/api/v1/learnpython')
print(x)