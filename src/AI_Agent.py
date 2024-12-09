from itertools import product

from ClueGame import *

class AI_Agent():
    def __init__(self, hand, turn_index, clue_game):
        self.turn_index = turn_index
        self.valid_cards = all_cards.copy()
        for card in hand + clue_game.face_up_cards:
            self.valid_cards.remove(card)
        self.mock_players = []
        for player in clue_game.players:
            if turn_index == player.turn_index: continue
            self.mock_players.append(MockPlayer(player.name, player.turn_index, hand+clue_game.face_up_cards))
        self.name = clue_game.players[turn_index].name

    def getAIMove(self, location, moves):
        combos = self.calcPossibleCombos()
        if len(combos) == 1:
            if location == RoomEnum.START: return -1
            else: return RoomEnum.START.value
        else:
            for loc in moves:
                if loc in self.valid_cards:
                    return loc.value
            for loc in moves:
                if loc == RoomEnum.START: continue
                for room in room_access[loc]:
                    if room in self.valid_cards:
                        return loc.value
            for loc in moves:
                if loc != RoomEnum.START:
                    return loc.value

    def makeSuggestion(self, location):
        combos = self.calcPossibleCombos()
        if len(combos) == 1 and location == RoomEnum.START:
            return combos[0]

        for combo in combos:
            if combo.room == location:
                return combo

        print(f"ERROR finding finding suggestion in current Location {location}")
        try:
            new_suggestion = Suggestion(combos[0].character, combos[0].weapon, location)
            print(new_suggestion)
        except IndexError:
            print(f"IndexError on combos: {combos}")
            print(f"Valid cards: {[card.name for card in self.valid_cards]}")
        return new_suggestion

    def update(self, code, x, y, turn_index):
        if code == "showMe" and self.turn_index == turn_index:
            player = x
            card = y
            for mock in self.mock_players:
                if mock.turn_index == player.turn_index: mock.hand.append(card)
                else: mock.not_in_hand.append(card)
        elif code == "show" and self.turn_index != turn_index:
            player = x
            if player.turn_index == self.turn_index: return
            suggestion_arr = [y.weapon, y.room, y.character]
            for mock in self.mock_players:
                if mock.turn_index == player.turn_index:
                    possiblities = [card for card in suggestion_arr if card not in mock.not_in_hand]
                    if len(possiblities) == 1:
                        mock.hand.append(possiblities[0])
        elif code == "skip" and self.turn_index != turn_index:
            player = x
            suggestion = y
            for mock in self.mock_players:
                if mock.turn_index == player.turn_index:
                    for card in [suggestion.weapon, suggestion.room, suggestion.character]:
                        mock.not_in_hand.append(card)
        self.updateValidCardsWithMocks()
        self.analyzeData()

    def updateValidCardsWithMocks(self):
        for mock in self.mock_players:
            for card in mock.hand:
                try:
                    self.valid_cards.remove(card)
                    print(f"{self.name} invalidates {card.name}")
                    #print(f"{self.name} valid cards: {[card.name for card in self.valid_cards]}")
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

        suggestions = [Suggestion(character, weapon, room) for character, weapon, room in product(characters, weapons, rooms)]
        return suggestions

class MockPlayer():
    def __init__(self, name, turn_index, not_in_hand):
        self.name = name
        self.turn_index = turn_index
        self.hand = []
        self.not_in_hand = not_in_hand