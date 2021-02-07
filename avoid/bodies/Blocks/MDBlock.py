from bodies.AvoidBlock import AvoidBlock

class MDBlock(AvoidBlock):
    def __init__(self, posx, posy, sprite):
        super().__init__(posx, posy, sprite)
        self.size = {'w':7, 'h':7}