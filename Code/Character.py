# Character.py
from Code.MyLibrary import *
import pygame


class Character:
    def __init__(self, hp, atk, deff, gold, exp):
        self.hp = hp
        self.atk = atk
        self.deff = deff
        self.gold = gold
        self.exp = exp


class Hero(Character, MySprite):
    def __init__(self, hp, atk, deff, gold, exp):
        MySprite.__init__(self)
        self.level = 1
        self.hp = hp
        self.atk = atk
        self.deff = deff
        self.gold = gold
        self.exp = exp
        self.moving = False
        self.isTalking = False


fairy_dialogue = {1: [('我是仙女，被困在这里','我需要你的帮助'),
                      ['我的十字架在第18层'],
                      ['请你取回我的十字架\n我可以增强强你的实力']],
                  2: ['我的十字架在第18层\n请你赶快取回来']}


class Npc:
    def __init__(self, pos_3, dialogue):
        self.position = pos_3 #level x y
        self.meet = 0
        self.dialogue = dialogue
        self.talk_status=False
        self.talk_num = 0

    def conversation(self):
        if self.meet <= 1:
            talk = self.dialogue[1]
        else:
            talk = self.dialogue[2]
        return talk

npc_fairy = Npc((0,10,9),fairy_dialogue)
