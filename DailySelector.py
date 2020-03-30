from urllib.request import urlopen
import json, random

def getData():
    word_url = "https://random-word-api.herokuapp.com/word?number=1"
    word_res = urlopen(word_url)
    random_word = ''.join(json.loads(word_res.read()))
    random_number = random.randint(0,10)

    movie_url = "http://www.omdbapi.com/?apikey=4ee51d38&type=movie&s=" + random_word + "&page=" + str(random_number)
    movie_res = urlopen(movie_url)
    data = json.loads(movie_res.read())
    return data

def main():
    res = getData()
    if (res['Response'] == "False"):
        main()
    else:
        print(res['Search'][0]['Title'] + " (" + res['Search'][0]['Year'] + ")")

main()


