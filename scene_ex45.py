# -*- coding: utf-8 -*-
# @Author: Zymous
# @Date:   2017-04-28 15:52:12
# @Last Modified by:   Zymous
# @Last Modified time: 2017-04-28 16:17:58
# Maps for ex45
class Scene(object):

    def enter(self):
        print "It's the base class for map, you should Subclass it in your own class"
        exit(1)

class BeginRoom(Scene):

    def enter(self):
        print "You wake up in a room with gun in your hand,"
        print "then, you realize you are a policeman,"
        print "you are here to protect 5 people in 5 rooms."
        print "Every 10 minutes, a killer will come to one room"
        print "and kill the one in this room"