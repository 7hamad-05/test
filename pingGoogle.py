import requests

google_url = "https://google.com"

req=requests.get(google_url)

print("Status Code :",req.status_code,", Headers :",req.headers)