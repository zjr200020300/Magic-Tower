# Main.py
# 18 * 13
import itertools, sys, time, random, math, pygame
from pygame.locals import *
from Code.MyLibrary import *
from Code.Map import INE, maps, get_item
from Code.LoadImage import *
from Code.Character import *


def init():
    pygame.init()
    screen = pygame.display.set_mode((32 * 18, 32 * 13))
    pygame.display.set_caption('Magic Tower')
    timer = pygame.time.Clock()

    return screen, timer


# main program begins
screen, timer = init()
# fonts
font11 = pygame.font.Font('C:/Windows/Fonts/STXINGKA.TTF', 32)
font12 = pygame.font.Font('C:/Windows/Fonts/Dengl.ttf', 18)
font2 = pygame.font.Font('C:/Windows/Fonts/AdobeSongStd-Light.otf', 32)
font3 = pygame.font.Font('C:/Windows/Fonts/ariali.ttf', 18)
font4 = pygame.font.Font(None, 40)

next_talk = 0


def print_info(screen, player):
    print_text(screen, font11, 120, 46, '级')
    print_text(screen, font2, 90, 46, str(player.level))

    print_text(screen, font12, 38, 84, '生命')
    print_text(screen, font3, 96, 85, str(player.hp))
    print_text(screen, font12, 38, 104, '攻击')
    print_text(screen, font3, 96, 105, str(player.atk))
    print_text(screen, font12, 38, 124, '防御')
    print_text(screen, font3, 96, 125, str(player.deff))
    print_text(screen, font12, 38, 144, '金币')
    print_text(screen, font3, 96, 145, str(player.gold))
    print_text(screen, font12, 38, 164, '经验')
    print_text(screen, font3, 96, 165, str(player.exp))

    print_text(screen, font12, 64, 320, '第')
    print_text(screen, font12, 88, 320, str(level))
    print_text(screen, font12, 104, 320, '层')


# init player
player = Hero(1000, 10, 10, 0, 0)
player.load('F:/PyCharmPro/Magic Tower/Graphics/Characters/hero01.png', 32, 32, 4)
player.position = 11 * 32, 32 * 11
player.direction = 0
player_group.add(player)
# dialog box
dialog_box = MySprite()
dialog_box.load('F:/PyCharmPro/Magic Tower/Graphics/Scenery/dialog box.png', 224, 72, 1)
dialog_box.position = 150, 150
# dialog_group.add(dialog_box)

graph = maps[0]
level = maps.index(graph)
# create the map of current level
load_map(graph)
load_ine(level, INE[level])

if __name__ == "__main__":
    # main loop
    while True:
        timer.tick(30)
        ticks = pygame.time.get_ticks()

        # events detecting
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            keys = pygame.key.get_pressed()
            if not player.isTalking:
                if keys[K_ESCAPE]:
                    sys.exit()
                elif keys[K_UP] or keys[K_w]:
                    player.direction = 3
                    player.moving = True
                elif keys[K_RIGHT] or keys[K_d]:
                    player.direction = 2
                    player.moving = True
                elif keys[K_DOWN] or keys[K_s]:
                    player.direction = 0
                    player.moving = True
                elif keys[K_LEFT] or keys[K_a]:
                    player.direction = 1
                    player.moving = True
                else:
                    player.moving = False
            else:
                if keys[K_SPACE]:
                    next_talk += 1
                    player.isTalking = False

        # select frame of player sprite
        player.first_frame = player.direction * player.columns
        player.last_frame = player.first_frame + player.columns - 1
        if player.frame < player.first_frame:
            player.frame = player.first_frame

        # if the player is moving
        if not player.moving:
            # stop animating when player is not pressing a key
            player.frame = player.first_frame = player.last_frame
        else:
            # move player in direction
            player.velocity = calc_velocity(player.direction, 1)
            player.velocity.x *= 32
            player.velocity.y *= 32

        # collision detection
        tempX = int((player.X + player.velocity.x) / 32)
        tempY = int((player.Y + player.velocity.y) / 32)
        if (collision_detection(tempY, tempX, graph)):
            player.moving = False

        # conversation detection
        npc = talk_detection(tempY, tempX, INE[level])
        if npc != 0:
            player.isTalking = True
            player.moving = False
        else:
            player.isTalking=False
        if player.isTalking:
            dialog_group.add(dialog_box)
            text = npc_fairy.conversation()
        else:
            dialog_group.empty()

        # if get an item
        if get_item(player.position, INE[level], player):
            groups_clear()
            load_map(graph)
            load_ine(level, INE[level])

        # manually move the player
        if player.moving:
            player.X += player.velocity.x
            player.Y += player.velocity.y
            player.moving = False

        # up or down
        old_level = level
        level = go(player.X, player.Y, graph, level)
        if old_level != level:
            if old_level < level:
                go_flag = 1  # go upstairs
            else:
                go_flag = 0  # go downstairs
            graph = maps[level]
            groups_clear()
            load_map(graph)
            load_ine(level, INE[level])
            player.position = new_map_position(level, go_flag)

        # update groups
        groups_update(ticks)

        # draw groups
        screen.fill((0, 0, 0))
        groups_draw(screen)

        # print player info
        print_info(screen, player)
        if player.isTalking:
            textList=npc_fairy.conversation()
            text = textList[next_talk]
            print_text(screen,font12,160,155,text[0])
            print_text(screen,font12,160,175,text[1])

        pygame.display.update()
