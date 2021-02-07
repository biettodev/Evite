import pyxel

class Body:
    def __init__(self, posx, posy, size, sprite):
        self.posx = posx
        self.posy = posy
        self.w, self.h = size.values()
        self.sprite = sprite
        self.alive = True 
    
    def die(self):
        self.alive = False
    
    def draw(self):
        simg, pu, pv, colk = self.sprite.values()
        width, height = self.size.values()
        
        pyxel.blt(
            x=self.posx, y=self.posy,
            img=simg,
            u=pu, v=pv,
            w=width, h=height,
            colkey=colk
        )
    
    def maskInx(self):
        mask = []
        for px in range(self.posx, self.posx + self.w+1):
            mask.append(px)
        
        return mask
    
    def maskIny(self):
        mask = []
        for py in range(self.posy, self.posy + self.h+1):
            mask.append(py)
        
        return mask