from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
def try_direction(player, direction):
    
    """
    args: player and direction
    returns: none
    """

    # check the players current location to see if there is a room in the 
    # specified direction 
    # if there is a room move player to that room
    # otherwise print('not moveable')
    attribute = direction + '_to'

    # USE 'hasattr' to check if a class has an attribute
    if hasattr(player.current_room, attribute):
        # valid direction
        # use getattr to fetch the value associated with the attrb
        # update player's current room with fetched room 
        player.current_room = getattr(player.current_room, attribute)

    else:
        print("Wrong direction!")


# Make a new player object that is currently in the 'outside' room.
 
player = Player(room['outside'])


# Write a loop that:
while True:
    #
    # * Prints the current room name
    print('\n')
    print(player.current_room)


    # * Prints the current description (the textwrap module might be useful here).
    def print_wrapped_lines(value = player.current_room.description):
        """
        args: room desciption
        returns: description spaced by 50 widths 
        """
        wrapper = textwrap.TextWrapper(width = 50)
        word_list = wrapper.wrap(text = value)

        for element in word_list:
            return element
    # * Waits for user input and decides what to do.
    # strip off everything but the first char 
    command = input("\nCommand: ").strip().lower().split()
    command = command[0]
    # command = command_command[0]

    commands = ['n','s','e','w']

    if command == "q":
        break 
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    # user can enter 'north, south, east, or west"
    # or any of "n,s,e,w" to move 
    else:
        if command in commands:
            # move to north 
            try_direction(player, command)

