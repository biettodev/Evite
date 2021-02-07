import pyxel

from bodies.Body import Body

class Player(Body):
    def __init__(self, posx, posy, size, sprite):
        super().__init__(posx, posy, size, sprite)
        self.size = {'w':10, 'h':10}
        self.vel = 2
        self.hit = False
        self.hp = 3
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.hit = True
        self.togglesDirection()
        
    def draw(self):
        width, height = self.size.values()
        pyxel.rect(
            x=self.posx, y=self.posy,
            w=width, h=height,
            col=9
        )
    
    def checkOnLimit(self, border):
        # Checks touch of ball on top
        if self.posy <= border:
            self.hit = False
    
    def moveUp(self):
        self.posy -= self.vel
        
    def moveDown(self):
        self.posy += self.vel
    
    def togglesDirection(self):
        if self.hit: self.moveUp()
        else: self.moveDown()