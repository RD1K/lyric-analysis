from requests import get
from bs4 import BeautifulSoup
import lyricsgenius

TOKEN = ""

genius = lyricsgenius.Genius(TOKEN)
# Client access token generated at https://genius.com/api-clients/new
genius.remove_section_headers = True
# Removes things like [Chorus] and [Verse] from the lyrics
genius.verbose = True
# The lyricsgenius library will give output about its current actions
genius.excluded_terms = ["Remix", "Live", "Snippet", "Skit"]
# Excludes songs with the above terms in the title, because they may skew results

rawArtist = input("What artist do you want to learn about? ")

choice = input("Would you like to learn about the vocabulary of (1) a record, (2) a track, or (3) an artist's entire discography? ")

if choice == "1" or choice == "3":
    artist = rawArtist.lower()
    artist = artist.split(" ")
    artist = "".join(artist)
    firstLetter = artist[0]
    url = ("https://www.azlyrics.com/%s/%s.html" % (firstLetter, artist))
    html = get(url)
    soup = BeautifulSoup(html.text, "lxml")
    albums = soup.find_all('b')
    length = len(albums)
    albumList = []
    album_ids = {}
    for tag in soup.find_all("b"):
        try:
            album_ids[tag.string] = tag.parent["id"]
        except:
            break

place = 1

if choice == "1" or choice == "3":
    for name, value in album_ids.items():
        parent = soup.find(id = value)
        if choice == "1":
            print("(%s) %s" % (place, name))
        else:
            pass
        albumList.append(name)
        place += 1
else:
    pass

results = []
if choice == "1":
    albumChoice = input("Enter the number of the record to view the lyrical variety of. ")
    results.append(soup.find(id=album_ids[albumList[int(albumChoice) - 1]]))
else:
    pass

if choice == "3":
    for album in albumList:
        results.append(soup.find(id=album_ids[album]))

tracklist = []

if choice == "1" or choice == "3":
    for result in results:
        for sibling in result.next_siblings:
            splitted = str(sibling).split()
            if splitted != [] and splitted[1] == 'class="listalbum-item"><a':
                tracklist.append(str(sibling.string))
            else:
                if splitted == []:
                    pass
                else:
                    break

if choice == "2":
    songName = input("What song do you want to view the lyrical variety of? ")
    tracklist.append(songName)

averageVocab = []
allLyrics = []

for track in tracklist:
    try:
        song = genius.search_song(track, rawArtist)
        splitLyrics = song.lyrics.split()
        allLyrics += splitLyrics
        total = len(splitLyrics)
        part = len(set(splitLyrics))
        print("The song \"%s\" has %s percent unique lyrics." % (track, str(round((part/total)*100, 2))))
        averageVocab.append(part/total)
    except:
        pass

if choice == "1" or choice == "3":
    sum = 0
    for item in averageVocab:
        sum += item
    allTotal = len(allLyrics)
    allPart = len(set(allLyrics))
    allAverage = round(allPart/allTotal*100, 2)
    average = round(sum/len(averageVocab)*100, 2)
    if choice == "1":
        string = "record"
    else:
        string = "artist's entire discography"
    print("On average, this %s consists of %s percent unique lyrics." % (string, str(average)))
    print("In total, the %s consists of %s percent unique lyrics." % (string, str(allAverage)))
else:
    pass
