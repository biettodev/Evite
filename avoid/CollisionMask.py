class CollisionMask:
    def __init__(self, posx, posy, size):
        self.posx = posx
        self.posy = posy
        self.size = size
		
    def maskInX(self):
        mask = []
        width = self.size['w']
        for px in range(self.posx, self.posx + width+1):
            mask.append(px)
        
        return mask
    
    def maskInY(self):
        mask = []
        height = self.size['h']
        for py in range(self.posy, self.posy + height+1):
            mask.append(py)
        
        return mask