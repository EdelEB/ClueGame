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
        self.failed = False
        self.is_ai = False
        self.ai_agent = None

    def getMoves(self):
        return room_access[self.location]


class ClueGame():
    def __init__(self, player_count):
        self.face_up_cards = []
        self.turn_index = 0
        self.solution = generateSolution()
        self.players = self.createPlayers(player_count)
        self.winner = None

    def createPlayers(self, player_count):
        cards = all_cards.copy()

        print(self.solution)
        cards.remove(self.solution.character)
        cards.remove(self.solution.weapon)
        cards.remove(self.solution.room)
        #print([card.name for card in cards])

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
        print("Face up cards: ", [card.name for card in self.face_up_cards], '\n')
        for player in self.players:
            print(f"{player.name} in {player.location.name}\t\t", end="");
        print('\n')
        self.promptPlayerMove()

    def promptPlayerMove(self):
        if self.players[self.turn_index].is_ai: return self.promptAIPlayerMove()
        else: return self.promptHumanPlayerMove()

    def promptAIPlayerMove(self):
        return None

    def promptHumanPlayerMove(self):
        player = self.players[self.turn_index]
        moves = player.getMoves()
        print(f"{player.name} to move. Current Location: {player.location.name}")
        print(f"See the key below to see what inputs make what moves")
        for index, move in enumerate(moves):    print(f"{move.name}: {move.value}", end="\t\t")
        if(player.location == RoomEnum.START):  print(f"\nMake Final Accusation: -1")
        else:                                   print(f"\nMake a suggestion: -1")

        player_input = input("Enter Move: ")
        while ( assignRoomEnum(player_input) not in moves ) and (player_input != '-1'):
            player_input = input("Invalid Move. Try again: ")

        player_input = int(player_input)
        if player_input != -1:
            self.players[self.turn_index].location = assignRoomEnum(player_input)

        if self.players[self.turn_index].location == RoomEnum.START:
            print(f"{player.name} Make Final Accusation:")
            suggestion = self.promptSuggestion()
            if suggestion == self.solution:
                self.winner = self.players[self.turn_index]
            else:
                player.failed = True
        else:
            print(f"{player.name} Make Suggestion: You are in the {player.location.name}")
            suggestion = self.promptSuggestion()
            print(suggestion)
            shown_card = self.proposeSuggestion(suggestion, self.nextPlayer(player))
            if shown_card is None:
                print("No player could show a card")
            else:
                print(f"{shown_card[0]} shows {shown_card[1]}")

        self.turn_index = self.nextPlayer(player).turn_index

    def promptSuggestion(self):
        if self.players[self.turn_index].is_ai: return self.promptAISuggestion()
        else: return self.promptHumanSuggestion()

    def promptAISuggestion(self):
        return None

    def promptHumanSuggestion(self):
        for weapon in list(WeaponEnum):
            print(f"{weapon.name}: {weapon.value},", end="\t\t")
        weapon_input = input("\nWeapon: ")
        while assignWeaponEnum(weapon_input) is None:
            weapon_input = input("Invalid Move. Try again: ")
        weapon_input = assignWeaponEnum(weapon_input)

        for character in list(CharacterEnum):
            print(f"{character.name}: {character.value},", end="\t\t")
        character_input = input("\nCulprit: ")
        while assignCharacterEnum(character_input) is None:
            character_input = input("Invalid Move. Try again: ")
        character_input = assignCharacterEnum(character_input)

        if self.players[self.turn_index].location == RoomEnum.START:
            for room in list(RoomEnum):
                print(f"{room.name}: {room.value},", end="\t\t")
            room_input = input("\nRoom: ")
            while assignRoomEnum(room_input) is None:
                room_input = input("Invalid Move. Try again: ")
            room_input = assignRoomEnum(room_input)
        else:
            room_input =  self.players[self.turn_index].location

        return Suggestion(character_input, weapon_input, room_input)

    def proposeSuggestion(self, suggestion, player):
        showable_cards = []
        while(player.turn_index != self.turn_index):
            for item in [suggestion.weapon, suggestion.character, suggestion.room ]:
                for card in player.hand:
                    if item == card:
                        showable_cards.append(card)
            if len(showable_cards) == 0:
                print(f"{player.name} skips")
                player = self.nextPlayer(player)
            else:
               return self.promptShowCard(player, showable_cards)
        return None

    def promptShowCard(self, player, showable_cards):
        if self.players[self.turn_index].is_ai: return self.promptAIShowCard(player, showable_cards)
        else: return self.promptHumanShowCard(player, showable_cards)

    def promptAIShowCard(self, player, showable_cards):
        return None

    def promptHumanShowCard(self, player, showable_cards):
        if len(showable_cards) == 1: return (player.name, showable_cards[0].name)
        print(f"{player.name} choose a card to show...")
        for card in showable_cards:
            print(f"{card.name}: {card.value},", end="\t\t")
        card_input = input("\nShow: ")
        while int(card_input) not in [c.value for c in showable_cards]:
            card_input = input("Invalid Move. Try again: ")

        for card in showable_cards:
            if card.value == int(card_input):
                return (player.name, card.name)

        return "Error choosing card to show"

    def nextPlayer(self, player):
        if player.turn_index == len(self.players)-1:
            return self.players[0]
        else:
            return self.players[player.turn_index+1]

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
