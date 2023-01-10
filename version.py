import requests as req

print(req.__version__)

request = req.get("http://www.google.com/")
print("Google Home Page: ")
print(request.text)

script = req.get("https://raw.githubusercontent.com/jaskim9824/CMPUT404Lab1/master/version.py")
print("Script on Github: ")
print(script.text)