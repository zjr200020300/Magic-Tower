# LoadImage.py

import pygame
from pygame.locals import *
from Code.MyLibrary import *

# create sprite groups

# player_status
icon_group = pygame.sprite.Group()
dialog_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
# scenery
wall_group = pygame.sprite.Group()
ground_group = pygame.sprite.Group()
starrySky_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
upstairs_group = pygame.sprite.Group()
downstairs_group = pygame.sprite.Group()

# npc
fairy_group = pygame.sprite.Group()

# items: doors and keys
redDoor_group = pygame.sprite.Group()
blueDoor_group = pygame.sprite.Group()
yellowDoor_group = pygame.sprite.Group()
redKey_group = pygame.sprite.Group()
blueKey_group = pygame.sprite.Group()
yellowKey_group = pygame.sprite.Group()

# items: medicament and gems
redBlood_group = pygame.sprite.Group()
blueBlood_group = pygame.sprite.Group()
redGem_group = pygame.sprite.Group()
blueGem_group = pygame.sprite.Group()

# icon
icon = MySprite()
icon.load('F:/PyCharmPro/Magic Tower/Graphics/Scenery/player01icon.png', 32, 32, 1,False)
icon.position = 40, 40
icon_group.add(icon)



def load_scenery(i, ni, nj):
    if i == 0:
        star = MySprite()
        star.load('F:/PyCharmPro/Magic Tower/Graphics/Scenery/starry sky.png', 32, 32, 4)
        star.position = ni * 32, nj * 32
        starrySky_group.add(star)
    elif i == 1:
        wall = MySprite()
        wall.load('F:/PyCharmPro/Magic Tower/Graphics/Scenery/wall.png', 32, 32, 1)
        wall.position = ni * 32, nj * 32
        wall_group.add(wall)
    elif i == 2:
        ground = MySprite()
        ground.load('F:/PyCharmPro/Magic Tower/Graphics/Scenery/ground.png', 32, 32, 1)
        ground.position = ni * 32, nj * 32
        ground_group.add(ground)
    elif i == 3:
        lava = MySprite()
        lava.load('F:/PyCharmPro/Magic Tower/Graphics/Scenery/lava.png', 32, 32, 4)
        lava.position = ni * 32, nj * 32
        lava_group.add(lava)
    elif i == 4:
        block = MySprite()
        block.load('F:/PyCharmPro/Magic Tower/Graphics/Scenery/block.png', 32, 32, 1)
        block.position = ni * 32, nj * 32
        block_group.add(block)
    elif i == 11:
        up = MySprite()
        up.load('F:/PyCharmPro/Magic Tower/Graphics/Scenery/upstairs.png', 32, 32, 1)
        up.position = ni * 32, nj * 32
        upstairs_group.add(up)
    elif i == 12:
        down = MySprite()
        down.load('F:/PyCharmPro/Magic Tower/Graphics/Scenery/downstairs.png', 32, 32, 1)
        down.position = ni * 32, nj * 32
        downstairs_group.add(down)


def load_items(i, ni, nj):
    if i == 41:
        rHP = MySprite()
        rHP.load('F:/PyCharmPro/Magic Tower/Graphics/Items/红血瓶.png', 32, 32, 1)
        rHP.position = ni * 32, nj * 32
        redBlood_group.add(rHP)
    elif i == 42:
        bHP = MySprite()
        bHP.load('F:/PyCharmPro/Magic Tower/Graphics/Items/蓝血瓶.png', 32, 32, 1)
        bHP.position = ni * 32, nj * 32
        blueBlood_group.add(bHP)
    elif i == 45:
        rGem = MySprite()
        rGem.load('F:/PyCharmPro/Magic Tower/Graphics/Items/红宝石.png', 32, 32, 1)
        rGem.position = ni * 32, nj * 32
        redGem_group.add(rGem)
    elif i == 46:
        bGem = MySprite()
        bGem.load('F:/PyCharmPro/Magic Tower/Graphics/Items/蓝宝石.png', 32, 32, 1)
        bGem.position = ni * 32, nj * 32
        blueGem_group.add(bGem)


def load_npc(i, ni, nj):
    if i == 61:
        fairy = MySprite()
        fairy.load('F:/PyCharmPro/Magic Tower/Graphics/Characters/fairy.png', 32, 32, 4)
        fairy.position = ni * 32, nj * 32
        fairy_group.add(fairy)


def load_map(graph):
    nj = -1
    for j in graph:
        ni = -1
        nj += 1
        for i in j:
            ni += 1
            load_scenery(i, ni, nj)


def load_ine(level, ineList):
    for ine in ineList:
        i, ni, nj = ine[0], ine[1], ine[2]
        load_items(i, ni, nj)
        load_npc(i, ni, nj)


# update groups
def groups_update(ticks):
    starrySky_group.update(ticks, 100)
    wall_group.update(ticks, 100)
    ground_group.update(ticks, 100)
    lava_group.update(ticks, 100)
    block_group.update(ticks, 100)
    upstairs_group.update(ticks, 100)
    downstairs_group.update(ticks, 100)

    fairy_group.update(ticks, 100)

    redBlood_group.update(ticks, 100)
    blueBlood_group.update(ticks, 100)
    redGem_group.update(ticks, 100)
    blueGem_group.update(ticks, 100)

    icon_group.update(ticks, 100)
    dialog_group.update(ticks, 100)
    player_group.update(ticks, 100)


def groups_draw(screen):
    starrySky_group.draw(screen)
    wall_group.draw(screen)
    ground_group.draw(screen)
    lava_group.draw(screen)
    block_group.draw(screen)
    upstairs_group.draw(screen)
    downstairs_group.draw(screen)

    fairy_group.draw(screen)

    redBlood_group.draw(screen)
    blueBlood_group.draw(screen)
    redGem_group.draw(screen)
    blueGem_group.draw(screen)

    icon_group.draw(screen)
    dialog_group.draw(screen)
    player_group.draw(screen)


def groups_clear():
    starrySky_group.empty()
    wall_group.empty()
    ground_group.empty()
    lava_group.empty()
    block_group.empty()
    upstairs_group.empty()
    downstairs_group.empty()

    fairy_group.empty()

    redBlood_group.empty()
    blueBlood_group.empty()
    redGem_group.empty()
    blueGem_group.empty()
