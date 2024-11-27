import random

from Entities import *

all_cards = [
    CharacterEnum.MR_GREEN, CharacterEnum.MRS_WHITE, CharacterEnum.MRS_PEACOCK, CharacterEnum.COLONEL_MUSTARD, CharacterEnum.MISS_SCARLET, CharacterEnum.PROFESSOR_PLUM,
    WeaponEnum.ROPE, WeaponEnum.KNIFE, WeaponEnum.WRENCH, WeaponEnum.REVOLVER, WeaponEnum.CANDLESTICK, WeaponEnum.LEAD_PIPE,
    RoomEnum.DINING_ROOM, RoomEnum.BILLIARD_ROOM, RoomEnum.HALL, RoomEnum.STUDY, RoomEnum.BALLROOM, RoomEnum.CONSERVATORY, RoomEnum.KITCHEN, RoomEnum.LIBRARY, RoomEnum.LOUNGE
]


def generateSolution():
    character = random.choice(list(CharacterEnum))
    weapon = random.choice(list(WeaponEnum))
    room = random.choice(list(RoomEnum))
    return Suggestion(character, weapon, room)

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.location = RoomEnum.START

class ClueGame():
    def __init__(self, player_count):
        self.turn_index = 0
        self.solution = generateSolution()
        self.players = self.createPlayers(player_count)
        self.face_up_cards = []

    def createPlayers(self, player_count):
        cards = all_cards.copy()

        cards.remove(self.solution.character)
        cards.remove(self.solution.weapon)
        cards.remove(self.solution.room)
        print(self.solution)
        print(cards)

        players = []
        for i in range(player_count):
            players.append(Player(f"Player{i}"))

        while len(cards) >= player_count:
            for player in players:
                card = random.choice(cards)
                cards.remove(card)
                player.hand.append(card)
        self.face_up_cards = cards
        return players


