import requests


class findSongs:

    def searchApi(self, pickedSong):
        url = "https://shazam.p.rapidapi.com/search"
        querystring = {f"term": {pickedSong}}
        headers = {
            'x-rapidapi-key': "94fa715ec9msh287bb2f3ea9b3fep1ddb1cjsncf93a0131f08",
            'x-rapidapi-host': "shazam.p.rapidapi.com"
            }
        res = requests.request("GET", url, headers=headers, params=querystring)
        print(res)
        print(res.status_code)
        return res

    def suggestSongs(self, songKey):
        url = "https://shazam.p.rapidapi.com/songs/list-recommendations"
        querystring = {f"key": {songKey}}
        headers = {
            'x-rapidapi-key': "94fa715ec9msh287bb2f3ea9b3fep1ddb1cjsncf93a0131f08",
            'x-rapidapi-host': "shazam.p.rapidapi.com"
            }
        res = requests.request("GET", url, headers=headers, params=querystring)
        return res

    # def createSongList(self, suggestedSongs):
    #     suggestedSongList = []
    #     for song in suggestedSongs:
    #         suggestedSongList.append(
    #             (song["track"]["title"]) + " by " + (song["track"]["subtitle"]))
    #     return suggestedSongList

    def createListOfSuggestions(self, suggestedSongs):
        suggestedSongList = []
        for song in suggestedSongs:
            suggestedSongList.append((song["title"]) + " by " + (song["subtitle"]))
        return suggestedSongList

    def printSongList(self, songList):
        for i, song in enumerate(songList):
            print(f"{i + 1}. {song}")

    def getSongs(self, pickedSong):
        response = self.searchApi(findSongs, pickedSong)
        suggestedSongs = response.json()["tracks"]["hits"]
        return suggestedSongs

    def selectSongs(self, songKey):
        print("next one")
        print("end")
        response2 = self.suggestSongs(findSongs, songKey)
        newSuggestedSongs = response2.json()["tracks"]
        return newSuggestedSongs
