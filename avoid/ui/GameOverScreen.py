import pyxel

from listHandler import *

class GameOverScreen:
    def __init__(self):
        self.next_level = 1
        
    def drawGameOverWinner(self, level):
        pyxel.text(5, 30, "You Win", 13)
        pyxel.text(5, 60, f"ENTER TO CONTINUE \n(Next {level})", 13)
    
    def drawGameOverLoser(self):
        pyxel.text(5, 30, "You Lose", 13)
        pyxel.text(5, 60, f"R - Retart ({self.next_level})", 13)
        pyxel.text(5, 70, "Q - Quit", 13)
    
    def nextLevel(self, next_level):
        self.next_level = next_level
    
    def draw(self, screen):
        if screen == 'WIN':
            self.drawGameOverWinner(self.next_level)
        elif screen == 'LOSE':
            self.drawGameOverLoser()