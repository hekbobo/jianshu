# coding=utf-8

import pycurl
import urllib
from io import StringIO
import json
import re
import requests
import urllib.parse
import certifi
from urllib.parse import urlencode, quote_plus

# class definition

class shua_view_class:

    def __init__(self,link):
        self.website = str(link)
        self.configure()

    def configure(self):
        self.c = pycurl.Curl()
        USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        self.c.setopt(pycurl.HTTPHEADER, ['Origin: http://www.jianshu.com', 'Referer: '+self.website])    # this line is very important to if we can succeed!
        self.c.setopt(self.c.FOLLOWLOCATION, 1)
        self.c.setopt(pycurl.VERBOSE, 0)
        self.c.setopt(pycurl.FAILONERROR, True)
        self.c.setopt(pycurl.USERAGENT, USER_AGENT)

    def shuaview(self):
        data_form = {
            'fuc': "1",
        }

        buffer = StringIO()
        data_post = urlencode(data_form)
        url = self.website.replace("/p/","/asimov/notes/") + '/mark_viewed'
        self.c.setopt(pycurl.URL, url)
        self.c.setopt(pycurl.POST, 1)
        self.c.setopt(pycurl.POSTFIELDS, data_post)
        self.c.setopt(self.c.WRITEFUNCTION, buffer.write)
        self.c.setopt(pycurl.CAINFO, certifi.where())
        self.c.perform()

        response = buffer.getvalue()
        print(response)
        #response_json = json.loads(response)

    def exit(self):
        self.c.close()


Post_link="https://www.jianshu.com/p/e33268cfe41d"
n = 0
app=shua_view_class(Post_link)
while True:
    app.shuaview()
    n += 1
    print("ok:"+str(n))

    if n > 100:  # add 101 more views
        break

app.exit()
