from bodies.AvoidBlock import AvoidBlock

class MBlock(AvoidBlock):
    def __init__(self, posx, posy, sprite):
        super().__init__(posx, posy, sprite)
        self.size = {'w':9, 'h':9}
        