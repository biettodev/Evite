import pyxel

class SkinsMenuScreen:
    def __init__(self, x, y, w, h, col):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col
    
    def draw(self):
        for x in range(0, 50, 10):
            for y in range(0, 50, 10):
                pyxel.blt(
                    x=5, y=5,
                    img=0,
                    u=0, v=0,
                    w=10, h=10,
                    colkey=0
                )