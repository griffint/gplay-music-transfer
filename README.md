# gplay-music-transfer
A library for importing and exporting a google play music all access library.

### Summary
Ever worried about backing up metadata about your All Access library and playlists? This is the tool for you!
The goal of this library is to provide tools for backing up and transferring information about your google play music all access library.


### Getting Started
1. Clone the repo
2. Create a virtualenv for the project `virtualenv -py python3 env`
3. Install required pip packages `pip install -r requirements.txt`
4. In `secrets.json`, insert your google username and password
5. Activate the virtualenv `source env/bin/activate`
6. Run music_export.py with python3 `python3 gplay-music-transfer/music_export.py `
7. You'll now have json and csv files backing up all metadata about your all access library!

### Potential Use Cases:
* Backing up your library data in case of account shutdown
* Saving all library metadata in a plain format for importing into other music streaming services
* Moving your library from one google account to another

### Current WIP features:
* Exporting of generic library data in CSV and JSON format. Includes song titles, artists, and albums
* Export of all google play library data in JSON format

### Planned Features:
* Exporting of all playlist data in CSV format.
* Exporting of google play specific data like thumbs up
* Importing of data into a google play music all access library
* Web inteface for the project

If you're interested in any specific features being added, put in a github issue or send me a message.
If you'd like to contribute, feel free to fork the repo.

### Credits:
This utilizes the unofficial Google Music API by Simon Weber found here: https://github.com/simon-weber/gmusicapi
This project is similar to this one, which has not been updated in 3 years: https://github.com/brettcoburn/gmusic-migrate