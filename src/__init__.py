from ClueGame import *
from AI_Agent import *

def main():
    game = ClueGame(4)

    while game.winner is None:
        game.printGameState()

    print(f"Game Over Winner: {game.winner.name}\nFinal answer: {game.solution}")

if __name__ == "__main__":
    main()