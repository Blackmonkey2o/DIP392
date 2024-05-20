# DIP392
DIP392 Team
https://docs.google.com/document/d/1VFEz9er-IhWF1hI35oSqtMKnKxJKBLiT1UiZTaVMjlk/edit?usp=sharing

Connect Four Game.

This is simple implementation of the Connect Four game using Python.

How to play:
1. Starting the Game:
- Run the Python script. This will open a window titled "Connect Four".
- The game board will be displayed as a blue grid with white circles representing empty slots.
2. Understanding the Interface:
- The board consists of 7 columns and 6 rows.
- There is a menu bar at the top with options: File and Points.
3. Making a Move:
- The game starts with Player One (Red) making the first move.
- To make a move, click on the column where you want to drop your piece. 
- The piece will fall to the lowest available slot in that column.
Player Two (Yellow) will take the next turn.
4. Winning the Game:
- The objective is to connect four of your pieces vertically, horizontally, or diagonally.
- The game checks for a winning move after each turn. If a player connects four pieces, a message box will pop up declaring the winner.
- The winning player will have their score incremented by one, which can be viewed in the Points menu.
5. Game Over:
- Once a player wins, the game is over, and no more moves can be made.
- To start a new game, go to the File menu and select "New Game". This will reset the board but keep the scores.
- To reset the game and the scores, select "Restart Game" from the File menu.
6. Viewing Scores:
- At any time, you can view the current scores by selecting "Show Points" from the Points menu. A message box will display the scores for Player One and Player Two.
7. Exiting the Game:
- To exit the game, select "Exit" from the File menu or close the window.

Playing Tips
Plan Ahead: Try to think a few moves ahead to block your opponent and create opportunities for yourself.
Center Column: The center column is often the best starting point because it offers the most potential connections.
Block Opponent: Keep an eye on your opponent’s moves and block them if they are about to connect four pieces.

Controls:
A player should use the mouse to select column, click on desire column and drop a disc. Close the game to exit game.

Files:
'main.py' - the game logic file.
'README.md' - instruction for the game.

Dependencies:
1. Python 3.
2. Tkinter library.

Installation: 
1. Clone or dowload the reprository to your machine.
2. Install dependencies.
3. Run 'main.py' to start game.

Enjoy the game!
