import requests as req

print(req.__version__)

request = req.get("http://www.google.com/")
print(request)