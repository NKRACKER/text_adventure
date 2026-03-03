

class Room:
    def __init__(self, mapping=None,locked=False,kill=False,secret=False,items=None,name="",story=""):
        self.mapping = mapping if mapping is not None else {}
        self.locked = locked
        self.kill = kill
        self.secret = secret
        self.items = items if items is not None else []
        self.name = name
        self.story = story

#################
#ROOMS_1
room0 = Room()
room1 = Room(name="Room 1\n")
room2 = Room(kill=True, name="Room 2\n")
room3 = Room(secret=True,name="Room 3\n")
room4 = Room(name="Room4")
room5 = Room(items=["key"],name="Room 5\n")
room6 = Room(kill=True,name="Room 6\n")
room7 = Room(locked=True,name="Room 7\n")
room8 = Room(name="Room 8\n")
room9 = Room(secret=True,name="Room 9\n")
room10 = Room(name="Room 10\n")
room11 = Room(name="you fall though a trapdoor\n")
room12 = Room(secret=True,name="Room 12\n")
room13 = Room(name="Room 13\n")
#MAPPING_1
room0.mapping = {"n" :room1}
room1.mapping = {"e": room2, "w": room3}
room2.mapping = None
room3.mapping = {"e": room1, "n": room4}
room4.mapping = {"n": room7, "e": room5, "s": room3, "w": room6}
room5.mapping = {"w": room4}
room6.mapping = None
room7.mapping = {"n": room8, "s": room4}
room8.mapping = {"n": room9, "e": room10}
room9.mapping = {"s" :room8}
room10.mapping = {"s" :room5, "e": room1, "n": room12, "w": room8}
room11.mapping = {"n": room1}
room12.mapping = {"w": room9, "e": room13, "s": room10}
room13.mapping = None
#################
#ROOMS_2
room2_0 = Room(
    name="[0] Gatehouse",
    story="Cold air comes through the broken gate."
)
room2_1 = Room(
    name="[1] Entry Court",
    story="Weeds grow between cracked stones."
)
room2_2 = Room(
    name="[2] Well Shaft",
    story="You step onto rotten wood covering an old well.",
    kill=True
)
room2_3 = Room(
    name="[3] Great Hall",
    story="Dusty banners hang from the ceiling."
)
room2_4 = Room(
    name="[4] Library",
    story="Collapsed shelves lean against the walls.",
    items=["note"]
)
room2_5 = Room(
    name="[5] Armory",
    story="Rusty weapons line the walls. A small key glints on a rack.",
    items=["key"]
)
room2_6 = Room(
    name="[6] Kitchen",
    story="Cold ovens and broken tables fill the room.",
    items=["torch"]
)
room2_7 = Room(
    name="[7] Pantry",
    story="A hidden little storage room. Somehow, one apple survived.",
    items=["apple"],
    secret=True
)
room2_8 = Room(
    name="[8] Chapel",
    story="A cracked altar stands in silence."
)
room2_9 = Room(
    name="[9] Servants' Stairs",
    story="Narrow stone stairs twist upward."
)
room2_10 = Room(
    name="[10] Iron Gate",
    story="A heavy iron gate blocks the path north.",
    locked=True
)
room2_11 = Room(
    name="[11] Crypt",
    story="A loose floor slab gives way beneath you.",
    kill=True
)
room2_12 = Room(
    name="[12] Treasury",
    story="Old chests lie open. On a pedestal rests a crown.",
    items=["crown"]
)
room2_13 = Room(
    name="[13] Bell Tower",
    story="A massive bell hangs above. Wind whistles through the cracks.",
    items=["rope"]
)
room2_14 = Room(
    name="[14] Observatory",
    story="A hidden chamber under the roof with faded star charts.",
    items=["chart"],
    secret=True
)
#MAPPINGS_2

room2_0.mapping = {
    "n": room2_1
}
room2_1.mapping = {
    "s": room2_0,
    "n": room2_3,
    "e": room2_4,
    "w": room2_2
}
room2_2.mapping = None
room2_3.mapping = {
    "s": room2_1,
    "w": room2_5,
    "e": room2_6,
    "n": room2_8
}
room2_4.mapping = {
    "w": room2_1,
    "n": room2_6
}
room2_5.mapping = {
    "e": room2_3
}
room2_6.mapping = {
    "w": room2_3,
    "s": room2_4,
    "n": room2_9
}
room2_7.mapping = {
    "w": room2_9
}
room2_8.mapping = {
    "s": room2_3,
    "n": room2_10,
    "e": room2_9
}
room2_9.mapping = {
    "s": room2_6,
    "w": room2_8,
    "e": room2_7,
    "n": room2_13
}
room2_10.mapping = {
    "s": room2_8,
    "w": room2_11,
    "e": room2_13,
    "n": room2_12
}
room2_11.mapping = None
room2_12.mapping = {
    "s": room2_10,
    "e": room2_14
}
room2_13.mapping = {
    "s": room2_9,
    "w": room2_10,
    "n": room2_14
}
room2_14.mapping = {
    "s": room2_13,
    "w": room2_12
}
#################
#ROOMS_3
room3_0 = Room(
    name="[0] Outer Gate",
    story="Broken banners hang over the ruined entrance."
)
room3_1 = Room(
    name="[1] Courtyard",
    story="Rainwater gathers between cracked stones in the open court."
)
room3_2 = Room(
    name="[2] Guard Post",
    story="A narrow watch post overlooks the eastern path."
)
room3_3 = Room(
    name="[3] Stables",
    story="Rotten wood and scattered hay fill the abandoned stables."
)
room3_4 = Room(
    name="[4] Main Hall",
    story="A broad hall opens before you, lined with worn pillars."
)
room3_5 = Room(
    name="[5] Collapsed Bridge",
    story="You step onto loose stone and the bridge gives way beneath you.",
    kill=True
)
room3_6 = Room(
    name="[6] Armory",
    story="Rusted blades and broken shields cover the walls. A key lies in the dust.",
    items=["key"]
)
room3_7 = Room(
    name="[7] Hidden Pantry",
    story="A cramped secret room stocked long ago. One apple somehow survived.",
    items=["apple"],
    secret=True
)
room3_8 = Room(
    name="[8] West Corridor",
    story="A dim corridor stretches along the western side of the fortress."
)
room3_9 = Room(
    name="[9] Kitchen",
    story="Cold ovens and cracked tables suggest this place has been dead for years.",
    items=["torch"]
)
room3_10 = Room(
    name="[10] Bronze Gate",
    story="A tall bronze gate blocks the northern passage.",
    locked=True
)
room3_11 = Room(
    name="[11] Chapel Ruin",
    story="Broken stone benches face a shattered altar."
)
room3_12 = Room(
    name="[12] Storage Room",
    story="Dusty crates are stacked to the ceiling."
)
room3_13 = Room(
    name="[13] Bell Passage",
    story="A narrow passage echoes with the distant groan of hanging metal."
)
room3_14 = Room(
    name="[14] Upper Crossing",
    story="Several upper paths connect here above the main fortress."
)
room3_15 = Room(
    name="[15] Furnace Pit",
    story="The floor is thin with ash. One more step sends you into the glowing pit.",
    kill=True
)
room3_16 = Room(
    name="[16] Gallery",
    story="Faded portraits stare at you from cracked golden frames."
)
room3_17 = Room(
    name="[17] Tower Stairs",
    story="A spiral staircase winds through cold stone."
)
room3_18 = Room(
    name="[18] Workshop",
    story="Old tools lie scattered across benches. Another key rests beside a vice.",
    items=["key"]
)
room3_19 = Room(
    name="[19] Mural Chamber",
    story="Ancient wall paintings shimmer beneath layers of dust.",
    items=["gem"],
    secret=True
)
room3_20 = Room(
    name="[20] North Walk",
    story="A high outer walkway circles the northern edge of the fortress."
)
room3_21 = Room(
    name="[21] Crossroads",
    story="Four paths split here, each darker than the last."
)
room3_22 = Room(
    name="[22] Silver Gate",
    story="A silver-plated gate seals the eastern ascent.",
    locked=True
)
room3_23 = Room(
    name="[23] Archive",
    story="Bundles of ruined parchment crumble on long stone desks.",
    items=["note"]
)
room3_24 = Room(
    name="[24] Map Room",
    story="A torn map of the fortress lies spread across a cracked table.",
    items=["map"]
)
room3_25 = Room(
    name="[25] Abyss Crack",
    story="The floor splits open into darkness. There is no time to stop falling.",
    kill=True
)
room3_26 = Room(
    name="[26] High Terrace",
    story="Wind tears through the open terrace high above the ruins."
)
room3_27 = Room(
    name="[27] East Tower",
    story="This lonely tower leans slightly, but still stands."
)
room3_28 = Room(
    name="[28] Observatory",
    story="A hidden chamber beneath the roof holds faded star charts.",
    items=["chart"],
    secret=True
)
room3_29 = Room(
    name="[29] Throne Vault",
    story="At the end of the fortress, a forgotten crown rests beneath a beam of pale light.",
    items=["crown"]
)
#MAPPINGS_3

room3_0.mapping = {
    "n": room3_1
}
room3_1.mapping = {
    "s": room3_0,
    "n": room3_4,
    "e": room3_2,
    "w": room3_3
}
room3_2.mapping = {
    "w": room3_1,
    "e": room3_5,
    "n": room3_6
}
room3_3.mapping = {
    "e": room3_1,
    "w": room3_7,
    "n": room3_8
}
room3_4.mapping = {
    "s": room3_1,
    "n": room3_10,
    "e": room3_6,
    "w": room3_8
}
room3_5.mapping = None
room3_6.mapping = {
    "s": room3_2,
    "w": room3_4,
    "e": room3_9
}
room3_7.mapping = {
    "e": room3_3
}
room3_8.mapping = {
    "s": room3_3,
    "e": room3_4,
    "n": room3_11
}
room3_9.mapping = {
    "w": room3_6,
    "n": room3_12,
    "e": room3_13
}
room3_10.mapping = {
    "s": room3_4,
    "n": room3_14
}
room3_11.mapping = {
    "s": room3_8,
    "e": room3_14,
    "w": room3_15
}
room3_12.mapping = {
    "s": room3_9,
    "n": room3_16
}
room3_13.mapping = {
    "w": room3_9,
    "n": room3_17,
    "e": room3_18
}
room3_14.mapping = {
    "s": room3_10,
    "w": room3_11,
    "e": room3_16,
    "n": room3_20
}
room3_15.mapping = None
room3_16.mapping = {
    "w": room3_14,
    "s": room3_12,
    "e": room3_17,
    "n": room3_21
}
room3_17.mapping = {
    "w": room3_16,
    "s": room3_13,
    "e": room3_19
}
room3_18.mapping = {
    "w": room3_13,
    "e": room3_22
}
room3_19.mapping = {
    "w": room3_17,
    "n": room3_23
}
room3_20.mapping = {
    "s": room3_14,
    "w": room3_24,
    "e": room3_21
}
room3_21.mapping = {
    "w": room3_20,
    "s": room3_16,
    "e": room3_23,
    "n": room3_26
}
room3_22.mapping = {
    "w": room3_18,
    "n": room3_27
}
room3_23.mapping = {
    "w": room3_21,
    "s": room3_19,
    "e": room3_25
}
room3_24.mapping = {
    "e": room3_20,
    "n": room3_28
}
room3_25.mapping = None
room3_26.mapping = {
    "s": room3_21,
    "w": room3_28,
    "e": room3_27,
    "n": room3_29
}
room3_27.mapping = {
    "w": room3_26,
    "s": room3_22
}
room3_28.mapping = {
    "e": room3_26,
    "s": room3_24
}
room3_29.mapping = {
    "s": room3_26
}
#################
#ROOMS_4
room4_0 = Room(
    name="[0]Ruined Gate",
    story="A shattered gate leans inward, as if the fortress is already swallowing you."
)
room4_1 = Room(
    name="[1] Echo Court",
    story="Your footsteps return from the wet stone walls a moment too late."
)
room4_2 = Room(
    name="[2] West Watch",
    story="A narrow guard platform overlooks a collapsed yard."
)
room4_3 = Room(
    name="[3] East Watch",
    story="Arrow slits look out over broken walls and thorny rubble."
)
room4_4 = Room(
    name="[4] Hall of Flags",
    story="Rotten banners hang from beams blackened by smoke."
)
room4_5 = Room(
    name="[5] Barracks",
    story="Old bunks rot quietly in the dark."
)
room4_6 = Room(
    name="[6] Mess Hall",
    story="Long tables sit crooked beneath a ceiling stained by time."
)
room4_7 = Room(
    name="[7] Shrine of Rain",
    story="Water drips through a crack in the roof onto a worn stone altar."
)
room4_8 = Room(
    name="[8] Moss Slide",
    story="A steep, slime-covered chute drops into darkness. Once you commit, there is no elegant comeback."
)
room4_9 = Room(
    name="[9] Armory",
    story="Rusted spears and broken armor fill the chamber. A key lies beneath a dented shield.",
    items=["key"]
)
room4_10 = Room(
    name="[10] Archive",
    story="Rows of moldy records sag in leaning shelves.",
    items=["map"]
)
room4_11 = Room(
    name="[11] Scriptorium",
    story="A hidden writing room survives behind a warped panel. A note waits on a tilted desk.",
    items=["note"],
    secret=True
)
room4_12 = Room(
    name="[12] Broken Gallery",
    story="Cracked portraits and fallen frames litter a long upper gallery."
)
room4_13 = Room(
    name="[13] Lower Junction",
    story="Passages branch away in all directions through damp stone."
)
room4_14 = Room(
    name="[14] Trapdoor Hall",
    story="The floor ahead is treacherous. One section looks a little too neat. A little too trapdoor-y."
)
room4_15 = Room(
    name="[15] Smithy",
    story="Cold anvils and cracked furnaces fill the forge. Another key glints in a bed of ash.",
    items=["key"]
)
room4_16 = Room(
    name="[16] Reservoir Walk",
    story="A narrow walkway curves along a deep black reservoir."
)
room4_17 = Room(
    name="[17] Flooded Cellar",
    story="You arrive in ankle-deep water beneath broken beams. The chute above offers no return.",
    items=["torch"]
)
room4_18 = Room(
    name="[18] Old Dock",
    story="A rotten wooden dock juts over dark water. A rope hangs from a post.",
    items=["rope"]
)
room4_19 = Room(
    name="[19] Chain Lift",
    story="A hulking iron lift hangs motionless, frozen between levels."
)
room4_20 = Room(
    name="[20] North Cloister",
    story="A silent corridor wraps around a dead inner garden."
)
room4_21 = Room(
    name="[21] Water Channel",
    story="Fast water surges through a stone channel. Step wrong and the current chooses for you."
)
room4_22 = Room(
    name="[22] Bone Pit",
    story="You land among old bones and snapped planks. The trapdoor above is far beyond practical discussion."
)
room4_23 = Room(
    name="[23] Fungus Garden",
    story="Pale fungus glows faintly between broken stones."
)
room4_24 = Room(
    name="[24] Deep Chapel",
    story="A buried chapel survives below the main halls, lit only by a seam of green light."
)
room4_25 = Room(
    name="[25] Cracked Ledge",
    story="A narrow ledge crumbles beneath your boots. One route forward looks less like a path and more like a bad decision with momentum."
)
room4_26 = Room(
    name="[26] Treasury Gate",
    story="A heavy bronze gate bars the way deeper into the fortress.",
    locked=True
)
room4_27 = Room(
    name="[27] Treasury Antechamber",
    story="Dusty statues stand guard before the inner vault."
)
room4_28 = Room(
    name="[28] Treasury Vault",
    story="Coins are long gone, but a crown still rests on a stone pedestal.",
    items=["crown"]
)
room4_29 = Room(
    name="[29] Bell Stairs",
    story="A spiraling stair rises through the tower beside a hanging bell."
)
room4_30 = Room(
    name="[30] Drain Tunnel",
    story="You are spat from the water channel into a foul drainage passage."
)
room4_31 = Room(
    name="[31] Ash Slope",
    story="You slide down loose ash and shattered stone onto a lower path."
)
room4_32 = Room(
    name="[32] Forge Bridge",
    story="A chained bridge crosses a fiery split in the fortress floor.",
    locked=True
)
room4_33 = Room(
    name="[33] Magma Gallery",
    story="Heat pulses through cracks in the walls like the fortress still has a heartbeat."
)
room4_34 = Room(
    name="[34] Observatory Stairs",
    story="Steep stairs climb toward the upper towers."
)
room4_35 = Room(
    name="[35] Star Chamber",
    story="A circular room under a broken dome holds faded charts of the night sky.",
    items=["chart"],
    secret=True
)
room4_36 = Room(
    name="[36] East Tower",
    story="Wind pushes through the tower's empty windows."
)
room4_37 = Room(
    name="[37] Warden Gate",
    story="An iron gate with a massive lock guards the inner keep.",
    locked=True
)
room4_38 = Room(
    name="[38] Warden Keep",
    story="This grim chamber once housed the fortress commander."
)
room4_39 = Room(
    name="[39] Throne of Dust",
    story="A cracked stone throne stands alone beneath torn banners."
)
room4_40 = Room(
    name="[40] Subterranean Lake",
    story="Black water stretches beneath the fortress like a second sky."
)
room4_41 = Room(
    name="[41] Prison Ring",
    story="Cells line a circular prison corridor, their doors hanging open."
)
room4_42 = Room(
    name="[42] Hidden Cache",
    story="A secret stash is tucked behind loose stones. Someone clearly planned ahead better than the rest of this place.",
    items=["key"],
    secret=True
)
room4_43 = Room(
    name="[43] Roof Walk",
    story="A narrow roof path skirts the upper edge of the fortress."
)
room4_44 = Room(
    name="[44] Beacon Peak",
    story="At the highest point of the ruins, a dead beacon tower overlooks the entire valley.",
    items=["gem"]
)
room4_45 = Room(
    name="[45] Poison Cistern",
    story="The fumes hit your lungs before your feet reach the bottom.",
    kill=True
)
room4_46 = Room(
    name="[46] Mirror Hall",
    story="Shattered mirrors reflect your torchlight into strange corners."
)
room4_47 = Room(
    name="[47] Hidden Reliquary",
    story="A secret chamber holds an old seal wrapped in brittle cloth.",
    items=["seal"],
    secret=True
)
room4_48 = Room(
    name="[48] Skybridge",
    story="The hanging bridge snaps behind you as you cross. Retreat is now a myth."
)
room4_49 = Room(
    name="[49] Execution Yard",
    story="The yard floor gives way beneath rotten timbers, and the fall is not negotiable.",
    kill=True
)
#MAPPINGS_4

room4_0.mapping = {
    "n": room4_1
}
room4_1.mapping = {
    "s": room4_0,
    "w": room4_2,
    "e": room4_3,
    "n": room4_4
}
room4_2.mapping = {
    "e": room4_1,
    "n": room4_5
}
room4_3.mapping = {
    "w": room4_1,
    "n": room4_6,
    "e": room4_10
}
room4_4.mapping = {
    "s": room4_1,
    "w": room4_5,
    "e": room4_6,
    "n": room4_7
}
room4_5.mapping = {
    "s": room4_2,
    "e": room4_4,
    "n": room4_9
}
room4_6.mapping = {
    "s": room4_3,
    "w": room4_4,
    "n": room4_10,
    "e": room4_12
}
room4_7.mapping = {
    "s": room4_4,
    "n": room4_20
}
# Einbahnweg: Rutsche
room4_8.mapping = {
    "s": room4_17
}
room4_9.mapping = {
    "s": room4_5,
    "e": room4_15
}
room4_10.mapping = {
    "s": room4_6,
    "w": room4_3,
    "e": room4_11,
    "n": room4_19
}
room4_11.mapping = {
    "w": room4_10
}
room4_12.mapping = {
    "w": room4_46,
    "s": room4_13,
    "n": room4_14,
    "e": room4_8
}
room4_13.mapping = {
    "n": room4_12,
    "w": room4_15,
    "e": room4_16,
    "s": room4_23
}
# Einbahnweg: Falltür nach Süden
room4_14.mapping = {
    "w": room4_24,
    "e": room4_29,
    "s": room4_22
}
room4_15.mapping = {
    "w": room4_9,
    "e": room4_13,
    "s": room4_17
}
room4_16.mapping = {
    "w": room4_13,
    "n": room4_18,
    "s": room4_45
}
room4_17.mapping = {
    "n": room4_15,
    "e": room4_18,
    "w": room4_30
}
room4_18.mapping = {
    "w": room4_17,
    "s": room4_16,
    "n": room4_21,
    "e": room4_41
}
room4_19.mapping = {
    "s": room4_10,
    "e": room4_20,
    "n": room4_29
}
room4_20.mapping = {
    "s": room4_7,
    "w": room4_19,
    "e": room4_26,
    "n": room4_34
}
# Einbahnweg: Wasserstrom nach Osten
room4_21.mapping = {
    "s": room4_18,
    "n": room4_26,
    "e": room4_30
}
room4_22.mapping = {
    "e": room4_23,
    "s": room4_30,
    "w": room4_42
}
room4_23.mapping = {
    "n": room4_13,
    "w": room4_22,
    "e": room4_24,
    "s": room4_31
}
room4_24.mapping = {
    "e": room4_20,
    "s": room4_23,
    "w": room4_25,
    "n": room4_46
}
# Einbahnweg: bröckelnde Kante nach Osten
room4_25.mapping = {
    "n": room4_32,
    "e": room4_31
}
room4_26.mapping = {
    "w": room4_20,
    "s": room4_21,
    "e": room4_27
}
room4_27.mapping = {
    "w": room4_26,
    "n": room4_28,
    "e": room4_36
}
room4_28.mapping = {
    "s": room4_27
}
room4_29.mapping = {
    "s": room4_19,
    "w": room4_14,
    "e": room4_32
}
room4_30.mapping = {
    "n": room4_31,
    "e": room4_17,
    "s": room4_40
}
room4_31.mapping = {
    "n": room4_23,
    "e": room4_33,
    "s": room4_40
}
room4_32.mapping = {
    "w": room4_29,
    "s": room4_25,
    "n": room4_33,
    "e": room4_37
}
room4_33.mapping = {
    "w": room4_31,
    "s": room4_32,
    "n": room4_39
}
room4_34.mapping = {
    "s": room4_20,
    "n": room4_35,
    "e": room4_43
}
room4_35.mapping = {
    "s": room4_34,
    "e": room4_47
}
room4_36.mapping = {
    "w": room4_27,
    "n": room4_37
}
room4_37.mapping = {
    "s": room4_36,
    "n": room4_38,
    "w": room4_32
}
room4_38.mapping = {
    "s": room4_37,
    "e": room4_39
}
room4_39.mapping = {
    "s": room4_33,
    "w": room4_38,
    "n": room4_44
}
room4_40.mapping = {
    "n": room4_31,
    "e": room4_41,
    "w": room4_42
}
room4_41.mapping = {
    "w": room4_18,
    "s": room4_40,
    "n": room4_43,
    "e": room4_49
}
room4_42.mapping = {
    "e": room4_40
}
room4_43.mapping = {
    "w": room4_34,
    "s": room4_41,
    "n": room4_44,
    "e": room4_48
}
room4_44.mapping = {
    "s": room4_43,
    "w": room4_39
}
room4_45.mapping = None
room4_46.mapping = {
    "s": room4_24,
    "e": room4_12
}
room4_47.mapping = {
    "w": room4_35
}
# Einbahnweg: Hängebrücke bricht, nur noch nach Süden weiter
room4_48.mapping = {
    "s": room4_44
}
room4_49.mapping = None
#################
#ROOMS_5
room5_0 = Room(
    name="[0] Drowned Gate",
    story="Black water drips from the broken gate stones."
)
room5_1 = Room(
    name="[1] Echo Vestibule",
    story="Every step returns from the walls half a second too late."
)
room5_2 = Room(
    name="[2] West Breach",
    story="A jagged breach in the wall opens into older masonry."
)
room5_3 = Room(
    name="[3] East Breach",
    story="The eastern wall has split open into a maze of passages."
)
room5_4 = Room(
    name="[4] Hall of Splinters",
    story="Broken beams and old banner poles cover the floor."
)
room5_5 = Room(
    name="[5] Ivy Court",
    story="A roofless court lies buried under wet ivy and pale roots."
)
room5_6 = Room(
    name="[6] Guard Barracks",
    story="Rotted bunks line the walls, and a key lies under a rusted helmet.",
    items=["key"]
)
room5_7 = Room(
    name="[7] Cross Chapel",
    story="Four cracked aisles meet beneath a shattered dome."
)
room5_8 = Room(
    name="[8] Scriptorium",
    story="Ink-stained desks sit beneath shelves of ruined parchment.",
    items=["note"]
)
room5_9 = Room(
    name="[9] Moss Slide",
    story="The floor tilts into a slime-slick chute with no dignified way back."
)
room5_10 = Room(
    name="[10] Broken Switchyard",
    story="Narrow corridors fork here like snapped tracks."
)
room5_11 = Room(
    name="[11] Thorn Maze",
    story="Root-thick walls divide the room into cramped turns."
)
room5_12 = Room(
    name="[12] Cloister Turn",
    story="A bent cloister passage curls around old stone supports."
)
room5_13 = Room(
    name="[13] False Reliquary",
    story="A hidden niche holds an old seal wrapped in brittle cloth.",
    secret=True,
    items=["seal"]
)
room5_14 = Room(
    name="[14] Sinkhole Mouth",
    story="The cracked floor gives way into a deep dark shaft.",
    kill=True
)
room5_15 = Room(
    name="[15] West Gallery",
    story="A long western gallery overlooks lower ruins through broken arches."
)
room5_16 = Room(
    name="[16] Split Stair",
    story="One staircase climbs, another falls, and neither looks trustworthy."
)
room5_17 = Room(
    name="[17] Rope Bridge",
    story="A swaying rope bridge stretches over a black drop."
)
room5_18 = Room(
    name="[18] Iron Lattice",
    story="An iron lattice gate bars the upper western route.",
    locked=True
)
room5_19 = Room(
    name="[19] Old Well Walk",
    story="A circular ledge wraps around a dry stone well."
)
room5_20 = Room(
    name="[20] East Arcade",
    story="Tall arches frame a damp and unusually cold arcade.",
    items=["map"]
)
room5_21 = Room(
    name="[21] Watchman's Loop",
    story="A looping patrol path circles above the eastern halls."
)
room5_22 = Room(
    name="[22] Dust Gallery",
    story="Every surface here is buried under a thick gray dust."
)
room5_23 = Room(
    name="[23] Bent Archive",
    story="Tilted shelves bend under the weight of dead records."
)
room5_24 = Room(
    name="[24] Brass Locker",
    story="A brass locker stands open, and inside lies another key.",
    items=["key"]
)
room5_25 = Room(
    name="[25] Needle Passage",
    story="The walls squeeze inward until the corridor becomes a slit."
)
room5_26 = Room(
    name="[26] Hidden Cell",
    story="A concealed stone cell sits behind a seam in the wall.",
    secret=True
)
room5_27 = Room(
    name="[27] Bronze Portcullis",
    story="A bronze portcullis blocks the way into the northern fortress.",
    locked=True
)
room5_28 = Room(
    name="[28] Rain Terrace",
    story="Rain blows through open stone ribs onto the terrace floor."
)
room5_29 = Room(
    name="[29] East Tower Foot",
    story="The base of a leaning tower opens into several dangerous routes."
)
room5_30 = Room(
    name="[30] Water Gate",
    story="Dark water presses behind old sluice machinery."
)
room5_31 = Room(
    name="[31] Poison Drain",
    story="The fumes here hit harder than any blade.",
    kill=True
)
room5_32 = Room(
    name="[32] Flood Sump",
    story="You arrive in a flooded basin fed by channels from above."
)
room5_33 = Room(
    name="[33] Pump Room",
    story="Old pumps and wheels surround a dry platform. A key sits beside a valve.",
    items=["key"]
)
room5_34 = Room(
    name="[34] Ashen Landing",
    story="A gray landing of soot and grit spreads out under a broken vault."
)
room5_35 = Room(
    name="[35] Mirror Corridor",
    story="Cracked mirrors distort every torchlight reflection into movement."
)
room5_36 = Room(
    name="[36] North Bastion",
    story="A cold bastion chamber opens into the fortress's upper ring."
)
room5_37 = Room(
    name="[37] Ash Chute",
    story="Loose ash slides down a steep chute toward red-lit depths."
)
room5_38 = Room(
    name="[38] Shattered Dome",
    story="The dome floor has collapsed into jagged emptiness.",
    kill=True
)
room5_39 = Room(
    name="[39] Sluice Crossing",
    story="A narrow crossing hangs above churning dark channels."
)
room5_40 = Room(
    name="[40] Black Stair",
    story="A broad staircase rises through stone blackened by old smoke."
)
room5_41 = Room(
    name="[41] Sunken Hall",
    story="A half-submerged hall lies deep below the eastern routes."
)
room5_42 = Room(
    name="[42] Cistern Junction",
    story="Several wet passages meet around a cracked cistern mouth."
)
room5_43 = Room(
    name="[43] Trap Stair",
    story="A crooked stair climbs into darkness and looks suspiciously one-way."
)
room5_44 = Room(
    name="[44] Furnace Gate",
    story="A heavy furnace gate seals the red-lit quarter of the ruin.",
    locked=True
)
room5_45 = Room(
    name="[45] Ember Walk",
    story="Heat breathes through the walls along this glowing stone walk."
)
room5_46 = Room(
    name="[46] Chain Crossing",
    story="Iron chains creak above a deep furnace trench."
)
room5_47 = Room(
    name="[47] Clock Loft",
    story="A dead clock mechanism fills the loft. A key lies in the gears.",
    items=["key"]
)
room5_48 = Room(
    name="[48] Skybridge",
    story="A high open bridge stretches into freezing wind."
)
room5_49 = Room(
    name="[49] High Post",
    story="A lonely stone post looks down over half the labyrinth."
)
room5_50 = Room(
    name="[50] North Gallery",
    story="The northern gallery bends around the keep like a stone rib."
)
room5_51 = Room(
    name="[51] Warden's Route",
    story="This stern corridor once belonged to the fortress wardens."
)
room5_52 = Room(
    name="[52] Guillotine Floor",
    story="The floor plate drops away the moment weight settles on it.",
    kill=True
)
room5_53 = Room(
    name="[53] Whisper Niche",
    story="A hidden niche murmurs with drafts from unseen cracks.",
    secret=True,
    items=["gem"]
)
room5_54 = Room(
    name="[54] Red Ramp",
    story="A red-stained ramp climbs through furnace-heated stone."
)
room5_55 = Room(
    name="[55] Smuggler Den",
    story="A hidden den is tucked behind loose stones, and another key was left here.",
    secret=True,
    items=["key"]
)
room5_56 = Room(
    name="[56] Bone Gallery",
    story="Dry bones and collapsed rails line this grim side gallery."
)
room5_57 = Room(
    name="[57] Fallen Choir",
    story="Broken choir stalls lie scattered beneath a fractured arch."
)
room5_58 = Room(
    name="[58] Silver Seal",
    story="A silver-bound gate guards the inner sanctum.",
    locked=True
)
room5_59 = Room(
    name="[59] Bell Furnace",
    story="An enormous cracked furnace stands below a hanging bell frame."
)
room5_60 = Room(
    name="[60] King's Span",
    story="A broad span links the red quarter to the upper royal routes."
)
room5_61 = Room(
    name="[61] Wind Spiral",
    story="A spiraling passage coils upward through violent drafts."
)
room5_62 = Room(
    name="[62] Ice Balcony",
    story="Cold air gathers on this exposed balcony high above the ruin."
)
room5_63 = Room(
    name="[63] Crown Approach",
    story="The stone ahead grows smoother and more deliberate. A final key glints in the dust.",
    items=["key"]
)
room5_64 = Room(
    name="[64] Outer Ledge",
    story="A narrow ledge clings to the exterior wall of the fortress."
)
room5_65 = Room(
    name="[65] Banner Run",
    story="Torn war banners whip along a long open corridor."
)
room5_66 = Room(
    name="[66] Warden Gate",
    story="An iron gate with a massive lock bars the last wardens' path.",
    locked=True
)
room5_67 = Room(
    name="[67] Maw Stair",
    story="The stair bends like a throat around a black central shaft."
)
room5_68 = Room(
    name="[68] Ash Vault",
    story="Ash piles knee-high under a low cracked vault."
)
room5_69 = Room(
    name="[69] Hidden Observatory",
    story="A secret observatory waits behind the upper walls, holding old star charts.",
    secret=True,
    items=["chart"]
)
room5_70 = Room(
    name="[70] Inner Ring",
    story="The innermost ring of the fortress circles the final core."
)
room5_71 = Room(
    name="[71] Crown Engine",
    story="At the heart of the labyrinth stands a strange throne-machine, and on it rests a crown.",
    items=["crown"]
)
#MAPPINGS_5

room5_0.mapping = {
    "n": room5_1
}
room5_1.mapping = {
    "s": room5_0,
    "w": room5_2,
    "e": room5_3,
    "n": room5_4
}
room5_2.mapping = {
    "e": room5_1,
    "n": room5_5,
    "w": room5_10
}
room5_3.mapping = {
    "w": room5_1,
    "n": room5_6,
    "e": room5_20
}
room5_4.mapping = {
    "s": room5_1,
    "w": room5_5,
    "e": room5_6,
    "n": room5_7
}
room5_5.mapping = {
    "s": room5_2,
    "e": room5_4,
    "n": room5_11
}
room5_6.mapping = {
    "s": room5_3,
    "w": room5_4,
    "e": room5_8,
    "n": room5_21
}
room5_7.mapping = {
    "s": room5_4,
    "w": room5_11,
    "e": room5_21,
    "n": room5_12
}
room5_8.mapping = {
    "w": room5_6,
    "e": room5_22,
    "s": room5_3
}
# Einbahnstraße: aus room5_12 nach room5_9, dann runter in room5_32
room5_9.mapping = {
    "s": room5_32
}
room5_10.mapping = {
    "e": room5_2,
    "n": room5_15,
    "s": room5_19,
    "w": room5_14
}
room5_11.mapping = {
    "s": room5_5,
    "e": room5_7,
    "w": room5_13,
    "n": room5_16
}
room5_12.mapping = {
    "s": room5_7,
    "w": room5_16,
    "e": room5_9,
    "n": room5_23
}
room5_13.mapping = {
    "e": room5_11
}
room5_14.mapping = None
room5_15.mapping = {
    "s": room5_10,
    "e": room5_16,
    "n": room5_24
}
room5_16.mapping = {
    "w": room5_15,
    "e": room5_17,
    "s": room5_11,
    "n": room5_18
}
# Einbahnstraße: von room5_17 nach room5_27, aber kein Rückweg nach Westen
room5_17.mapping = {
    "w": room5_16,
    "e": room5_27
}
room5_18.mapping = {
    "s": room5_16,
    "n": room5_25,
    "e": room5_23
}
room5_19.mapping = {
    "n": room5_10,
    "e": room5_30
}
room5_20.mapping = {
    "w": room5_3,
    "n": room5_8,
    "e": room5_28,
    "s": room5_31
}
room5_21.mapping = {
    "s": room5_6,
    "w": room5_7,
    "e": room5_22,
    "n": room5_29
}
room5_22.mapping = {
    "w": room5_8,
    "e": room5_23,
    "s": room5_21,
    "n": room5_28
}
room5_23.mapping = {
    "w": room5_22,
    "s": room5_12,
    "e": room5_18,
    "n": room5_33
}
room5_24.mapping = {
    "s": room5_15,
    "e": room5_25,
    "n": room5_34,
    "w": room5_30
}
room5_25.mapping = {
    "w": room5_24,
    "n": room5_26,
    "e": room5_34,
    "s": room5_18
}
# Einbahnstraße: versteckte Zelle, kein Rückweg direkt nach Süden
room5_26.mapping = {
    "n": room5_35,
    "e": room5_53
}
room5_27.mapping = {
    "s": room5_34,
    "n": room5_36,
    "e": room5_29
}
room5_28.mapping = {
    "w": room5_20,
    "s": room5_22,
    "e": room5_29,
    "n": room5_37
}
room5_29.mapping = {
    "w": room5_28,
    "s": room5_21,
    "n": room5_38,
    "e": room5_36
}
room5_30.mapping = {
    "w": room5_19,
    "e": room5_24,
    "s": room5_32,
    "n": room5_39
}
room5_31.mapping = None
room5_32.mapping = {
    "e": room5_33,
    "w": room5_40,
    "s": room5_41
}
room5_33.mapping = {
    "w": room5_32,
    "s": room5_23,
    "e": room5_35,
    "n": room5_42
}
room5_34.mapping = {
    "w": room5_25,
    "s": room5_24,
    "n": room5_43,
    "e": room5_27
}
room5_35.mapping = {
    "w": room5_33,
    "s": room5_26,
    "e": room5_44,
    "n": room5_45
}
room5_36.mapping = {
    "w": room5_29,
    "s": room5_27,
    "e": room5_46,
    "n": room5_47
}
# Einbahnstraße: nach Norden in die rote Tiefe, kein Rückweg nach Süden
room5_37.mapping = {
    "s": room5_28,
    "e": room5_45,
    "n": room5_54
}
room5_38.mapping = None
room5_39.mapping = {
    "s": room5_30,
    "e": room5_50,
    "n": room5_40
}
room5_40.mapping = {
    "e": room5_32,
    "w": room5_39,
    "n": room5_51
}
# Einbahnstraße: room5_32 → room5_41, aber nicht zurück nach Norden
room5_41.mapping = {
    "e": room5_42,
    "w": room5_52,
    "s": room5_55
}
room5_42.mapping = {
    "w": room5_41,
    "s": room5_33,
    "e": room5_43,
    "n": room5_53
}
room5_43.mapping = {
    "w": room5_42,
    "s": room5_34,
    "e": room5_44,
    "n": room5_57
}
room5_44.mapping = {
    "w": room5_35,
    "s": room5_43,
    "e": room5_58,
    "n": room5_45
}
room5_45.mapping = {
    "w": room5_37,
    "s": room5_35,
    "e": room5_59,
    "n": room5_46
}
room5_46.mapping = {
    "w": room5_36,
    "s": room5_45,
    "e": room5_47,
    "n": room5_60
}
room5_47.mapping = {
    "w": room5_46,
    "s": room5_36,
    "e": room5_48,
    "n": room5_61
}
# Einbahnstraße: von room5_48 nach room5_49, kein Rückweg nach Westen
room5_48.mapping = {
    "w": room5_47,
    "e": room5_49,
    "s": room5_59
}
room5_49.mapping = {
    "n": room5_62,
    "s": room5_50,
    "e": room5_63
}
room5_50.mapping = {
    "w": room5_39,
    "n": room5_49,
    "s": room5_64,
    "e": room5_51
}
room5_51.mapping = {
    "w": room5_50,
    "s": room5_40,
    "e": room5_52,
    "n": room5_65
}
room5_52.mapping = None
room5_53.mapping = {
    "s": room5_42,
    "w": room5_55,
    "e": room5_54
}
room5_54.mapping = {
    "w": room5_53,
    "e": room5_56,
    "n": room5_66
}
room5_55.mapping = {
    "e": room5_53,
    "n": room5_67
}
room5_56.mapping = {
    "w": room5_54,
    "e": room5_57,
    "s": room5_68
}
# Einbahnstraße: von room5_43 nach room5_57, aber kein direkter Rückweg nach Süden
room5_57.mapping = {
    "w": room5_56,
    "e": room5_69,
    "n": room5_58
}
room5_58.mapping = {
    "w": room5_44,
    "s": room5_57,
    "e": room5_70,
    "n": room5_59
}
room5_59.mapping = {
    "w": room5_45,
    "n": room5_58,
    "s": room5_48,
    "e": room5_60
}
room5_60.mapping = {
    "w": room5_59,
    "s": room5_46,
    "e": room5_71,
    "n": room5_61
}
room5_61.mapping = {
    "s": room5_47,
    "w": room5_60,
    "n": room5_68,
    "e": room5_62
}
room5_62.mapping = {
    "w": room5_61,
    "s": room5_49,
    "e": room5_63,
    "n": room5_69
}
room5_63.mapping = {
    "w": room5_62,
    "s": room5_70,
    "n": room5_71
}
room5_64.mapping = {
    "n": room5_50,
    "e": room5_65
}
room5_65.mapping = {
    "w": room5_64,
    "s": room5_51,
    "e": room5_66
}
room5_66.mapping = {
    "w": room5_65,
    "s": room5_54,
    "n": room5_67,
    "e": room5_70
}
room5_67.mapping = {
    "s": room5_66,
    "w": room5_55,
    "e": room5_68,
    "n": room5_71
}
room5_68.mapping = {
    "s": room5_61,
    "w": room5_67,
    "e": room5_69,
    "n": room5_56
}
room5_69.mapping = {
    "s": room5_62,
    "w": room5_68,
    "e": room5_70
}
# Einbahnstraße: von room5_70 nach room5_71, aber nicht zurück nach Süden
room5_70.mapping = {
    "w": room5_69,
    "s": room5_63,
    "n": room5_71,
    "e": room5_58
}
room5_71.mapping = {
    "w": room5_63,
    "s": room5_67
}