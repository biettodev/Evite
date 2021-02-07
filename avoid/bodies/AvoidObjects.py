from bodies.CarousselObject import CarousselObject

class AvoidObject(CarousselObject):
    def __init__(self, posx, posy, size, sprite):
        super().__init__(posx, posy, size, sprite)
        self.group = 'AVOID'
        
    def  giveDamage(self, player):
        player.hp -= 1
        player.posy = 30
        player.hit = False
 
class SBlock(AvoidObject):
    def __init__(self, posx, posy, size, sprite):
        super().__init__(posx, posy, size, sprite)
        self.size = {'w':7, 'h':7}  
     
class MBlock(AvoidObject):
    def __init__(self, posx, posy, size, sprite):
        super().__init__(posx, posy, size, sprite)
        self.size = {'w':9, 'h':9}

class LBlock(AvoidObject):
    def __init__(self, posx, posy, size, sprite):
        super().__init__(posx, posy, size, sprite)
        self.size = {'w':4, 'h':12}

class DBlock(AvoidObject):
    def __init__(self, posx, posy, size, sprite):
        super().__init__(posx, posy, size, sprite)
        self.size = {'w':7, 'h':7}
        
    def decreaseSpeed(self, player):
        player.vel = 1

class MDBlock(AvoidObject):
    def __init__(self, posx, posy, size, sprite):
        super().__init__(posx, posy, size, sprite)
        self.size = {'w':7, 'h':7}
        
    def giveDamage(self, player):
        player.hp -= 2
        player.posy = 30
        player.hit = False
        