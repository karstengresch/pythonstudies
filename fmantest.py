from urllib.request import urlopen

response = urlopen('https://api.github.com/search/repositories?q=topic:fman+topic:plugin&per_page=100&page=1')
print(response.status)