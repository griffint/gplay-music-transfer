from gmusicapi import Mobileclient
import csv
import json


def connect_api():
    with open('secrets.json', 'r') as secrets:
        secrets_dict = json.load(secrets)
        user = secrets_dict['username']
        user_pass = secrets_dict['password']
    api = Mobileclient()
    api.login(user, user_pass, Mobileclient.FROM_MAC_ADDRESS)
    return api


def write_generic_libray_csv(songs, filename='library_generic.csv'):
    """
    Writes generic, plaintext info about a library to a csv file.
    CSV columns:
        Title
        Artist
        Album Name
    :param songs: Array of song dictionaries
    :param filename: output file to write to
    :return:
    """
    with open(filename, 'w', newline='') as csvfile:
        songwriter = csv.writer(csvfile)
        for song in songs:
            songwriter.writerow([song['title'], song['artist'], song['album']])


def write_generic_libray_json(songs, filename='library_generic.json'):
    songs_basics = []
    for song in songs:
        songs_basics.append({
            'title': song['title'],
            'artist': song['artist'],
            'album': song['album'],
        })
    with open(filename, 'w') as jsonfile:
        json.dump(songs_basics, jsonfile)


def write_full_library_json(songs, filename='library_full.json'):
    """
    Writes all library information accessible through the api to a json file.
    This will include lots of google play sepecific data, and result in a much
    larger file than writing generic data to a csv file
    :param songs: Array of song dictionaries
    :param filename:
    :return:
    """
    with open(filename, 'w') as jsonfile:
        json.dump(songs, jsonfile)


def api_cleanup(api):
    api.logout()


if __name__ == '__main__':
    api = connect_api()
    all_songs = api.get_all_songs()
    write_generic_libray_csv(all_songs)
    write_generic_libray_json(all_songs)
    write_full_library_json(all_songs)
    api_cleanup(api)
