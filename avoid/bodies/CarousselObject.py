import pyxel

from bodies.Body import Body

class CarousselObject(Body):
    # Checks blocks reached the limit
    def move(self):
        self.posx += 1
        if self.posx >= 100:
            self.posx = 0
    
    def update(self):
        self.move()