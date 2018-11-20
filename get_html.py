import requests

response = requests.get('https://www.scrapmagazine.com/')
print(response.text)
