import requests

url = "https://www.ynet.co.il/Integration/StoryRss2.xml"
response = requests.get(url)

print(response.text)
