# Modules,Classes,And Objects
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_baby = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(['They rally around tha family',
                        'With pockets full of shells'])

wa_ga_ga = Song(["twinkle, twinkle","fufu"])

happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

wa_ga_ga.sing_me_a_song()

juju = "aaaa"

vv = Song(juju)
vv.sing_me_a_song()

dd = wa_ga_ga
dd.sing_me_a_song()

dd.lyrics = juju
dd.sing_me_a_song()

wa_ga_ga.sing_me_a_song()