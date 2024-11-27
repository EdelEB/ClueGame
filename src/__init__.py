from ClueGame import *
from AI_Agent import *

def main():
    hand = [CharacterEnum.MR_GREEN, WeaponEnum.ROPE, RoomEnum.DINING_ROOM, CharacterEnum.MRS_WHITE]
    ai = AI_Agent(hand)

    ai.calcPossibleCombos()


    for room, access in room_access.items():
        print(f'{room.name}: ')
        for e in access:
            print(f'\t{e.name}')

if __name__ == "__main__":
    main()