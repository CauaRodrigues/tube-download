import requests

url = requests.get(
    'https://www.youtube.com/playlist?list=PLc0PaCztdgoqCAcaqwW0YS6lCWNfHk')
print(url.status_code)
