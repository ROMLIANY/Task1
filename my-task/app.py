import requests
import xml.etree.ElementTree as ET

# url of ynet
url = "https://www.ynet.co.il/Integration/StoryRss2.xml"

# info from web
response = requests.get(url)
response.raise_for_status()  # test errors

# replace form
root = ET.fromstring(response.content)

items = root.findall(".//item")

# print the title
print(" כותרות אחרונות מ-Ynet:\n")
for i, item in enumerate(items, start=1):
    title = item.find("title").text.strip()
    print(f"{i}. {title}")
