from bs4 import BeautifulSoup

OUTPUT_FILE="songUrlList.txt"

with open("rawhtml/songlist.html") as songhtml:
  soup = BeautifulSoup(songhtml, "lxml")

songUrls = soup.find_all("a", class_="title")

urlOutputFile = open(OUTPUT_FILE, 'w')

for songUrl in songUrls:
  urlOutputFile.write(songUrl.attrs['href'] + "\n")

urlOutputFile.close()

