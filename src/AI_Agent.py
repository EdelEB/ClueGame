from itertools import product

from ClueGame import *

class AI_Agent():
    def __init__(self, hand, turn_index, clue_game):
        self.hand = hand
        self.shown_hand = []
        self.turn_index = turn_index
        self.valid_cards = all_cards.copy()
        for card in hand + clue_game.face_up_cards:
            self.valid_cards.remove(card)
        self.mock_players = []
        for player in clue_game.players:
            if turn_index == player.turn_index: continue
            self.mock_players.append(MockPlayer(player.name, player.turn_index, hand+clue_game.face_up_cards))

    def getAIMove(self, location, moves):
        combos = self.calcPossibleCombos()
        if len(combos) == 1:
            if location == RoomEnum.START: return -1
            else: return RoomEnum.START.value
        else:
            for loc in moves:
                if loc in self.valid_cards:
                    return loc.value
        return -1

    def makeSuggestion(self, location):
        combos = self.calcPossibleCombos()
        if len(combos) == 1 and location == RoomEnum.START:
            return combos[0]

        for combo in combos:
            if combo.room == location:
                return combo

        print(f"ERROR finding finding suggestion in current Location {location}")
        new_suggestion = Suggestion(combos[0].character, combos[0].weapon, location)
        print(new_suggestion)
        return new_suggestion

    def update(self, code, x, y, turn_index):
        if code == "showMe" and self.turn_index == turn_index:
            player = x
            card = y
            for mock in self.mock_players:
                if mock.turn_index == player.turn_index: mock.hand.append(card)
                else: mock.not_in_hand.append(card)
                try: mock.maybe_in_hand.remove(card)
                except: pass
        elif code == "show" and self.turn_index != turn_index:
            player = x
            suggestion_arr = [y.weapon, y.room, y.character]
            for mock in self.mock_players:
                if mock.turn_index == turn_index:
                    possiblities = [card for card in suggestion_arr if card not in mock.not_in_hand]
                    if len(possiblities) == 1:
                        mock.hand.append(possiblities[0])
                        try: player.maybe_in_hand.remove(possiblities[0])
                        except: pass
        elif code == "skip" and self.turn_index != turn_index:
            player = x
            suggestion = y
            for mock in self.mock_players:
                if mock.turn_index == player.turn_index:
                    for card in [suggestion.weapon, suggestion.room, suggestion.character]:
                        mock.not_in_hand.append(card)
                        try: mock.maybe_in_hand.remove(card)
                        except: pass

        elif code == "passed":
            suggestion = x
            for mock in self.mock_players:
                mock.not_in_hand.append(suggestion.weapon)
                mock.not_in_hand.append(suggestion.room)
                mock.not_in_hand.append(suggestion.character)
                try: mock.maybe_in_hand.remove(suggestion.weapon)
                except: pass
                try: mock.maybe_in_hand.remove(suggestion.room)
                except: pass
                try: mock.maybe_in_hand.remove(suggestion.character)
                except: pass
        self.updateValidCardsWithMocks()
        self.analyzeData()

    def updateValidCardsWithMocks(self):
        for mock in self.mock_players:
            for card in mock.hand:
                try: self.valid_cards.remove(card)
                except: pass

    def analyzeData(self):
        final_cards = []
        for card in self.valid_cards:
            is_final_card = True
            for mock in self.mock_players:
                if card in mock.not_in_hand: continue
                else: is_final_card = False

            if is_final_card: final_cards.append(card)

        for fcard in final_cards:
            self.valid_cards = [ card for card in self.valid_cards if not (isinstance(card, type(fcard)) and card != fcard)]

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

        return suggestions

class MockPlayer():
    def __init__(self, name, turn_index, not_in_hand):
        self.name = name
        self.turn_index = turn_index
        self.hand = []
        self.not_in_hand = not_in_hand
        self.maybe_in_hand = [card for card in all_cards if card not in not_in_hand]