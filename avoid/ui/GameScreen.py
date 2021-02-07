import pyxel

from listHandler import draw_list

class GameScreen:
    def __init__(self, player, blocks):
        self.player = player
        self.blocks = blocks
    
    def handleHearts(self):
        if self.player.hp > 1:
            if self.player.hp < 3:
                pyxel.rect(0, 0, 5, 5, 4)
                pyxel.rect(10, 0, 5, 5, 4)
                pyxel.rect(20, 0, 5, 5, 1)
            
            else:
                pyxel.rect(0, 0, 5, 5, 4)
                pyxel.rect(10, 0, 5, 5, 4)
                pyxel.rect(20, 0, 5, 5, 4)
            
        else:
            pyxel.rect(0, 0, 5, 5, 4)
            pyxel.rect(10, 0, 5, 5, 1)
            pyxel.rect(20, 0, 5, 5, 1)
    
    def update(self, blocks):
        self.blocks = blocks
    
    def draw(self):
        self.player.draw()
        draw_list(self.blocks)
        
        self.handleHearts()
    