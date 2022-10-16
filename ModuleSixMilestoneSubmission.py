# Christopher Carlson-Estes
# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.

# Sys allows for an exit to work that is acceptable for use.
# Numpy allows for fancy indexing to allow only certain directions to be
import sys
import numpy as np
import random

# I added directions to the definitions to check if action can be performed in that room.
rooms = {
        'Bedroom': {'south': 'North Gallery Hall', 'South': 'North Gallery Hall', 'S': 'North Gallery Hall',
                    's': 'North Gallery Hall', '': '', 'text': 'As you close the door behind you you hear the howl '
                         'of wind and the rustling of trees. You hope this noise doesn'"'"'t '
                         'mask something more sinister'},
        'North Gallery Hall': {'north': 'Bedroom', 'North': 'Bedroom', 'N': 'Bedroom', 'n': 'Bedroom',
                               'south': 'Gallery', 'South': 'Gallery', 'S': 'Gallery', 's': 'Gallery',
                               'east': 'North Hall', 'East': 'North Hall', 'E': 'North Hall', 'e': 'North Hall',
                               'west': 'Apothecary', 'West': 'Apothecary', 'W': 'Apothecary', 'w': 'Apothecary',
                               '': '', 'text': 'You hear the crash of thunder outside. The flashes of shadows it '
                                               'creates give you no comfort.'},
        'North Hall': {'east': 'Kitchen', 'East': 'Kitchen', 'E': 'Kitchen', 'e': 'Kitchen',
                       'south': 'East Gallery Hall', 'South': 'East Gallery Hall', 'S': 'East Gallery Hall',
                       's': 'East Gallery Hall', 'west': 'North Gallery Hall', 'West': 'North Gallery Hall',
                       'W': 'North Gallery Hall', 'w': 'North Gallery Hall', '': '', 'text': 'Silhouettes that you'
                            ' once knew appear strange and abstract. The smell of potash and chlorine waft through the '
                            'air.'},
        'Kitchen': {'south': 'Courtyard', 'South': 'Courtyard', 'S': 'Courtyard', 's': 'Courtyard',
                    'west': 'North Hall', 'West': 'North Hall', 'W': 'North Hall', 'w': 'North Hall', '': '',
                    'text': 'You look at the bottles of strong drink longingly. '
                            'Surely a drink now would spell the end of you.'},
        'Apothecary': {'south': 'Library', 'South': 'Library', 'S': 'Library', 's': 'Library',
                                'east': 'North Gallery Hall', 'East': 'North Gallery Hall', 'E': 'North Gallery Hall',
                       'e': 'North Gallery Hall', 'west': 'Garret', 'West': 'Garret', 'W': 'Garret', 'w': 'Garret',
                       '': '', 'text': 'Tinctures and baubles flicker in the candlelight. Ingredients strewn across '
                                       'the tables.', 'item': 'Mortar and Pestle'},
        'Garret': {'east': 'Apothecary', 'East': 'Apothecary', 'E': 'Apothecary', 'e': 'Apothecary', '': '',
                   'text': 'The winding steps lead up to a dark and musty attic, boxes stacked precariously against '
                           'the walls. You hear rain clattering against the roof.', "item": 'Beeswax Candle'},
        'Library': {'north': 'Apothecary', 'North': 'Apothecary', 'N': 'Apothecary', 'n': 'Apothecary',
                    'east': 'West Gallery Hall', 'East': 'West Gallery Hall', 'E': 'West Gallery Hall',
                    'e': 'West Gallery Hall', 'south': 'Cellar', 'South': 'Cellar', 'S': 'Cellar', 's': 'Cellar',
                    '': '', 'text': 'Books line the walls, stretching up to the arched ceiling.',
                    'item': 'Ophanims Index'},
        'West Gallery Hall': {'east': 'Gallery', 'East': 'Gallery', 'E': 'Gallery', 'e': 'Gallery', 'west': 'Library',
                              'West': 'Library', 'W': 'Library', 'w': 'Library', '': '', 'text': 'The hall is lined '
                                      'with seating, though you haven'"'"'t had a guest in ages. The smell of potash '
                                      'and chlorine waft through the air.'},
        'Gallery': {'north': 'North Gallery Hall', 'North': 'North Gallery Hall', 'N': 'North Gallery Hall',
                    'n': 'North Gallery Hall', 'east': 'East Gallery Hall', 'East': 'East Gallery Hall',
                    'E': 'East Gallery Hall', 'e': 'East Gallery Hall', 'south': 'South Gallery Hall',
                    'South': 'South Gallery Hall', 'S': 'South Gallery Hall', 's': 'South Gallery Hall',
                    'west': 'West Gallery Hall', 'West': 'West Gallery Hall', 'W': 'West Gallery Hall',
                    'w': 'West Gallery Hall', '': '', 'text': 'Paintings and tapestries line the walls of the '
                                                              'centerpiece of this grand home. All is in order except '
                                                              'for the one empty space...', 'item': 'Ancient Dagger'},
        'East Gallery Hall': {'north': 'North Hall', 'North': 'North Hall', 'N': 'North Hall', 'n': 'North Hall',
                              'east': 'Courtyard', 'East': 'Courtyard', 'E': 'Courtyard', 'e': 'Courtyard',
                              'south': 'South Hall', 'South': 'South Hall', 'S': 'South Hall', 's': 'South Hall',
                              'west': 'Gallery', 'West': 'Gallery', 'W': 'Gallery', 'w': 'Gallery', '': '',
                              'text': 'Ah, the beautiful entrance to your home. It used to feel so welcoming. Now the'
                                      ' smell of potash and chlorine waft through the air.'},
        'Courtyard': {'north': 'Kitchen', 'North': 'Kitchen', 'N': 'Kitchen', 'n': 'Kitchen',
                      'west': 'East Gallery Hall', 'West': 'East Gallery Hall', 'W': 'East Gallery Hall',
                      'w': 'East Gallery Hall', '': '', 'text': 'Flower beds line the sides of the crumbling '
                                                                'cobblestone walkway that flows around an ancient '
                                                                'Elm Tree', 'item': 'Elm Bark'},
        'Cellar': {'north': 'Library', 'North': 'Library', 'N': 'Library', 'n': 'Library', 'east': 'South Gallery Hall',
                   'East': 'South Gallery Hall', 'E': 'South Gallery Hall', 'e': 'South Gallery Hall', '': '',
                   'text': 'Dark and dank. The musty smell of petrichor and dry rot permeate the air. '
                           'A tall armoire stands across from you.', 'item': 'Obsidian Goblet'},
        'South Gallery Hall': {'north': 'Gallery', 'North': 'Gallery', 'N': 'Gallery', 'n': 'Gallery',
                               'east': 'South Hall', 'East': 'South Hall', 'E': 'South Hall', 'e': 'South Hall',
                               'south': 'Conservatory', 'South': 'Conservatory', 'S': 'Conservatory',
                               's': 'Conservatory', 'west': 'Cellar', 'West': 'Cellar', 'W': 'Cellar', 'w': 'Cellar',
                               '': '', 'text': 'Some gardening tools lean against the walls of this quaint hallway. '
                                               'You feel calm... for a moment. '},
        'South Hall': {'north': 'East Gallery Hall', 'North': 'East Gallery Hall', 'N': 'East Gallery Hall',
                       'n': 'East Gallery Hall', 'west': 'South Gallery Hall', 'West': 'South Gallery Hall',
                       'W': 'South Gallery Hall', 'w': 'South Gallery Hall', '': '', 'text': 'You can see the courtyard'
                                                                                             ' through the towering '
                                                                                             'glass windows. The smell '
                                                                                             'of potash and chlorine '
                                                                                             'waft through the air.'},
        'Conservatory': {'north': 'South Gallery Hall', 'North': 'South Gallery Hall', 'N': 'South Gallery Hall',
                         'n': 'South Gallery Hall', '': '', 'text': 'Greenery surrounds you, as if mother nature '
                                                                    'herself is giving you comfort. The air is warm '
                                                                    'even though the sun has been down for many '
                                                                    'hours.', 'item': 'Amorpha fructosia'},
        'Exit': {'Exit'}
    }
# These check to see if the input is valid.
actions = ['north', 'North', 'N', 'n', 'east', 'East', 'E', 'e', 'south', 'South', 'S', 's', 'west', 'West', 'W', 'w',
           'wait', 'Wait', 'observe', 'Observe', 'obs', 'Obs']
endGame = ['Exit', 'exit', 'Quit', 'quit', 'e', 'E']
current_room = 'North Gallery Hall'
inventory = []
wait = ['wait', 'Wait', 'observe', 'Observe', 'obs', 'Obs']
search_listY = ['Yes', 'Y', 'yes', 'y']
search_listN = ['No', 'N', 'no', 'n']
# Defining the input loop. Using 'actions' lets me have space for other actions I want...
# to add such as waiting and searching.


def intro():
    print('     Welcome to Aberrant Effigy.\n_____________________________________\nIn this game you will explore a '
          'mansion while an unspeakable horror walks the halls. \nIf you have the misfortune of encountering that... '
          'that thing before you know how to banish it your fate is surely sealed. \nYou must go to your library and '
          'use Ophanims Index to determine exactly how to dispose of this other worldly horror.\nYou can get to the '
          'library through the Apothecary, just west of you.')


def player_status():
    print('\n\n\nYou enter the ' + current_room + '.')
    if len(inventory) > 0:
        print('You are carrying' + str(inventory) + '.\n')
    else:
        print('Your night robe is light and the pockets empty.\n')


def monster_status():
    y = random.randint(0, 3)
    potential_rooms = ['West Gallery Hall', 'East Gallery Hall', 'South Hall', 'North Hall']
    monster_room = potential_rooms[y]
    return monster_room


def fight():
    print('It is upon you!\n')
    if len(inventory) > 6:
        print('It has been banished.')
        sys.exit('You win.')
    else:
        print('You have ceased to exist on this plane of reality')
        sys.exit('You lose.')


def search_library():
    answer = input('Would you like to search the Library?: ')
    if answer in search_listY:
        print('You have obtained ' + rooms[current_room]['item'])
        inventory.append(rooms[current_room]['item'])
        del (rooms[current_room]['item'])
        return input_request()
    elif answer in search_listN:
        pass
    else:
        print('Please type yes or no.')
        return search_library()


def search():
    answer = input('The index is warm to the touch. Would you like to search the room?: ')
    if answer in search_listY:
        print('You have obtained the ' + rooms[current_room]['item'])
        inventory.append(rooms[current_room]['item'])
        print(inventory)
        del (rooms[current_room]['item'])
        return input_request()
    elif answer in search_listN:
        pass
    else:
        print('Please type yes or no.')
        return search()


def input_request():
    direction_list = np.array((list(rooms[current_room])))
    direction_printer = []
    if 'n' in direction_list:
        direction_printer = ' north'
    if 'e' in direction_list:
        if 'north' in direction_printer:
            direction_printer += ' or east'
        else:
            direction_printer += ' east'
    if 's' in direction_list:
        if 'east' or 'north' in direction_printer:
            direction_printer += ' or south'
        else:
            direction_printer += ' south'
    if 'w' in direction_list:
        if 'north' or 'east' or 'south' in direction_printer:
            direction_printer += ' or west'
        else:
            direction_printer += ' west'
    direction_printer = ''.join(direction_printer)
    print('You can go' + direction_printer + '.\nYou may also wait and observe your surroundings.\n')
    if 'item' in rooms[current_room]:
        if 'Ophanims Index' in inventory:
            search()
        elif current_room in 'Library':
            search_library()
        else:
            pass
    action = input('Type a direction or action:')
    if action in actions:
        if action in wait:
            print(rooms[current_room]['text'])
            return current_room
        elif action in rooms[current_room]:
            room = rooms[current_room][action]
            print(action + rooms[current_room][action])
            return room
        else:
            if action not in rooms[current_room]:
                print('You walk face first into a wall. Try a different direction.')
                return input_request()
    elif action in endGame:
        sys.exit('You Quitter!')
    else:
        print("Its really simple. Type a DIRECTION or ACTION. Maybe you can""'""t spell?\n")
        return input_request()


intro()


while True:
    if current_room in 'Exit':
        sys.exit('You Quitter!')
    else:
        monster_status()
        player_status()
        current_room = input_request()
        if monster_status() is current_room:
            fight()
