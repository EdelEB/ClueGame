from itertools import product

from ClueGame import *

class AI_Agent():
    def __init__(self, hand, turn_index, clue_game):
        self.hand = hand
        self.turn_index = turn_index
        self.valid_cards = all_cards.copy()
        for card in self.hand:
            self.valid_cards.remove(card)
        self.mock_players = []
        for player in clue_game:
            if turn_index == player.turn_index: continue
            self.mock_players.append(MockPlayer(player.name, player.turn_index, hand + clue_game.face_up_cards))

    def calcPossibleCombos(self):
        characters = []
        weapons = []
        rooms = []
        for card in self.valid_cards:
            if isinstance(card, RoomEnum): rooms.append(card)
            elif isinstance(card, WeaponEnum): weapons.append(card)
            else: characters.append(card)

        suggestions = [
            Suggestion(character, weapon, room) for character, weapon, room in product(characters, weapons, rooms)
        ]

        count = 1;
        for suggestion in suggestions:
            #print(f"{count} {suggestion}")
            count+=1


    # track players' hands
    # track who shows a card and what was guessed
    # track what players do not have

class MockPlayer():
    def __init__(self, name, turn_index, not_in_hand):
        self.name = name
        self.turn_index = turn_index
        self.hand = []
        self.maybe_in_hand = []
        self.not_in_hand = not_in_hand