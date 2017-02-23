#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Get all track listings from user's Spotify playlists
and put them in a CSV file

"""

# from __future__ import unicode_literals
import csv
import re
from spotipy_helpers import *



session = start_spotify()


def store_track_data(playlist, track):
    # song_link =  re.sub('spotify:track:', 'https://play.spotify.com/album/', track.link.uri)
    row = [playlist.name, playlist.owner.display_name, playlist.owner.canonical_name, str(len(playlist.subscribers)), track.name, track.album.name, str(track.duration), track.artists[0].name, str(track.popularity), track.link.uri, track.link.url]
    row = [s.encode('utf-8') for s in row]
    trackwriter.writerow(row)


# Main program starts here
csvfile = open('~/projects/spotify/spotify_tracks.csv', 'w')
trackwriter = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_NONNUMERIC)   # , quoting=csv.QUOTE_MINIMAL
# trackwriter.writerow(['Spam'] * 5 + ['Baked Beans', 5.234])
# csvfile.close()


all_tracks = [];

container = session.playlist_container
container.load()

# iterate through items inthe playlist_container. Note will not handle playlists-within-playlists
for item in container:
    if hasattr(item, 'tracks'):
        for track in item.tracks:
            store_track_data (item, track)




# first_track = container[0].tracks[0]
# playlist_name = container[0].name
#
#
# # search = session.search('adele')
# search = session.search(raw_input("Search for tracks by artist, track or playlist"))
# search.load()
#
# for i in range(0, 12):
#     print(str(i) + ": " + search.tracks[i].name + "   " + str(search.tracks[i].popularity))
#
# t = raw_input("Which track would you like to hear (or enter for random playlist track)?")
# if len(t) > 0:
#     track_uri = search.tracks[int(t)].link.uri
# else:
#     track_uri = first_track.link.uri
#
#
# # Play a track
# track = session.get_track(track_uri).load()
# session.player.load(track)
# session.player.play()
#
# # Wait for playback to complete or Ctrl+C
# try:
#     while not end_of_track.wait(0.1):
#         pass            # this means "do nothing"
# except KeyboardInterrupt:
#     pass
#
#

# file = open('myfile.dat', 'w+')
#
# with open('/home/ai/projects/spotify/eggs.csv', 'w') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',',
#                             quotechar='"', quoting=csv.QUOTE_NONNUMERIC)   # , quoting=csv.QUOTE_MINIMAL
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans', 5.234])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam', -0.1335, str(2)])