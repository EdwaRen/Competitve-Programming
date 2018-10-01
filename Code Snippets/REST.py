import requests

# GET request
r = requests.get('https://api.github.com/events')
print(r.content)

# POST request
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
print(r.content)
