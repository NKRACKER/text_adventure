class Room:
    def __init__(self, mapping=None, locked=False, kill=False,win=False, secret=False, items=None, name="", story=""):
        self.mapping = mapping if mapping is not None else {}
        self.locked = locked
        self.kill = kill
        self.secret = secret
        self.items = items if items is not None else []
        self.name = name
        self.story = story
        self.win = win


# ROOMS_short_TEST
room_test_0 = Room(name="0")
room_test_1 = Room(name="1")
room_test_2 = Room(name="2", secret=True)
#MAPPING_short_TEST
room_test_0.mapping = {"n": room_test_1}
room_test_1.mapping = {"n": room_test_2}
room_test_2.mapping = {}

#################
# ROOMS_1
room0 = Room(name="[00] Start")
room1 = Room(name="[01] Hall")
room2 = Room(kill=True, name="[02] Trap")
room3 = Room(secret=True, name="[03] Side Room")
room4 = Room(name="[04] Junction")
room5 = Room(items=["key"], name="[05] Key Room")
room6 = Room(kill=True,secret=True,name="[06] Pit")
room7 = Room(locked=True, name="[07] Lock")
room8 = Room(name="[08] Corridor")
room9 = Room(secret=True, name="[09] Hidden Room")
room10 = Room(name="[10] Upper Hall")
room11 = Room(name="[11] Trapdoor")
room12 = Room(secret=True, name="[12] Secret Hall")
room13 = Room(name="[13] Exit",story="you finally made it out of here", win = True)
# MAPPING_1
room0.mapping = {"n": room1}
room1.mapping = {"e": room2, "n": room3}
room2.mapping = {}
room3.mapping = {"n": room6, "e": room5, "s": room1}
room4.mapping = {"s": room5, "w": room6, "e": room7}
room5.mapping = {"w": room3, "e": room10, "n": room4, "s": room2}
room6.mapping = {"e": room4}
room7.mapping = {"s": room10, "n": room8, "e": room11, "w": room4}
room8.mapping = {"e": room9, "s": room7}
room9.mapping = {"w": room8, "s": room11}
room10.mapping = {"w": room5, "n": room7, "e": room12}
room11.mapping = {"w": room7, "e": room13, "n": room9}
room12.mapping = {"w": room10}
room13.mapping = {}

#################
# ROOMS_2
room2_0 = Room(name="[00] Gatehouse", story="Cold air comes through the broken gate.")
room2_1 = Room(name="[01] Entry Court", story="Weeds grow between cracked stones.")
room2_2 = Room(name="[02] Well Shaft", story="You step onto rotten wood covering an old well.", kill=True)
room2_3 = Room(name="[03] Great Hall", story="Dusty banners hang from the ceiling.")
room2_4 = Room(name="[04] Library", story="Collapsed shelves lean against the walls.", items=["note"])
room2_5 = Room(name="[05] Armory", story="Rusty weapons line the walls. A small key glints on a rack.", items=["key"])
room2_6 = Room(name="[06] Kitchen", story="Cold ovens and broken tables fill the room.", items=["torch"])
room2_7 = Room(name="[07] Pantry", story="A hidden little storage room. Somehow, one apple survived.", items=["apple"], secret=True)
room2_8 = Room(name="[08] Chapel", story="A cracked altar stands in silence.")
room2_9 = Room(name="[09] Servants' Stairs", story="Narrow stone stairs twist upward.")
room2_10 = Room(name="[10] Iron Gate", story="A heavy iron gate blocks the path north.", locked=True)
room2_11 = Room(name="[11] Crypt", story="A loose floor slab gives way beneath you.", kill=True)
room2_12 = Room(name="[12] Treasury", story="Old chests lie open. On a pedestal rests a crown.", items=["crown"])
room2_13 = Room(name="[13] Bell Tower", story="A massive bell hangs above. Wind whistles through the cracks.", items=["rope"])
room2_14 = Room(name="[14] Observatory",win = True, story="A hidden chamber under the roof with faded star charts.", items=["chart"], secret=True)
# MAPPINGS_2
room2_0.mapping = {"n": room2_1}
room2_1.mapping = {"n": room2_3, "e": room2_4, "w": room2_2}
room2_2.mapping = {}
room2_3.mapping = {"s": room2_1, "w": room2_5, "e": room2_6, "n": room2_8}
room2_4.mapping = {"w": room2_1, "n": room2_6, "e": room2_5}
room2_5.mapping = {"w": room2_4, "e": room2_3}
room2_6.mapping = {"w": room2_3, "s": room2_4, "n": room2_9, "e": room2_7}
room2_7.mapping = {"w": room2_6, "n": room2_13}
room2_8.mapping = {"s": room2_3, "n": room2_10, "e": room2_9}
room2_9.mapping = {"s": room2_6, "w": room2_8, "e": room2_13}
room2_10.mapping = {"s": room2_8, "w": room2_11, "e": room2_12}
room2_11.mapping = {}
room2_12.mapping = {"w": room2_10, "e": room2_14}
room2_13.mapping = {"s": room2_7, "w": room2_9, "n": room2_14}
room2_14.mapping = {"s": room2_13, "w": room2_12}

#################
#ROOMS_3
room3_0 = Room(
    name="[00] Tidal Gate",
    story="Sea water drips through the cracked threshold stones."
)
room3_1 = Room(
    name="[01] Lower Narthex",
    story="The old entrance hall smells of salt, wax, and mildew."
)
room3_2 = Room(
    name="[02] Undertow Pit",
    story="The floor gives way into a black shaft where water roars below.",
    kill=True
)
room3_3 = Room(
    name="[03] Cloister Walk",
    story="A narrow cloister path circles a drowned inner court."
)
room3_4 = Room(
    name="[04] Flooded Chapel",
    story="Rows of broken pews vanish beneath dark water."
)
room3_5 = Room(
    name="[05] Store Cellar",
    story="Old crates sag in the damp. A small iron key has not yet rusted away.",
    items=["key"]
)
room3_6 = Room(
    name="[06] Abbey Hall",
    story="A long hall of worn stone opens into several ruined wings."
)
room3_7 = Room(
    name="[07] Broken Nave",
    story="The central nave has partially collapsed, but a path still winds through it."
)
room3_8 = Room(
    name="[08] Scriptorium",
    story="Mold-eaten manuscripts cling to leaning shelves.",
    items=["note"]
)
room3_9 = Room(
    name="[09] Iron Choir",
    story="A rusted iron screen divides the old choir from the rest of the abbey."
)
room3_10 = Room(
    name="[10] Bell Landing",
    story="A narrow stone landing overlooks the ruined bell shaft."
)
room3_11 = Room(
    name="[11] Rope Loft",
    story="Ropes and pulleys hang from the rafters above the choir.",
    items=["rope"]
)
room3_12 = Room(
    name="[12] Upper Transept",
    story="Cold drafts move through the upper crossing of the abbey."
)
room3_13 = Room(
    name="[13] Sealed Reliquary",
    story="A heavy reliquary door bars the eastern shrine.",
    locked=True
)
room3_14 = Room(
    name="[14] Hidden Apse",
    story="A secret apse survives behind the reliquary wall.",
    secret=True,
    items=["chart"]
)
room3_15 = Room(
    name="[15] High Reliquary",
    story="A silver chest rests on a stone altar above the ruined transept.",
    items=["crown"],
    win=True
)
room3_16 = Room(
    name="[16] East Balcony",
    story="A narrow balcony peers into the drowned sanctuary.",
    items=["map"]
)
room3_17 = Room(
    name="[17] Font Passage",
    story="A passage of cracked basins and toppled fonts leads deeper east."
)
room3_18 = Room(
    name="[18] Quiet Dormitory",
    story="Dusty cots line the walls. The room feels strangely untouched.",
    items=["apple"]
)
#MAPPINGS_3
room3_0.mapping = {
    "n": room3_1
}
room3_1.mapping = {
    "w": room3_2,
    "n": room3_3
}
room3_2.mapping = {}
room3_3.mapping = {
    "s": room3_1,
    "e": room3_4,
    "n": room3_6
}
room3_4.mapping = {
    "w": room3_3,
    "n": room3_7
}
room3_5.mapping = {
    "e": room3_6,
    "s": room3_2
}
room3_6.mapping = {
    "w": room3_5,
    "e": room3_7,
    "s": room3_3,
    "n": room3_8
}
room3_7.mapping = {
    "w": room3_6,
    "e": room3_17,
    "s": room3_4,
    "n": room3_9
}
room3_8.mapping = {
    "s": room3_6,
    "e": room3_9,
    "n": room3_11
}
room3_9.mapping = {
    "w": room3_8,
    "e": room3_10,
    "s": room3_7,
    "n": room3_12
}
room3_10.mapping = {
    "w": room3_9,
    "s": room3_17,
    "n": room3_13
}
room3_11.mapping = {
    "e": room3_12,
    "s": room3_8
}
room3_12.mapping = {
    "w": room3_11,
    "e": room3_13,
    "s": room3_9,
    "n": room3_15
}
room3_13.mapping = {
    "w": room3_12,
    "e": room3_14,
    "s": room3_10
}
room3_14.mapping = {
    "w": room3_13,
    "s": room3_16
}
room3_15.mapping = {}
room3_16.mapping = {
    "n": room3_14,
    "s": room3_18
}
room3_17.mapping = {
    "w": room3_7,
    "e": room3_18,
    "n": room3_10
}
room3_18.mapping = {
    "w": room3_17,
    "n": room3_16
}

#################
#ROOMS_4
room4_0 = Room(
    name="[00] Intake Hatch",
    story="A round hatch opens into the lowest level of the machine-fortress."
)
room4_1 = Room(
    name="[01] Rust Foyer",
    story="Steam condenses on riveted walls and drops onto the metal floor."
)
room4_2 = Room(
    name="[02] Gear Hub",
    story="Huge gears grind somewhere behind the walls."
)
room4_3 = Room(
    name="[03] East Service",
    story="A narrow maintenance aisle runs beside old boilers."
)
room4_4 = Room(
    name="[04] West Service",
    story="A dim service corridor rattles whenever the fortress stirs."
)
room4_5 = Room(
    name="[05] Crusher Pit",
    story="The floor plate drops and crushing pistons slam down from above.",
    kill=True
)
room4_6 = Room(
    name="[06] Key Forge",
    story="A cold forge sits silent. A brass key rests in the ash.",
    items=["key"]
)
room4_7 = Room(
    name="[07] Outer Conveyor",
    story="An outer belt route circles the western machinery."
)
room4_8 = Room(
    name="[08] Piston Walk",
    story="Thick pistons rise and fall behind grated walls."
)
room4_9 = Room(
    name="[09] Tooth Corridor",
    story="The corridor bends around giant gear teeth."
)
room4_10 = Room(
    name="[10] Boiler Hall",
    story="Ancient boilers loom over a maze of pipes and catwalks."
)
room4_11 = Room(
    name="[11] West Rampart",
    story="A fortified metal ramp leads toward the upper works."
)
room4_12 = Room(
    name="[12] Conveyor Spine",
    story="A moving spine of belts and chains drives cargo eastward."
)
room4_13 = Room(
    name="[13] Ratchet Run",
    story="A ratcheting mechanism allows passage only one way.",
)
room4_14 = Room(
    name="[14] Brass Passage",
    story="Warm brass walls amplify every footstep into a metallic hum."
)
room4_15 = Room(
    name="[15] Turbine Stairs",
    story="A steep stair coils around a silent turbine shaft."
)
room4_16 = Room(
    name="[16] North Rampart",
    story="A broad armored walkway spans the northern face of the keep."
)
room4_17 = Room(
    name="[17] Governor Seal",
    story="A sealed security gate blocks the central upper route.",
    locked=True
)
room4_18 = Room(
    name="[18] Signal Bridge",
    story="A bridge of cables and signal lamps crosses the inner machinery."
)
room4_19 = Room(
    name="[19] Warden Rail",
    story="A narrow rail track leads toward the upper command vault."
)
room4_20 = Room(
    name="[20] Sky Intake",
    story="Cold air rushes through giant intake vanes overhead."
)
room4_21 = Room(
    name="[21] Hidden Control Room",
    story="A concealed maintenance station still holds faded schematics.",
    secret=True,
    items=["chart"]
)
room4_22 = Room(
    name="[22] Crown Rail",
    story="A polished rail line runs straight toward the central sanctum."
)
room4_23 = Room(
    name="[23] Clockwork Sanctum",
    story="At the top of the machine-fortress, a crown rests inside a ticking cage.",
    items=["crown"],
    win=True
)
#MAPPINGS_4
room4_0.mapping = {
    "n": room4_1
}
room4_1.mapping = {
    "w": room4_4,
    "e": room4_2,
    "n": room4_8
}
room4_2.mapping = {
    "w": room4_1,
    "e": room4_3,
    "n": room4_9,
    "s": room4_0
}
room4_3.mapping = {
    "w": room4_2,
    "n": room4_10,
    "s": room4_5
}
room4_4.mapping = {
    "e": room4_1,
    "n": room4_7
}
room4_5.mapping = {}
room4_6.mapping = {
    "w": room4_10,
    "n": room4_15
}
room4_7.mapping = {
    "e": room4_8,
    "n": room4_11,
    "s": room4_4
}
room4_8.mapping = {
    "w": room4_7,
    "e": room4_9,
    "n": room4_12,
    "s": room4_1
}
room4_9.mapping = {
    "w": room4_8,
    "e": room4_10,
    "s": room4_2
}
room4_10.mapping = {
    "w": room4_9,
    "e": room4_6,
    "n": room4_14,
    "s": room4_3
}
room4_11.mapping = {
    "e": room4_12,
    "s": room4_7
}
room4_12.mapping = {
    "w": room4_11,
    "e": room4_13,
    "n": room4_16,
    "s": room4_8
}
room4_13.mapping = {
    "e": room4_14,
    "n": room4_17,
    "s": room4_9
}
room4_14.mapping = {
    "w": room4_13,
    "e": room4_15,
    "n": room4_18,
    "s": room4_10
}
room4_15.mapping = {
    "w": room4_14,
    "n": room4_19,
    "s": room4_6
}
room4_16.mapping = {
    "e": room4_17,
    "n": room4_20,
    "s": room4_12
}
room4_17.mapping = {
    "w": room4_16,
    "e": room4_18,
    "n": room4_21,
    "s": room4_13
}
room4_18.mapping = {
    "w": room4_17,
    "e": room4_19,
    "n": room4_22,
    "s": room4_14
}
room4_19.mapping = {
    "w": room4_18,
    "n": room4_23,
    "s": room4_15
}
room4_20.mapping = {
    "e": room4_21,
    "s": room4_16
}
room4_21.mapping = {
    "w": room4_20,
    "e": room4_22,
    "s": room4_17
}
room4_22.mapping = {
    "w": room4_21,
    "e": room4_23,
    "s": room4_18
}
room4_23.mapping = {
    "s": room4_19
}

#################
# ROOMS_5
room5_0 = Room(
    name="[00] Frost Gate",
    story="A heavy iron gate stands half-open. Frost coats every stone."
)
room5_1 = Room(
    name="[01] Guard Chamber",
    story="An old guardroom with a cracked hearth. The fire died long ago."
)
room5_2 = Room(
    name="[02] Bone Cellar",
    story="The floor gives out under your weight. Bones rush up to meet you.",
    kill=True
)
room5_3 = Room(
    name="[03] Supply Hall",
    story="Frost-covered crates line the walls. A torch still wrapped in oilcloth.",
    items=["torch"]
)
room5_4 = Room(
    name="[04] Barracks",
    story="Rows of frozen cots. Someone left in a hurry and never came back."
)
room5_5 = Room(
    name="[05] Forge Pit",
    story="The ancient forge collapsed inward. Embers still glow beneath the rubble.",
    kill=True
)
room5_6 = Room(
    name="[06] Arsenal",
    story="Racks of rusted weapons. A brass key hangs forgotten on a peg.",
    items=["key"]
)
room5_7 = Room(
    name="[07] Inner Keep",
    story="The heart of the watchtower. Cold wind howls through arrow slits."
)
room5_8 = Room(
    name="[08] Prison",
    story="The cell floor collapses into a black shaft. Something stirs below.",
    kill=True
)
room5_9 = Room(
    name="[09] Armory Cache",
    story="A hidden alcove behind a loose stone. Faded schematics of the tower.",
    secret=True,
    items=["chart"]
)
room5_10 = Room(
    name="[10] Sealed Vault",
    story="A heavy vault door. Whatever is inside was meant to stay there.",
    locked=True
)
room5_11 = Room(
    name="[11] Commander's Hall",
    story="At the top of the tower, a frozen crown rests on a stone throne.",
    items=["crown"],
    win=True
)
# MAPPINGS_5
room5_0.mapping = {
    "n": room5_1
}
room5_1.mapping = {
    "s": room5_0,
    "e": room5_2,
    "n": room5_4
}
room5_2.mapping = {}
room5_3.mapping = {
    "w": room5_4,
    "n": room5_6
}
room5_4.mapping = {
    "s": room5_1,
    "e": room5_3,
    "n": room5_7
}
room5_5.mapping = {}
room5_6.mapping = {
    "s": room5_3,
    "w": room5_7
}
room5_7.mapping = {
    "s": room5_4,
    "w": room5_5,
    "e": room5_6,
    "n": room5_10
}
room5_8.mapping = {}
room5_9.mapping = {
    "e": room5_10
}
room5_10.mapping = {
    "w": room5_9,
    "e": room5_8,
    "n": room5_11,
    "s": room5_7
}
room5_11.mapping = {}

#################
# ROOMS_6
room6_0 = Room(
    name="[00] Ashen Gate",
    story="The gate to the crypt hangs open. Ash drifts silently through the arch."
)
room6_1 = Room(
    name="[01] Ember Foyer",
    story="A wide entry chamber. The walls are still faintly warm to the touch."
)
room6_2 = Room(
    name="[02] Pit of Bones",
    story="The floor collapses under you. Bones break your fall—and everything else.",
    kill=True
)
room6_3 = Room(
    name="[03] Cinder Hall",
    story="A broad hall carpeted in grey ash. The air smells of old fire.",
    items=["torch"]
)
room6_4 = Room(
    name="[04] Scorching Vent",
    story="A gust of superheated air blasts upward from a vent below.",
    kill=True
)
room6_5 = Room(
    name="[05] Charred Armory",
    story="Weapon racks reduced to charcoal. A brass key lies untouched in the ash.",
    items=["key"]
)
room6_6 = Room(
    name="[06] Ember Gate",
    story="A chamber sealed behind heat-fused iron bars. Faded notes line the walls.",
    locked=True,
    items=["note"]
)
room6_7 = Room(
    name="[07] Ash Corridor",
    story="A long corridor coated in soft ash. Every step leaves a perfect print."
)
room6_8 = Room(
    name="[08] Coal Walk",
    story="Black walls of compacted coal reflect faint red light from somewhere below."
)
room6_9 = Room(
    name="[09] Magma Drop",
    story="You step onto a false floor above a magma pool. It does not hold.",
    kill=True
)
room6_10 = Room(
    name="[10] Soot Chamber",
    story="A small chamber thick with black soot. The air is heavy and bitter."
)
room6_11 = Room(
    name="[11] Fire Vault",
    story="A vault chamber where embers still glow in ancient braziers."
)
room6_12 = Room(
    name="[12] Bone Shrine",
    story="A hidden alcove behind a collapsed pillar. Strange inscriptions cover the wall.",
    secret=True,
    items=["chart"]
)
room6_13 = Room(
    name="[13] High Crypt",
    story="Upper crypt passages hewn from black stone. The ceiling drips with minerals."
)
room6_14 = Room(
    name="[14] Ember Bridge",
    story="A narrow bridge over a dry abyss. A ratchet locks the gate behind you once crossed."
)
room6_15 = Room(
    name="[15] Crypt Antechamber",
    story="An antechamber before the upper crypts. Cold air descends from above.",
    items=["rope"]
)
room6_16 = Room(
    name="[16] Inferno Shaft",
    story="A shaft roaring with updrafts of flame. The heat is absolute.",
    kill=True
)
room6_17 = Room(
    name="[17] Upper Crypt",
    story="The upper burial halls. Dust covers everything in a perfect grey layer."
)
room6_18 = Room(
    name="[18] Deep Sanctum",
    story="The innermost sanctum. An iron crown rests cold on a stone pedestal.",
    items=["crown"]
)
room6_19 = Room(
    name="[19] Ember Throne",
    story="The ancient throne chamber. The crypt's master is long gone. You have claimed it.",
    win=True
)
# MAPPINGS_6
room6_0.mapping = {
    "n": room6_1
}
room6_1.mapping = {
    "s": room6_0,
    "w": room6_2,
    "n": room6_3
}
room6_2.mapping = {}
room6_3.mapping = {
    "s": room6_1,
    "n": room6_7,
    "e": room6_4
}
room6_4.mapping = {}
room6_5.mapping = {
    "e": room6_7,
    "n": room6_10
}
room6_6.mapping = {
    "n": room6_13,
    "s": room6_8
}
room6_7.mapping = {
    "w": room6_5,
    "e": room6_8,
    "s": room6_3,
    "n": room6_11
}
room6_8.mapping = {
    "w": room6_7,
    "e": room6_9,
    "s": room6_4,
    "n": room6_6
}
room6_9.mapping = {}
room6_10.mapping = {
    "s": room6_5,
    "e": room6_11,
    "n": room6_15
}
room6_11.mapping = {
    "w": room6_10,
    "e": room6_6,
    "s": room6_7,
    "n": room6_14
}
room6_12.mapping = {
    "e": room6_15
}
room6_13.mapping = {
    "s": room6_6,
    "w": room6_14,
    "n": room6_16
}
room6_14.mapping = {
    "s": room6_11,
    "e": room6_13,
    "n": room6_18
}
room6_15.mapping = {
    "s": room6_10,
    "w": room6_12,
    "e": room6_14,
    "n": room6_17
}
room6_16.mapping = {}
room6_17.mapping = {
    "s": room6_15,
    "e": room6_18
}
room6_18.mapping = {
    "w": room6_17,
    "s": room6_14,
    "e": room6_16,
    "n": room6_19
}
room6_19.mapping = {}