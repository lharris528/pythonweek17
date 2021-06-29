from flask import Flask, request, render_template
from songFetcher import *


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/form", methods = ["GET"])
def form():    
    return render_template("form.html")

@app.route("/data", methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return render_template("home.html")
    if request.method == 'POST':
        startSong = request.form.to_dict().get('song')
        songData = findSongs.getSongs(findSongs, startSong)
        return render_template('data.html', songData = songData)

@app.route("/displaySongs", methods = ["GET", "POST"])
def display():
    songData = request.form
    print("HI")
    songKey = songData["songKey"]
    print(songData)
    selection = findSongs.selectSongs(findSongs, songKey)
    return render_template("displaySongs.html", recommendationResults = selection)
  

if __name__ == '__main__':
    app.run(debug=True)
