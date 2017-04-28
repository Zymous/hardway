# -*- coding: utf-8 -*-
# @Author: Zymous
# @Date:   2017-04-28 15:27:18
# @Last Modified by:   Zymous
# @Last Modified time: 2017-04-28 16:41:00
# You Make a Game

from scene_ex45 import *

class Runner(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.

class Map(object):

    rooms = {
        "s_room": Sroom(),
        "h_room": Hroom(),
        "a_room": Aroom(),
        "f_room": Froom(),
        "e_room": Eroom(),
        "r_room": Rroom()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = self.rooms.get(scene_name)
        return val

    def openning_scene(self, scene_name):
        return self.next_scene(scene_name)

room = BeginRoom()
room.enter()