import requests

URL = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
response = requests.get(URL)
open("python-logo-master-v3-TM.png", "wb").write(response.content)