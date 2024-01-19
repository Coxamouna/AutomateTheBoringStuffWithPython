import requests

web = requests.get('https://automatetheboringstuff.com/files/rj.txt')
web.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in web.iter_content(100000):
    playFile.write(chunk)
playFile.close()