import sys
import requests

print(sys.version)
print("Hellow World")

r = requests.get("www.google.com")
print(r.status_code)
