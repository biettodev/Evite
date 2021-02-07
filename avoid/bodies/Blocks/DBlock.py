from bodies.AvoidBlock import AvoidBlock

class DBlock(AvoidBlock):
    def __init__(self, posx, posy, sprite):
        super().__init__(posx, posy, sprite)
        self.size = {'w':7, 'h':7}
        
    def decreaseSpeed(self, obj):
        if cond:
            obj.posx -= 1