from random import randint
from maps import *
from rooms import *

#################
death_messages = [
    "You fell into the pit. The pit was not surprised.",
    "The trap was here before you. It will be here after you.",
    "You walked north into certain death. Bold directional choice.",
    "The dungeon has claimed another offering. It is pleased.",
    "You found the kill room. Achievement unlocked, ironically.",
    "The floor gave way. Floors do that sometimes. Especially this one.",
    "You touched the rotten wood. It had one job and so did you.",
    "The well shaft says hello from the bottom.",
    "That was the Trap room. The name was a hint.",
    "You have been absorbed into the dungeon's collection.",
    "The crypt floor opened up. Crypts do that. It's their thing.",
    "You stepped on the loose slab. It was very clearly loose.",
    "Congratulations on finding the secret room. It was a kill room.",
    "The dungeon has been fed. It will sleep well tonight.",
    "You died. The key is still on the rack, judging you.",
    "The pit was dark. You were in it. That's the whole story.",
    "Your torch went out at the worst possible moment.",
    "You tried to cross without the key. The gate remained unimpressed.",
    "The old well is now your permanent address.",
    "You entered the Undertow Pit. The name had 'pit' in it.",
    "Death by architecture. A classic.",
    "The dungeon has filed you under 'former adventurers.'",
    "You are now one with the cobblestones. They are honored.",
    "The rope was right there. You did not use the rope.",
    "You went west into the Pit. East was also an option.",
    "The rotting floorboards have claimed another brave soul.",
    "You found the secret passage. It found you first.",
    "The chest was locked. The pit was not.",
    "Your map-reading skills need some posthumous improvement.",
    "You went north when every instinct should have said south.",
    "The dungeon keeps your gear as a souvenir.",
    "You have been added to the Bell Tower's body count.",
    "The iron gate did not move. Neither will you, ever again.",
    "You discovered the hidden room. It killed you. Still counts.",
    "The crypt reclaims what the crypt is owed.",
    "You ran out of dungeon before you ran out of bad decisions.",
    "The underground temple found your offering acceptable.",
    "You ignored the cracked floor. The cracked floor did not ignore you.",
    "Death by curiosity. The dungeon respects the hustle.",
    "You have been promoted from adventurer to permanent fixture.",
    "The altar stood in silence. You did not.",
    "Without the key, the locked room wins. The locked room won.",
    "The shaft below the well was longer than expected. Much longer.",
    "You found every trap in the dungeon. Sequentially.",
    "The dungeon is a puzzle. You were a piece that didn't fit.",
    "There was a note in the library. You did not read it.",
    "The hidden chamber hid from you by killing you.",
    "Your adventure has been archived in the dungeon's memory.",
    "You fell through the Trapdoor. It's called a Trapdoor for a reason.",
    "The observatory will remember you as 'the one who didn't make it.'",
    "The dungeon floor accepted your challenge and your life.",
    "You walked into the room labeled 'kill.' Respect the labeling system.",
    "The rusty weapons on the wall were more dangerous than they looked.",
    "Your torch illuminated exactly one fatal mistake.",
    "The crown sits uncollected. So do your bones.",
    "You found the shortcut. It went straight down.",
    "The dungeon was designed by someone who did not like adventurers.",
    "You ran out of exits at the wrong moment.",
    "The star charts remain unfound. So do you.",
    "The apple in the pantry outlived you. A moment of silence.",
    "You picked the wrong door in the Junction. The Junction is unmoved.",
    "The narrow stairs twisted upward. You twisted downward.",
    "The chapel altar did not grant miracles today.",
    "You went west into the well shaft. East existed.",
    "The dungeon accepted your gear as tribute. You were the tribute.",
    "Death found you faster than the exit did.",
    "The loose floor slab has a long and distinguished history of this.",
    "You discovered that 'secret' and 'safe' are different words.",
    "The Pit says it enjoyed your visit. Please don't come back.",
    "You have been filed under 'reasons this dungeon has a reputation.'",
    "You went deeper. The dungeon went deeper faster.",
    "The rotten wood bridge had one job. So did you.",
    "The dungeon locked the exit behind you. Metaphorically.",
    "You were so close to the observatory. It was watching.",
    "The corridor ended abruptly. So did you.",
    "You took the scenic route. The scenic route killed you.",
    "The dungeon claps once, softly, for the effort.",
    "You needed the key. You had the torch. The torch was not the key.",
    "The gatehouse saw you arrive. The gatehouse did not see you leave.",
    "Death occurred in the Great Hall, which is neither great nor yours now.",
    "Your bones join the armory's collection. Unofficially.",
    "The kitchen was cold. The pit was colder.",
    "You found the locked door and then the kill room. Wrong order.",
    "The dungeon has many rooms. You found the worst one.",
    "The treasury is empty. So is your future.",
    "You fell. The dungeon does not issue refunds.",
    "The reaper got your coordinates from the trap.",
    "You entered the crypt uninvited. It responded in kind.",
    "The hidden passage was hidden for a reason.",
    "You solved the navigation puzzle incorrectly and fatally.",
    "The dungeon's trap count is now one higher. You helped.",
    "You ran out of 'go north' options at an inopportune time.",
    "The ancient stones have seen many adventurers. One more now.",
    "You unlocked the wrong room at the wrong moment.",
    "The dungeon gave you a torch and a key. You needed both. You used neither.",
    "A lesser dungeon might feel bad about this. This one does not.",
    "The note in the library would have been helpful. Too late now.",
    "You made it further than some. Not far enough for all.",
    "The dungeon floor: 1. Your continued existence: 0.",
    "The underground holds your secret now. Permanently.",
    "Here lies a brave explorer. The dungeon sends no condolences."]
#COLORS
bg_black   = "\033[40m"
bg_red     = "\033[41m"
bg_green   = "\033[42m"
bg_yellow  = "\033[43m"
bg_blue    = "\033[44m"
bg_magenta = "\033[45m"
bg_cyan    = "\033[46m"
bg_white   = "\033[47m"
black   = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
reset = "\033[0m"
#################

class Player:
    def __init__(self, name=None, items=None, current_room=None, map=None, start_room = None):

        if items is None:
            items = []
        self.items = items
        self.name = name if name is not None else ""
        self.current_room = current_room if current_room is not None else room0
        self.map = map if map is not None else map1()
        self.start_room = start_room

    def take_item(self, item):
        self.items.append(item)
        print(f"you took the {blue}{item}{reset}")

    def die(self):
        print(f"{red}you died{yellow}\n{death_messages[randint(0, len(death_messages) - 1)]}{reset}\n")
        self.current_room = self.start_room
        self.enter_room("n")


    def enter_room(self, new_room_direction):
        new_room = self.current_room.mapping[new_room_direction]
        print(f"{bg_white}{black}{new_room.name}{reset}")
        print(f"{yellow}{new_room.story}{reset}")
        if new_room.win:
            return True
        #this way, the final room cant be locked
        if len(new_room.mapping) > 0:
            print(f"you can go {blue}{', '.join(new_room.mapping.keys())}{reset}")
        if new_room.kill:
            return "die"
        if len(new_room.items) > 0:
            print(f"there is a {blue}{' ,'.join(new_room.items)}{reset}")
        if new_room.secret:
            print("there is a secret")
        if new_room.locked:
            print("the room is locked, you need a key to unlock it")
            while new_room.locked:
                if "key" in self.items:
                    use_question = input(f"you have a key. do you want to use it? {blue}[y]{reset} or {blue}[n]{reset}\n>")
                    if use_question == "y":
                        self.items.remove("key")
                        new_room.locked = False
                        self.current_room = new_room
                        print("you entered the room")
                        return "goon"

                    elif use_question == "n":
                        return "goon"
                    else: print(f"type {blue}[y]{reset} or{blue} [n]{reset}")
                else:
                    print("you don't have a key!")
                    return "goon"
        self.current_room = new_room
        return "goon"


    def player_action(self):
        while True:
            action_input = input("what do you want to do?\n>")

            if len(action_input.split(" ")) == 1:
                if action_input == "craft":
                    print("craft here")
                elif action_input == "exit":
                    print(f"{bg_red}{black}EXIT GAME{reset}")
                    return "exit"
                elif action_input == "help":
                    print(f"you can do:\n{green}go {yellow}<direction>\n{green}take {yellow}<item> \n{green}show {yellow}inv / map / secret \n{green}exit{reset}")
                else: print(f"{red}invalid input {yellow}use help for help{reset}")

            elif len(action_input.split(" ")) == 2:
                verb, noun = action_input.lower().split(" ")
                if len(verb) > 0 and len(noun) > 0:
                    if verb == "go":
                        if noun[0] in self.current_room.mapping.keys():
                            return noun
                        else: print(f"{red}you can't go {blue}{noun},{red} you can go {blue}{', '.join(self.current_room.mapping.keys())}{reset}")
                    elif verb == "take":
                        if noun in self.current_room.items:
                            self.current_room.items.remove(noun)
                            self.take_item(noun)
                            return "goon"
                        else: print(f"{red}there is no {blue}{noun}{red} to take{reset}")
                    elif verb == "show":
                        if noun == "inv":
                            print(f"you have: {', '.join(self.items)}")
                            return "goon"
                        elif noun == "map":
                            return "map"
                        elif noun == "secret":
                            if self.current_room.secret == True:
                                return "minigame"
                            else: print(f"{yellow}There is no secret in this room{reset}")
                        else: print(f"{red}there is no {blue} {noun} {red}to show, you can show {blue}inv {red}or {blue}map{reset}")
                    else: print(f"{red}invalid input {yellow}use help for help{reset}")

            else: print(f"{red}please use the correct format{reset}")


def mini_game():
    print("you can play a minigame!")
    random = int(input("[1] or [2]?\n>"))# only until second minigame is implemented
    if random == 1:
        print(f"you have to guess the number! Its between 1 and 100. You have 5 tries")
        random_number = randint(1, 100)
        count = 4
        while count >= 0:
            try:
                guess = int(input(f"your guess\n>"))
            except ValueError:
                print(f"{red}Wrong input{reset}")
            else:
                if guess == random_number:
                    print(f"{blue}Minigame WON!{reset}")
                    return "miniwon"
                else:
                    print(f"You guessed wrong, {blue}{count}{reset} tries left")
                    if guess > random_number:
                        print(f"{blue}the number is smaller{reset}")
                    elif guess < random_number:
                        print(f"{blue}the number is bigger{reset}")
                    count = count-1
        print(f"{red}Minigame LOST{reset}")
        print(f"the number was:{blue} {random_number}{reset}")
        return "minilost"

    elif random == 2:
        print("minigame 2 - always win")
        return "miniwon"
    else:
        print("wrong input")# only until second minigame is implemented
        return "minilost"

def display_map(maps):
    room_name = player1.current_room.name[:4]
    for row in maps:
        for cell in row:
            if room_name in cell:
                print(f"{bg_yellow}{room_name}{reset}", end="")
            else:
                print(cell, end="")
        print()

def game_map():

    maps = {
        "0": {"map": None, "room": room_test_0, "return": "goon", "print": "You chose Map 0: The short test"},
        "1": {"map": map1(), "room": room0, "return": "goon", "print": "You chose the testing Map"},
        "2": {"map": map2(), "room": room2_0, "return": "goon", "print": "You chose Map 2: The Ruined Castle"},
        "3": {"map": map3(), "room": room3_0, "return": "goon", "print": "You chose Map 3: The Drowned Abbey of Tides"},
        "4": {"map": map4(), "room": room4_0, "return": "goon", "print": "You chose Map 4: The Clockwork Keep of Brass"},
        "5": {"map": map5(), "room": room5_0, "return": "goon", "print": "You chose Map 5: The Forsaken Watchtower"},
        "6": {"map": map6(), "room": room6_0, "return": "goon", "print": "You chose Map 6: The Sunken Crypt of Embers"}
    }

    while True:
        map_input = input(f"""
Which map do you want to play?
    {blue}[0] {reset} test_short
    {blue}[1] {reset} test_long
    {blue}[2] {reset} The Ruined Castle
    {blue}[3] {reset} The Drowned Abbey of Tides
    {blue}[4] {reset} The Clockwork Keep of Brass
    {blue}[5] {reset} The Forsaken Watchtower
    {blue}[6] {reset} The Sunken Crypt of Embers
>""")
        if map_input in maps:
            room_dict = maps[map_input]
            player1.map = room_dict["map"]
            player1.current_room = player1.start_room = room_dict["room"]
            print(room_dict["print"])
            return room_dict["return"]
        else: print(f"{yellow}choose one of the options{reset}")

def game():
    map_output = game_map()
    print(f"{green}use {blue}help {green}to show commands{reset}")
    if map_output == "goon":
        player1.enter_room("n")
        output = player1.player_action()
        while True:
            if output[0] in player1.current_room.mapping.keys():
                output = player1.enter_room(output[0])
            if output is True:
                print(f"{bg_yellow}{black}YOU WON!{reset}")
                break
            if output == "minigame":
                minigame = mini_game()
                if minigame == "miniwon":
                    output = player1.player_action()
                elif minigame == "minilost":
                    output = player1.player_action()
            elif output == "goon":
                output = player1.player_action()
            elif output == "die":
                player1.die()
                output = player1.player_action()
            elif output == "map":
                if player1.map is not None:
                    display_map(player1.map)
                    output = player1.player_action()
                else:
                    print(f"{yellow}there is no map to show{reset}")
                    output = player1.player_action()
            elif output == "exit":
                game()
                return "exit"
            elif output == "unfinished":
                print(f"{red}unfinished element{reset}")
                break
            else: print("wrong return statement")
    elif map_output == "unfinished":
        print(f"{red}unfinished element{reset}")

if __name__ == "__main__":
    player1 = Player()
    game()
