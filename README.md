To Run: 
	From the terminal, go to the src folder. Run `python __init__.py`

To Clone:
	git clone https://github.com/EdelEB/ClueGame.git

Abstract: 
	This project’s goal was to create a playable version of the game Cluedo that includes AI agents that have the ability to play the game and make decisions. The game poses a great format, since the decisions players make should be evolving as the game progresses and more information is revealed. Also, depending on the player’s ability to maintain and aggregate information, they can deduct which cards players may or may not have, and what cards may not be getting shown secretly. 



Game Rules: 
	To start, a solution is randomly picked that contains a character, weapon, and room. Then the rest of the cards are evenly dealt to the players where extra cards are left face up. 
All of the players begin at the Start location. The Start is where you begin and end the game; this is because final accusations can only be made from the Start location. 
This version of the game has no dice or grid pattern to traverse on the board. Depending on the room a player is in determines which rooms they can travel to on their turn. Once a room is entered, a suggestion must be made. A suggestion is a combination of a character, a weapon, and the room that player is in. 
Once a suggestion is made, the next player is required to show a card from their hand, present in the suggestion, to the player who made the suggestion. If they don’t have a card from the suggestion, they  pass to the next player until it returns to the suggestor. 
Throughout these interactions the players should be able to slowly gather more information that allows them to figure out what the solution is. 
The game ends when a player moves back to the start and makes a final accusation that matches the solution. If a final accusation is incorrect, that player can no longer win. 
