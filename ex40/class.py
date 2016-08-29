#! /usr/bin/env python


##
## A very basic class definition
## -----------------------------
##


class Song(object):

    def __init__(self, lyrics):
       self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_bday = Song(["Hapy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

happy_bday.sing_me_a_song()

the_reynes = Song(["And who are you",
                   "the proud lord said,",
                   "that I must bow so low?"])

the_reynes.sing_me_a_song()
