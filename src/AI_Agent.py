from itertools import product

from ClueGame import *

class AI_Agent():
    def __init__(self, hand):
        self.hand = hand

        self.valid_cards = all_cards.copy()
        for card in self.hand: self.valid_cards.remove(card)

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
