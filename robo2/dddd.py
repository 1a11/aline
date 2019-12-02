import requests
url1 = "http://localhost:666/get"
res = requests.post(url = url1)
print(res.text)
