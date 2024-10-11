import requests
import os
import platform
import sys
from html.parser import HTMLParser

print("TeamSpeak3 Server installer")
print("Repository: github.com/medowic/ts3-server-installer\n")

if platform.system() == "Windows":
    ext = "zip"
    if platform.architecture()[0] == "64bit":
        ts3inst = "teamspeak3-server_win64"
    else:
        ts3inst = "teamspeak3-server_win32"
elif platform.system() == "Linux":
    ext = "tar.bz2"
    if platform.architecture()[0] == "64bit":
        ts3inst = "teamspeak3-server_linux_amd64"
    else:
        ts3inst = "teamspeak3-server_linux_x86"
else:
    print("Error: Couldn't resolve system platform")
    input()
    sys.exit(1)

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.download_url = None

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href' and str(ts3inst) in attr[1]:
                    self.download_url = attr[1]

url = "https://teamspeak.com/en/downloads/#server"
response = requests.get(url)
parser = MyHTMLParser()
parser.feed(response.text)

if parser.download_url:
    download_url = parser.download_url
    file_response = requests.get(download_url)
    with open(f"teamspeak_latest.{ext}", "wb") as file:
        file.write(file_response.content)
else:
    print("Error: Couldn't find url for downloading")
    input()
    sys.exit(1)

if platform.system() == "Windows":
    import zipfile
    with zipfile.ZipFile(f"teamspeak_latest.{ext}", "r") as archive:
        archive.extractall()
else:
    import tarfile
    with tarfile.open(f"teamspeak_latest.{ext}", "r:bz2") as archive:
        archive.extractall()

for path in os.listdir():
    if path.startswith("teamspeak3-server"):
        os.rename(path, "ts3-server")

os.remove("teamspeak_latest.zip")
with open("ts3-server/.ts3server_license_accepted", "w") as _:
    pass

if platform.system() == "Windows":
    print("Done! Installation was successful.")
    print("Start 'ts3server.exe' in 'ts3-server' folder to run a server")
    input()
sys.exit(0)