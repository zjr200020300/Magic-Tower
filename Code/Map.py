# Map.py
import copy


def list_add(l, l2):
    l1 = copy.deepcopy(l)
    for j1, j2 in zip(l1, l2):
        j1.reverse()
        for i in j1:
            j2.insert(0, i)


# starrySky=0,wall=1,ground=2,lava=3,block=4
up = 11
down = 12
rD = 21  # red blue yellow doors
bD = 23
yD = 25
rK = 22  # red blue yellow keys
bK = 24
yK = 26
rHP = 41
bHP = 42
ATK = 45
DEF = 46
item_list=[rD,bD,yD,rHP,bHP,ATK,DEF]
#npc
fairy=61

# bgd
status_bgd = [[4, 4, 4, 4, 4],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 2, 2, 2, 2],
              [4, 4, 4, 4, 4]]
level0_bgd = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [4, 1, 0, 0, 0, 0, up, 0, 0, 0, 0, 1, 4],
              [4, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 4],
              [4, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 4],
              [4, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 4],
              [4, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 4],
              [4, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 4],
              [4, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 4],
              [4, 1, 1, 0, 0, 0, 2, 0, 0, 0, 1, 1, 4],
              [4, 1, 3, 3, 1, 2, 2, 2, 1, 3, 3, 1, 4],
              [4, 1, 3, 3, 3, 1, 2, 1, 3, 3, 3, 1, 4],
              [4, 1, 3, 3, 3, 1, 2, 1, 3, 3, 3, 1, 4],
              [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]
level1_bgd = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [4, up, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4],
              [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4],
              [4, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 4],
              [4, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 4],
              [4, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 4],
              [4, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 4],
              [4, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 2, 4],
              [4, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 4],
              [4, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1, 4],
              [4, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 4],
              [4, 2, 2, 2, 1, 2, down, 2, 1, 2, 2, 2, 4],
              [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]

maps = [level0_bgd, level1_bgd]
for map in maps:
    list_add(status_bgd, map)

# items npc enemies --- ine
ine0=[(61,10,9)]
ine1=[(41,6,3),(45,8,4)]
INE=[ine0,ine1]

def get_item(pos, ineList, player):
    x = int(pos[0] / 32)
    y = int(pos[1] / 32)
    item = -1
    index = ()
    for ine in ineList:
        if (x, y) == (ine[1], ine[2]) and ine[0] in item_list:
            item = ine[0]
            index = ine
            break
    if item == 41:
        player.hp += 200
    elif item == 42:
        player.hp += 500
    elif item == 45:
        player.atk += 3
    elif item == 46:
        player.deff += 3
    else:
        pass
    if item != -1 and index != None:
        ineList.remove(index)
        return True
    else:
        return False
