import random

from Entities import *

all_cards = [
    CharacterEnum.MR_GREEN, CharacterEnum.MRS_WHITE, CharacterEnum.MRS_PEACOCK, CharacterEnum.COLONEL_MUSTARD, CharacterEnum.MISS_SCARLET, CharacterEnum.PROFESSOR_PLUM,
    WeaponEnum.ROPE, WeaponEnum.KNIFE, WeaponEnum.WRENCH, WeaponEnum.REVOLVER, WeaponEnum.CANDLESTICK, WeaponEnum.LEAD_PIPE,
    RoomEnum.DINING_ROOM, RoomEnum.BILLIARD_ROOM, RoomEnum.HALL, RoomEnum.STUDY, RoomEnum.BALLROOM, RoomEnum.CONSERVATORY, RoomEnum.KITCHEN, RoomEnum.LIBRARY, RoomEnum.LOUNGE
]

class Player():
    def __init__(self, name, turn_index):
        self.name = name
        self.turn_index = turn_index
        self.hand = []
        self.location = RoomEnum.START

    def getMoves(self):
        return room_access[self.location]

    def makeMove(self, number):
        print(f"move chosen: {number}")

class ClueGame():
    def __init__(self, player_count):
        self.face_up_cards = []
        self.turn_index = 0
        self.solution = generateSolution()
        self.players = self.createPlayers(player_count)

    def createPlayers(self, player_count):
        cards = all_cards.copy()

        print(self.solution)
        cards.remove(self.solution.character)
        cards.remove(self.solution.weapon)
        cards.remove(self.solution.room)
        print(cards)

        players = []
        for i in range(player_count):
            players.append(Player(f"Player{i+1}", i))

        while len(cards) >= player_count:
            for player in players:
                card = random.choice(cards)
                cards.remove(card)
                player.hand.append(card)
        self.face_up_cards = cards
        return players

    def printGameState(self):
        printBoard()
        print("Face up cards: ", [card.name for card in self.face_up_cards])
        for player in self.players:
            #if(player.turn_index == self.turn_index): print("Your Turn: ", end="")
            print(f"{player.name} is in {player.location.name}");
        print()
        self.promptPlayer()

    def promptPlayer(self):
        player = self.players[self.turn_index]
        moves = player.getMoves()
        print(f"{player.name} to move. Current Location: {player.location.name}")
        for index, move in enumerate(moves):
            print(f"To move to {move.name}, type: {index}")
        if(player.location == RoomEnum.START): print(f"To stay and make a Final Accusation type: -1")
        else: print(f"To stay and make a suggestion type: -1")
        self.players[self.turn_index].makeMove(input("Enter Move: "))


def printBoard():
    print("""
        +------------+------------+--------------+
        |   KITCHEN  |            | CONSERVATORY |
        |               BALLROOM                 |
        | [SECRET_2] |            |  [SECRET_1]  |
        |            |-----  -----+------  ------+
        +-----  -----+            |   BILLIARD   |
        |   DINING   |    START         ROOM     |
        |    ROOM                 +------  ------+
        +-----  -----+-----  -----+    LIBRARY   |
        |   LOUNGE   |            +------ -------+
        |                 HALL          STUDY    |
        | [SECRET_1] |            |  [SECRET_2]  |
        +------------+------------+--------------+ """
    )

def generateSolution():
    character = random.choice(list(CharacterEnum))
    weapon = random.choice(list(WeaponEnum))
    room_list = list(RoomEnum)
    room_list.remove(RoomEnum.START)
    room = random.choice(room_list)
    return Suggestion(character, weapon, room)
