import requests
import xml.etree.ElementTree as ET

url = "https://www.ynet.co.il/Integration/StoryRss2.xml"
response = requests.get(url)

root = ET.fromstring(response.content)

for item in root.findall(".//item"):
    title = item.find("title").text
    print(title)
