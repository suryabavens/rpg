#!/bin/python3
from typing import List, Any


def show_instructions():
    # main menu and instruction
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')


inventory = []
rooms1 = { 'kitchen' : { 'north' : 'hall' , 'pan' : 'item1' }, 'hall' : {'south' : 'kitchen' , 'chair' : 'item1' }}
currentRoom = 'hall'


def show_status():
    # display current position and inventory
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))


show_instructions()

# loop forever
while True:

    show_status()

    # get the player's next 'move'
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms1[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms1[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if move[1] in rooms1[currentRoom].keys():  # and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms1[currentRoom][move[1]]
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
