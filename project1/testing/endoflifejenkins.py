import requests

req = requests.get("https://endoflife.date/api/tomcat/9.json")
result = req.json()

print(result)
print(type(result))