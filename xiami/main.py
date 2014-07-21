# -*- coding: utf-8 -*-
__author__ = 'ghost'

import re

url = 'http://www.xiami.com/song/1773346501?spm=a1z1s.3521865.23309997.1.qojLGF'


def get_song_id(url):
    pattren = re.compile(r'/(\d+)\?')
    song_id = re.search(pattren, url).group(1)
    return song_id

def get_song_info_url(song_id):
    url = ('http://www.xiami.com/'
           'song/playlist/id/{song_id}/'
           'object_name/default/object_id/0/cat/json').format(song_id=song_id)
    return url

