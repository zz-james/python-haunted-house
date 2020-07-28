import random

numberOfVerbs = 25  # first word
numberOfNouns = 36  # second word
numberOfGettables = 18  # things you can get

rooms = ['SE', 'WE', 'WE', 'SWE', 'WE', 'WE',  'SWE', 'WS',
         'NS', 'SE', 'WE', 'NW', 'SE', 'W',  'NE', 'NSW',
         'NS', 'NS', 'SE', 'WE', 'NWUD', 'SE',  'WSUD', 'NS',
         'N', 'NS', 'NSE', 'WE', 'WE', 'NSW',  'NS', 'NS',
         'S', 'NSE', 'NSW', 'S', 'NSUD', 'N',  'N', 'NS',
         'NE', 'NW', 'NE', 'W', 'NSE', 'WE',  'W', 'NS',
         'SE', 'NSW', 'E', 'WE', 'NW', 'S',  'SW', 'NW',
         'NE', 'NWE', 'WE', 'WE', 'WE', 'NWE',  'NWE', 'W']  # rooms (shows exits)

description = ["dark corner", "overgrown garden", "by large woodpile", "yard by rubbish", "weedpatch", "forest", "thick forest", "blasted tree",
               "corner of house", "entrance to kitchen", "kichen & grimy cooker", "scullery door", "room with inches of dust", "rear turret room",
               "clearning by house", "path", "side of house", "back of hallway", "dark alcove", "small dark room", "bottom of spiral staircase", "wide passage",
               "slippery steps", "clifftop", "near crumbling wall", "gloomy passage", "pool of light", "impressive vaulted hallway", "hall by thick wooden door", "trophy room",
               "cellar with barred window", "cliff path", "cupboard with hanging coat", "front hall", "sitting room", "secret room", "steep marble stairs", "dining room",
               "deep cellar with coffin", "cliff path", "closet", "front lobby", "library of evil books", "study with desk & hole in wall", "weird cobwebby room", "very cold chamber",
               "spooky room", "cliff path by marsh", "rubble-strewn verandah", "front porch", "front tower", "sloping corridor", "upper gallery", "marsh by wall",
               "marsh", "soggy path", "twisted railing", "path through iron gate", "by railings", "beneath front tower", "debris from crumbling facade", "large fallen brickwork",
               "rotting stone arch", "crumbling clifftop"]

objects = ["painting", "ring", "magic spells", "goblet", "scroll", "coins",
           "statue", "candlestick", "matches", "vacuum", "batteries", "shovel",
           "axe", "rope", "boat", "aerosol", "candle", "key", "north", "south",
           "west", "east", "up", "down", "door", "bats", "ghosts", "drawer",
           "desk", "coat", "rubbish", "coffin", "books", "xzanfar", "wall", "spells"]

flag = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

verbs = ['help', 'carrying', 'go', 'n', 's', 'w', 'e', 'u', 'd', 'get', 'take', 'open', 'examine',
         'read', 'say', 'dig', 'swing', 'climb', 'light', 'unlight', 'spray', 'use', 'unlock', 'leave', 'score']  # verbs

carrying = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

listOfGettables = [46, 38, 35, 50, 13, 18, 28, 42, 10, 25, 26,
                   4, 2, 7, 47, 60, 43, 32]  # list of the room numbers of the 18 gettables

# some positions in the flag array are not tied to the objects
flag[18] = 1  # key
flag[17] = 1  # candle
flag[2] = 1  # ring
flag[26] = 1  # bats
flag[28] = 1  # drawer
flag[23] = 1  # up
LL = 60  # candle time left

room = 57
message = "ok"


def wordsIKnow():
    global message
    for i in range(numberOfVerbs):
        print(verb[i])
    message = ''
    inputASpace()


def inventory():
    global message
    print('you are carrying')
    for i in range(numberOfGettables):
        if(carrying[i] == 1):
            print(objects[i]+", ")
    message = ''
    print('')
    inputASpace()


def go():
    global room
    global message
    direction = 0  # [n, s, w, e, u, d]
    if(objectPosition == 0):
        # north, south, west, east, up, down are verbposition 4, 5, 6, 7, 8, 9
        direction = verbPosition-2
    if(objectPosition == 19):  # north
        direction = 1
    if(objectPosition == 20):  # south
        direction = 2
    if(objectPosition == 21):  # west
        direction = 3
    if(objectPosition == 22):  # east
        direction = 4
    if(objectPosition == 23):  # up
        direction = 5
    if(objectPosition == 24):  # down
        direction = 6

    # convert up and down into north and south cheat on map representation
    if(room == 20 and direction == 5):
        direction = 1
    if(room == 20 and direction == 6):
        direction = 3
    if(room == 22 and direction == 6):
        direction = 2
    if(room == 22 and direction == 5):
        direction = 3
    if(room == 36 and direction == 6):
        direction = 1
    if(room == 36 and direction == 5):
        direction = 2

    # SPECIAL FLAGGED CONDITIONS
    if(flag[14] == 1):
        message = "crash you fell out of the tree"
        flag[14] = 0
        return

    if(flag[27] == 1 and room == 52):
        message = "ghosts will not let you move"
        return

    if(room == 45 and carrying[1] == 1 and flag[34] == 0):
        message = "a magical barrier to the west"
        return

    if((room == 26 and flag[0] == 0) and (direction == 1 or direction == 4)):
        message = "you need a light"
        return

    if(room == 45 and carrying[15] != 1):
        message = "you're stuck"
        return

    if(carrying[15] == 1 and not(room == 53 or room == 54 or room == 55 or room == 47)):
        message = "you can't carry a boat"
        return

    if((room > 26 and room < 30) and flag[0] == 0):
        message = "too dark to move"
        return

    flag[35] = 0  # is there an exit?
    # this is about checking valid exits/routes
    routesLength = len(rooms[room])

    for i in range(routesLength):
        u = rooms[room][i]

        if(u == "N" and direction == 1 and flag[35] == 0):
            room = room - 8
            flag[35] = 1
            break

        if(u == "S" and direction == 2 and flag[35] == 0):
            room = room + 8
            flag[35] = 1
            break

        if(u == "W" and direction == 3 and flag[35] == 0):
            room = room - 1
            flag[35] = 1
            break

        if(u == "E" and direction == 4 and flag[35] == 0):
            room = room + 1
            flag[35] = 1
            break

    message = "ok"

    if(flag[35] == 0):
        message = "you can't go that way"

    if(direction < 1):
        message = "go where?"

    if(room == 41 and flag[23] == 1):  # lobby front door open
        rooms[49] = "SW"
        message = "the door slams shut"
        flag[23] = 0  # front door shut
# this is the end of the go function.


def get():
    global message
    if(objectPosition > numberOfGettables):
        message = "I can't get "+_object
        if listOfGettables[objectPosition] != room:
            message = "it isn't here"
        if flag[objectPosition] != 0:
            message = "what "+_object
        if carrying[objectPosition] == 1:
            message = "you already have it"
        if (objectPosition > 0 and listOfGettables[objectPosition] == room and flag[objectPosition] == 0):
            carrying[objectPosition] = 1
            listOfGettables[objectPosition] = 65
            message = "you have the "+_object


def open():
    global message
    if(room == 43 and (objectPosition == 28 or objectPosition == 29)):
        flag[17] = 0
        message = "Drawer open"

    if(room == 28 and objectPosition == 25):
        message = "it's locked"

    if(room == 38 and objectPosition == 32):
        message = "that's creepy"
        flag[2] = 0


def examine():
    global message
    if(objectPosition == 30):
        flag[18] = 0
        message = "something here!"
    if(objectPosition == 31):
        message = "that's disgusting"
    if(objectPosition == 28 or objectPosition == 29):
        message = "there's a drawer"
    if(objectPosition == 33 or objectPosition == 5):
        say()
    if(room == 43 and objectPosition == 35):
        message = "there is something beyond"
    if(objectPosition == 32):
        open()


def read():
    global message
    if(room == 42 and objectPosition == 33):
        message = "they are demonic works"
    if((objectPosition == 3 or objectPosition == 36) and carrying[3] == 1 and flag[34] == 0):
        message = "use this word with care 'xzanfar'"
    if(carrying[5] == 1 and objectPosition == 5):
        message = "the script is in an alien tongue"


def say():
    message = "ok "+_object
    if(carrying[3] == 1 and objectPosition == 34):
        message == "magic occurs"
        if(room != 45):
            room = random.randint(1, 63)
    if(carrying[3] == 1 and objectPosition == 34 and room == 45):
        flag[34] = 1


def dig():
    global message
    if(carrying[12] == 1):
        message = "you made a hole"
    if(carrying[12] == 1 and room == 30):
        message = "dug the bars out"
        rooms[room] = "NSE"


def swing():
    global message
    if(carrying[14] != 1 and room == 7):
        message = "this is no time to play games"
    if(objectPosition == 14 and carrying[14] == 1):
        message = "you swung it"
    if(objectPosition == 13 and carrying[13] == 1):
        message = "swoooosh"
    if(objectPosition == 13 and carrying[13] == 1 and room == 43):
        rooms[room] = "WN"
        description[room] = "Study with a secret room"
        message = "you broke the thin wall"


def climb():
    global message
    if(objectPosition == 14 and carrying[14] == 1):
        message = "it isn't attached to anything"
    if(objectPosition == 14 and carrying[14] != 1 and room == 7 and flag[14] == 0):
        message = "you see thick forest and cliff south"
        flag[14] = 1
        return
    if(objectPosition == 14 and carrying[14] != 1 and room == 43 and flag[14] == 1):
        message = "going down!"
        flag[14] = 0


def light():
    global message
    if(objectPosition == 17 and carrying[17] == 1 and carrying[8] == 0):
        message = "it will burn your hands"
    if(objectPosition == 17 and carrying[17] == 1 and carrying[9] == 0):
        message = "nothing to light it with"
    if(objectPosition == 17 and carrying[17] == 1 and carrying[9] == 1 and carrying[8] == 1):
        message = "it casts a flickering light"
        flag[0] = 1


def unlight():
    global message
    if (flag[0] == 1):
        flag[0] = 0
        message = "extinguished"


def spray():
    global message
    if(objectPosition == 26 and carrying[16] == 1):
        message = "hisssssssssss"
    if(objectPosition == 26 and carrying[16] == 1 and flag[26] == 0):
        message = "pfffft got them"


def use():
    global message
    if(objectPosition == 10 and carrying[10] == 1):
        message = "switched on!"
    if(flag[27] == 1 and flag[24] == 1):
        message = "whizzzzz - vacuumed the ghosts up"
        flag[27] = 0


def unlock():
    global message
    if(room == 43 and (objectPosition == 27 or objectPosition == 28)):
        open()
    if(room == 28 and objectPosition == 25 and flag[25] == 0 and carrying[18] == 1):
        flag[25] = 1
        rooms[room] = "SEW"
        description[room] = "huge open door"
        message = "the key turns"
    if(carrying[objectPosition] == 1):
        carrying[objectPosition] = 0
        listOfGettables[objectPosition] = room
        message = "done!"


def leave():
    global message
    if carrying[objectPosition] == 1:
        carrying[objectPosition] = 0
        listOfGettables[objectPosition] = room
        message = "DONE"


def score():
    global gameOver
    s = 0

    for i in range(numberOfGettables):
        if(carrying[i] == 1):
            s += 1

    if(s == 17 and carrying[15] != 1 and room != 57):
        print("you have everything")
        print("return to the gate for the final score")

    if(s == 17 and room == 57):
        print("double score for reaching here")
        s = s * 2

    print("you're score = "+s)
    if(s > 18):
        print("well done you finsished the game")
        gameOver = True

    inputASpace()


def inputASpace():  # 1580
    input('press return to continue')
    return


def batsAttacking():
    global gameOver
    gameOver = True


while True:
    print('\n')
    print('Haunted House')
    print('-------------')
    print('your location:')
    print(description[room])
    print('\n')
    print('exits:')

    for i in range(len(rooms[room])):
        print(rooms[room][i]+',')

    for i in range(numberOfGettables):
        if((objects[i] == room) and (flag[i] == 0)):
            print('you can see: ')
            print(objects[i])
            print('here')

    print('-------------')

    print(message)
    message = 'what'
    print('\n')
    query = input('what will you do now?')
    print('\n')
    # parse input string
    verb = ''  # clear verb
    _object = ''  # clear noun
    verbPosition = 0  # position in verb list
    objectPosition = 0  # position in objects list

# spilt q by space
    if len(query.split()) > 1:
        verb, _object = query.split()
    else:
        verb = query

    # if(_object == ""):
    #     verb = query

    # find
    for i in range(numberOfVerbs):
        if(verb == verbs[i]):
            verbPosition = i

    for i in range(numberOfNouns):
        if(_object == objects[i]):
            objectPosition = i

    # errors in input (validation)

    # there is a second word but it is not found in the list
    if(_object != '' and objectPosition == 0):
        message = "that's silly"

    # no second word
    if(_object == ''):
        message = "I need two words"

    # doesnt have verb but does have _object
    if(verbPosition == 0 and objectPosition > 0):
        message = "you can't " + query

    # doesn't have either words
    if(verbPosition == 0 and objectPosition == 0):
        message = "you don't make sense"

    # it has verb and _object but is not carrying _object
    if(verbPosition > 0 and objectPosition > 0 and carrying[objectPosition] == 0):
        message = "you don't have " + _object

    # SPECIAL FLAGGED CONDITIONS

    if(flag[26] == 1 and room == 13 and (random.randint(1, 4) != 3) and verbPosition != 21):
        message = "bat's attacking"
        batsAttacking()

    # cobwebbt room, vacuum cleaner off, set ghosts to 1
    if(room == 44 and random.randint(1, 2) == 1 and flag[24] != 1):
        flag[27] = 1

    # candle is lit, decrement light limit
    if(flag[0] == 1):
        LL = LL - 1

    # if light limit is zero or less turn off candle
    if(LL < 1):
        flag[0] = 0

    # branch according to verbs

    if verbPosition == 1:
        wordsIKnow()  # 500
    if verbPosition == 2:
        inventory()  # 570
    if verbPosition == 3:
        go()  # 640
    if verbPosition == 4:
        go()  # 640
    if verbPosition == 5:
        go()  # 640
    if verbPosition == 6:
        go()  # 640
    if verbPosition == 7:
        go()  # 640
    if verbPosition == 8:
        go()  # 640
    if verbPosition == 9:
        go()  # 640
    if verbPosition == 10:
        get()  # 980
    if verbPosition == 11:
        get()  # 980 (take)
    if verbPosition == 12:
        open()  # 1030 ?
    if verbPosition == 13:
        examine()  # 1070
    if verbPosition == 14:
        read()  # 1140
    if verbPosition == 15:
        say()  # 1180
    if verbPosition == 16:
        dig()  # 1220
    if verbPosition == 17:
        swing()  # 1250
    if verbPosition == 18:
        climb()  # 1300
    if verbPosition == 19:
        light()  # 1340
    if verbPosition == 20:
        unlight()  # 1380
    if verbPosition == 21:
        spray()  # 1400
    if verbPosition == 22:
        use()  # 1430
    if verbPosition == 23:
        unlock()  # 1460
    if verbPosition == 24:
        leave()  # 1490
    if verbPosition == 25:
        score()  # 1510
    if verbPosition == 26:
        pass  # 1590

    if(LL == 10):
        message = "You're candle is waning"

    if(LL == 1):
        message = "You're candle is out"
# start again goto 90
