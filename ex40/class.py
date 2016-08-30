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


my_lyrics = ["Far over the misty mountains cold\nTo dungeons deep and caverns old\nWe must away ere break of day\nTo seek the pale enchanted gold."]

thorin_oakenshield = Song(my_lyrics)
thorin_oakenshield.sing_me_a_song()
