# -*- coding: utf-8 -*-
__author__ = 'ghost'


import os
import os.path
import re
import sys
import stat
from xiamiHttp import XiamiHttp
from xiamiParse import XiamiParser


class XiaMi(object):

    def __init__(self):
        self.category = {
            'mp3': ('song_url', 'mp3'),
            'lyric': ('lyric', 'Irc'),
            'picture': ('pic', 'jpg')
        }

    def start(self):
        self.song_id = self._get_song_id_from_input()
        self.request_url = self._get_song_request_url(self.song_id)
        self.song_json = self._get_song_json(self.request_url)
        self.song_info = self._get_song_info(self.song_json)
        self.song_url = self.song_info['song_url']


        sys.stdout.write('####### start download mp3 ####### \r')
        self._download('mp3')
        sys.stdout.write('####### download completed ####### \r')

        sys.stdout.write('####### start download lyric ####### \r')
        self._download('lyric')
        sys.stdout.write('####### download completed ####### \r')

        sys.stdout.write('####### start download pic ####### \r')
        self._download('picture')
        sys.stdout.write('####### download completed ####### \r')


    def _get_song_id_from_input(self):
        song_url = raw_input(u"请输入歌曲的url地址：", )
        pattren = re.compile(r'/(\d+)\?')
        song_id = re.search(pattren, song_url).group(1)
        return song_id

    def _get_song_request_url(self, song_id):
        url = ('http://www.xiami.com/'
               'song/playlist/id/{song_id}/'
               'object_name/default/object_id/0/cat/json').format(song_id=song_id)
        return url

    def _get_song_json(self, url):
        res = XiamiHttp.send_request(url)
        j = XiamiHttp.get_res_json(res)
        return j

    def _get_song_info(self, data):
        return XiamiParser.get_song_info(data)

    def _checkout_directory(self, directory_name):
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
            os.chmod(directory_name, stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO) # mode:777


    def _download(self, type='mp3'):

        file_name = self.song_id
        entry = self.category.get(type)

        extension_name = entry[1]
        req_url = self.song_info.get(entry[0])

        directory_name = 'download/{directory_name}'.format(directory_name=file_name)

        self._checkout_directory(directory_name)

        filename = '{directory_name}/{file_name}.{extension_name}'.\
            format(directory_name=directory_name, file_name=file_name, extension_name=extension_name)

        XiamiHttp.save(req_url, filename)



    # def _download_mp3(self):
    #     directory_name = 'download/{filename}'.format(filename=self.song_id)
    #     self._checkout_directory(directory_name)
    #     file_name = '{directory_name}/{filename}.mp3'.\
    #         format(directory_name=directory_name, filename=self.song_id)
    #     XiamiHttp.save(self.song_url, file_name)
    #
    # def _download_lyric(self):
    #     directory_name = 'download/{filename}'.format(filename=self.song_id)
    #     self._checkout_directory(directory_name)
    #     file_name = '{directory_name}/{filename}.Irc'.\
    #         format(directory_name=directory_name, filename=self.song_id)
    #     XiamiHttp.save(self.song_info['lyric'], file_name)
    #
    # def _download_pic(self):
    #     directory_name = 'download/{filename}'.format(filename=self.song_id)
    #     self._checkout_directory(directory_name)
    #     file_name = '{directory_name}/{filename}.jpg'.\
    #         format(directory_name=directory_name, filename=self.song_id)
    #     XiamiHttp.save(self.song_info['pic'], file_name)

if __name__ == '__main__':
    url = 'http://www.xiami.com/song/1773346501?spm=a1z1s.3521865.23309997.1.254APJ'
    app = XiaMi()
    app.start()
