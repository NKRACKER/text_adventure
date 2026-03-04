from random import randint
from maps import *
from rooms import *

#################
death_messages = [
    "You died. Bold strategy.",
    "Well, that ended terribly.",
    "You are now deceased. Reviews are mixed.",
    "Death has claimed you. It seemed excited.",
    "Game over. The universe remains unconcerned.",
    "You have died. The floor sends its regards.",
    "Congratulations, you found the lose condition.",
    "You are dead. That was embarrassingly fast.",
    "Your adventure has been canceled due to a fatal error.",
    "You died exactly as the prophecy predicted: badly.",
    "Your health reached zero and kept going out of spite.",
    "You have been removed from the living playerbase.",
    "You died. The enemy is trying not to laugh.",
    "Your journey ends here, mostly because you did.",
    "You are no longer adventuring. You are decor.",
    "You died. Even the tutorial is disappointed.",
    "That looked survivable from a distance.",
    "You have been promoted to cautionary tale.",
    "You died. The checkpoint is judging you silently.",
    "Your last idea has been voted worst idea of the week.",
    "You are dead. Physics wins again.",
    "The reaper has added you to his frequent flyer program.",
    "You died. In hindsight, that was the trap.",
    "Your character has stopped being biologically ambitious.",
    "You have perished. Style points were not enough.",
    "Death was not on your to-do list, yet here we are.",
    "You died. The wall accepted your challenge.",
    "Your plan was clever, right up until reality arrived.",
    "You are dead. The loot was not worth it.",
    "That enemy would like to thank you for the free confidence boost.",
    "You died. The ground remains undefeated.",
    "Your bones have filed a formal complaint.",
    "You have fallen in battle, or at least in a direction.",
    "Death has occurred. Please update your strategy.",
    "You are now haunting this save file.",
    "You died. The soundtrack tried its best.",
    "Your final move was very memorable to the witnesses.",
    "You have ceased operations.",
    "You died. The monster barely had to commit.",
    "Your adventure is over. Please enjoy this complimentary regret.",
    "You have been outlived by your own bad decisions.",
    "You died. Nature is healing.",
    "The dungeon appreciates your donation of gear.",
    "You are dead. That lever was not decorative.",
    "Your story ends here with a wet crunch.",
    "You died. The laws of consequences remain in effect.",
    "Fatal mistake detected. User error confirmed.",
    "You are now one with the cobblestones.",
    "You died. The trap was older and wiser than you.",
    "Your hit points have entered the afterlife.",
    "You have died. The enemy calls this 'light exercise.'",
    "The void accepts your application.",
    "You died. Curiosity was not the only thing killed.",
    "You have been professionally defeated.",
    "You died. The barrel was, in fact, explosive.",
    "Your overconfidence has achieved terminal velocity.",
    "You are dead. The sign did say 'Do not touch.'",
    "You have reached the end of your warranty.",
    "You died. Your inventory survives you.",
    "That was less heroism and more immediate consequences.",
    "You have been flattened, folded, and emotionally humbled.",
    "You died. The boss rated your attempt 2 out of 10.",
    "Your adventure has been paused indefinitely by death.",
    "You died. The bridge disagreed with your weight distribution.",
    "You are dead. The lava remains extremely committed to being lava.",
    "Your final thought was probably not useful.",
    "You have perished. At least it was educational for someone else.",
    "You died. The goblin will be talking about this for weeks.",
    "Your body has left the chat.",
    "You are now an example in somebody else's safety lecture.",
    "You died. The chest was hungrier than expected.",
    "Your tactical genius has been postponed until next life.",
    "You have been defeated by basic cause and effect.",
    "You died. The universe rolled a natural nope.",
    "Your adventure has concluded with maximum oof.",
    "You are dead. Turns out, gravity had hands.",
    "You died. The skeleton found that hilarious.",
    "That button did exactly what it threatened to do.",
    "You have expired like a discount coupon.",
    "You died. The cliff was not bluffing.",
    "Your plan has been buried with you.",
    "You are dead. The game calls this a learning experience.",
    "You died. The fire considered you highly flammable.",
    "Your courage exceeded your life expectancy.",
    "You have been unsubscribed from existence.",
    "You died. Not even dramatically, just efficiently.",
    "Your life bar has resigned on ethical grounds.",
    "You are dead. The bees won.",
    "You have perished. The rat will now tell legends of this day.",
    "You died. The potion was not health-shaped.",
    "Your heroic sacrifice was mostly just sacrifice.",
    "You are no longer a problem for the enemy.",
    "You died. The darkness had hands.",
    "Your save file just sighed.",
    "You have been defeated by something that can't even open doors.",
    "You died. The banana peel sends no apologies.",
    "That went poorly in every available dimension.",
    "You are dead. The reaper gave you a little thumbs-up.",
    "You died. Please enjoy the silence of poor choices.",
    "Your adventure ended the way it was lived: suspiciously.",
    "You have fallen. Gracefully is not the word.",
    "You died. The narrator would like a quick word about impulse control.",
    "Here lies your hero. Cause of death: advanced nonsense."]
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
        self.name = name if not None else ""
        self.current_room = current_room if not None else room0
        self.map = map if not None else map1()
        self.start_room = start_room

    def take_item(self, item):
        self.items.append(item)
        print(f"you took the {blue}{item}{reset}")

    def die(self):
        print(f"{red}you died{yellow}\n{death_messages[randint(0, 99)]}{reset}\n")
        self.current_room = self.start_room
        self.enter_room("n")


    def enter_room(self, new_room_direction):
        new_room = self.current_room.mapping[new_room_direction]
        print(f"{bg_white}{black}{new_room.name}{reset}")
        print(f"{yellow}{new_room.story}{reset}")
        if len(new_room.mapping) > 0:
            print(f"you can go {blue}{', '.join(new_room.mapping.keys())}{reset}")
        if new_room.kill:
            return "die"
        if len(new_room.items) > 0 or None:
            print(f"there is a {blue}{' ,'.join(new_room.items)}{reset}")
        if new_room.secret:
            print("there is a secret, but you cant do anything by now, because this feature isn't implemented yet")
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
        if new_room.win:
            return "win"

        self.current_room = new_room

        return "goon"


    def player_action(self):
        while True:
            action_input = input("what do you want to do?\n>")

            if len(action_input.split(" ")) == 1:
                if action_input == "craft":
                    print("craft here")
                elif action_input == "help":
                    print(f"you can do:\n{green}go {yellow}<direction>\n{green}take {yellow}<item> \n{green}show {yellow}inv / map{reset}")
                else: print(f"{red}invalid input {yellow}use help for help{reset}")

            elif len(action_input.split(" ")) == 2:
                verb, noun = action_input.lower().split(" ")
                if len(verb) and len(noun) > 0:
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
                            print(', '.join(self.items))
                            return "goon"
                        elif noun == "map":
                            return "map"
                        else: print(f"{red}there is no {blue} {noun} {red}to show, you can show {blue}inv {red}or {blue}map{reset}")
                    else: print(f"{red}invalid input {yellow}use help for help")

            else: print(f"{red}please use the correct format{reset}")


def game_map():
    while True:
        map_input = input(f"Which map do you want to play?{blue} [1]{reset} or {blue}[2]{reset} or {blue}[3]{reset} or {blue}[4]{reset} or {blue}[5]{reset}\n>")
        if map_input == "1":
            print(f"You chose the testing Map")
            player1.map = map1()
            player1.current_room =  player1.start_room = room0
            return "goon"
        elif map_input == "2":
            print(f"You chose Map 2: The Chapel of the Ruined Court")
            player1.map = map2()
            player1.current_room = player1.start_room = room2_0
            return "goon"
        elif map_input == "3":
            print(f"You chose Map 3: The Citadel of Broken Towers")
            player1.map = map3()
            player1.current_room = player1.start_room = room3_0
            return "goon"
        elif map_input == "4":
            print(f"You chose Map 4: The Crownkeep of Falling Paths")
            player1.map = map4()
            player1.current_room = player1.start_room = room4_0
            return "goon"
        elif map_input == "5":
            print(f"You chose Map 5: The Labyrinth of Falling Ash")
            player1.map = map5()
            player1.current_room = player1.start_room = room5_0
            return "goon"
        else:
            print(f"{yellow}choose one of the options{reset}")


def game():
    if game_map() == "goon":
        player1.enter_room("n")
        output = player1.player_action()

        while True:
            if output == "goon":
                output = player1.player_action()
            elif output[0] in player1.current_room.mapping.keys():
                output = player1.enter_room(output[0])
            elif output == "die":
                player1.die()
                output = player1.player_action()
            elif output == "map":
                print(player1.map)
                output = player1.player_action()
            elif output == "win":
                print(f"{bg_blue}{yellow}YOU WON!{reset}")
            else: print("wrong return statement")


player1 = Player()
game()
