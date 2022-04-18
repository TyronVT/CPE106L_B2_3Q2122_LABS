''' This is the main logic for a Tic-tac-toe game.
It is not optimised for a quality game it simply
generates random moves and checks the results of
a move for a winning line. Exposed functions are:
newGame()
saveGame()
restoreGame()
userMove()
computerMove()

This is a modified version of the oxo_logic.py program. 
The modification was made to reflect OOP design. A 'Game'
class was used in this case.
'''

import os, random
import oxo_data

class Game:
    def __init__(self):
        self.game_board = []
        self.newGame()

    def newGame(self):
        """Return a list with all elements as a whitespace."""
        self.game_board = list(" " * 9)

    def saveGame(self):
        oxo_data.saveGame(self.game_board)

    def restoreGame(self):
        """Restore previously stored game. Return new game if not succesful."""
        try:
            self.game_board = oxo_data.restoreGame()
            if len(self.game_board) != 9:
                self.game_board = self.newGame()
        except IOError:
            self.game_board = self.newGame()
                
    def _generateMove(self):
        """Generate a random move from available cells. Return -1 if all cells are occupied."""
        options = [i for i in range(len(self.game_board)) if self.game_board[i] == " "]
        if options:
            return random.choice(options)
        else: return -1
    
    def _isWinningMove(self):
        """Checks if the move placed is the winning move."""
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))

        for a,b,c in wins:
            chars = self.game_board[a] + self.game_board[b] + self.game_board[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def userMove(self,cell):
        if self.game_board[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.game_board[cell] = 'X'
        if self._isWinningMove():
            return 'X'
        else:
            return ""

    def computerMove(self):
        cell = self._generateMove()
        if cell == -1:
            return 'D'
        self.game_board[cell] = 'O'
        if self._isWinningMove():
            return 'O'
        else:
            return ""

def testGame(game):
    result = ""
    while not result:
        print(game.game_board)
        try:
            result = game.userMove(game._generateMove())
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = game.computerMove()
        
        if not result: continue
        elif result == 'D':
            print("Draw")
        else:
            print("Winner is: ", result)
        print (game.game_board)

def playGame(game):
    result = ""
    while not result:
        print(game.game_board)
        try:
            user_choice = input("Enter cell [0-8] (Q to quit game | R to restore): ")
            if user_choice == 'Q':
                save = input("Save game before quitting? [y/n]: ")
                if save == 'y':
                    oxo_data.saveGame(game.game_board)
                    quit()
            elif user_choice == 'R':
                game.game_board = oxo_data.restoreGame()
            else:
                result = game.userMove(int(user_choice))
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result and user_choice != 'R':
            result = game.computerMove()
        
        if not result: continue
        elif result == 'D':
            print("Draw")
        else:
            print("Winner is: ", result)
        print (game.game_board)
