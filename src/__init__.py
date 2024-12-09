from ClueGame import *
from AI_Agent import *

def main():
    game = ClueGame(3)
    game.players[0].is_ai = True
    game.players[0].ai_agent = AI_Agent(game.players[0].hand, 0, game)
    game.players[1].is_ai = True
    game.players[1].ai_agent = AI_Agent(game.players[1].hand, 1, game)
    game.players[2].is_ai = True
    game.players[2].ai_agent = AI_Agent(game.players[2].hand, 2, game)
    '''game.players[3].is_ai = True
    game.players[3].ai_agent = AI_Agent(game.players[3].hand, 3, game)
'''
    for player in game.players:
        print(f"{player.name}: {[card.name for card in player.hand]}")

    while game.winner is None:
        game.printGameState()
        #input("\nClick Enter to continue")

    print(f"Game Over Winner: {game.winner.name}\nFinal answer: {game.solution}")

if __name__ == "__main__":
    main()