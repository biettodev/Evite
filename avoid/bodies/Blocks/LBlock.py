from bodies.AvoidBlock import AvoidBlock

class LBlock(AvoidBlock):
    def __init__(self, posx, posy, sprite):
        super().__init__(posx, posy, sprite)
        self.size = {'w':4, 'h':12}