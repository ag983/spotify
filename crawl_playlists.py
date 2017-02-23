#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Get all track listings from user's Spotify playlists
and put them in a CSV file

"""

# from __future__ import unicode_literals
import csv
import re
from spotipy_helpers import *       # includes login details for spotify (start_spotify)



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



