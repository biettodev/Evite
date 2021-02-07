import pyxel
from bodies.CarousselObject import CarousselObject

class Gem(CarousselObject):
    def __init__(self, posx, posy, size, animation):
        super().__init__(posx, posy, size, animation)
        self.group = 'DESTRUCT'
        self.size = {'w':7, 'h':7}
        self.animation = animation
        
    def draw(self): 
        width, height = self.size.values()
        try:
            for frame in self.animation:
                aimg, pu, pv, colk = frame.values()
                pyxel.blt(
                    x=self.posx, y=self.posy,
                    img=aimg,
                    u=pu, v=pv,
                    w=width, h=height,
                    colkey=colk
                )
        except:
            return 

class Ruby(Gem):
    def setSpecial(self):
        pass

class Saphire(Gem):
    def setSpecial(self, player):
        try:
            player.hp += 1
            player.hit = False
        except:
            return

class Emerald(Gem):
    def setSpecial(self):
        pass