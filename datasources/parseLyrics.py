from bs4 import BeautifulSoup
import glob, os

INPUT_FOLDER="rawhtml/songhtml/"
OUTPUT_FILE="songLyrics.txt"

# Do any filtering for each input document
def filteredSoup(soup):
  # Filter '<br>' to '\n'
  for br in soup.find_all("br"):
    br.replace_with("\n")

# Split an individual lyric block into lines
# and write the lines to the output file
def writeLyricBlockLines(lyric, outputFileHandle):
  for line in lyric.text.splitlines():
    if line:
      outputFileHandle.write(line + "\n")

# Break an entire input document into 
# lines and write to the outputfile
def writeSongHtmlLyrics(songFileHandle, outputFileHandle):
  soup = BeautifulSoup(songhtml, "lxml")
  filteredSoup(soup)

  lyrics = soup.find_all("p", class_="verse")
  for lyric in lyrics:
    writeLyricBlockLines(lyric, outputFile)

# Main

# Clear lyric output file (if it exists)
open(OUTPUT_FILE, 'w').close()

outputFile = open(OUTPUT_FILE, 'a')
for songfile in glob.glob(os.path.join(INPUT_FOLDER, '*.html')):
  with open(songfile) as songhtml:
    writeSongHtmlLyrics(songfile, outputFile)

outputFile.close()
