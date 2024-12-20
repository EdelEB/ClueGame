
from enum import Enum

class Suggestion:
    def __init__(self, character, weapon, room):
        self.character = character
        self.weapon = weapon
        self.room = room

    def __eq__(self, other):
        if self.character == other.character and self.weapon == other.weapon and self.room == other.room:
            return True
        return False

    def __repr__(self):
        return f"Suggestion(Character: {self.character.name}, Weapon: {self.weapon.name}, Room: {self.room.name})"

class CharacterEnum(Enum):
    COLONEL_MUSTARD = 1
    MISS_SCARLET = 2
    PROFESSOR_PLUM = 3
    MR_GREEN = 4
    MRS_PEACOCK = 5
    MRS_WHITE = 6

def assignCharacterEnum(player_input):
    try:
        x = int(player_input)
        x = CharacterEnum(x)
        return x
    except:
        return None

class WeaponEnum(Enum):
    CANDLESTICK = 1
    KNIFE = 2
    LEAD_PIPE = 3
    REVOLVER = 4
    ROPE = 5
    WRENCH = 6

def assignWeaponEnum(player_input):
    try:
        x = int(player_input)
        x = WeaponEnum(x)
        return x
    except:
        return None

class RoomEnum(Enum):
    KITCHEN = 1
    BALLROOM = 2
    CONSERVATORY = 3
    DINING_ROOM = 4
    BILLIARD_ROOM = 5
    LIBRARY = 6
    LOUNGE = 7
    HALL = 8
    STUDY = 9
    START = 10

def assignRoomEnum(player_input):
    try:
        x = int(player_input)
        x = RoomEnum(x)
        return x
    except:
        return None

room_access = {
    RoomEnum.KITCHEN: [RoomEnum.BALLROOM, RoomEnum.DINING_ROOM, RoomEnum.STUDY, RoomEnum.START],
    RoomEnum.BALLROOM: [RoomEnum.KITCHEN, RoomEnum.CONSERVATORY, RoomEnum.START],
    RoomEnum.CONSERVATORY: [RoomEnum.BALLROOM, RoomEnum.LOUNGE, RoomEnum.START],
    RoomEnum.DINING_ROOM: [RoomEnum.KITCHEN, RoomEnum.LOUNGE, RoomEnum.START],
    RoomEnum.BILLIARD_ROOM: [RoomEnum.LIBRARY, RoomEnum.BALLROOM, RoomEnum.START],
    RoomEnum.LIBRARY: [RoomEnum.STUDY, RoomEnum.BILLIARD_ROOM, RoomEnum.START],
    RoomEnum.LOUNGE: [RoomEnum.DINING_ROOM, RoomEnum.HALL, RoomEnum.CONSERVATORY, RoomEnum.START],
    RoomEnum.HALL: [RoomEnum.LOUNGE, RoomEnum.STUDY, RoomEnum.LIBRARY, RoomEnum.START],
    RoomEnum.STUDY: [RoomEnum.HALL, RoomEnum.LIBRARY, RoomEnum.KITCHEN, RoomEnum.START],
    RoomEnum.START: [RoomEnum.KITCHEN, RoomEnum.BALLROOM, RoomEnum.CONSERVATORY, RoomEnum.DINING_ROOM,
                     RoomEnum.LIBRARY, RoomEnum.LOUNGE, RoomEnum.HALL, RoomEnum.STUDY, RoomEnum.BILLIARD_ROOM]
}