import requests
r=requests.get("https://api.agify.io/?name=bella")
print(r.text)