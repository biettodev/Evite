import pyxel

from listHandler import update_list, cleanup_list

class MainMenuScreen:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self):
        pyxel.text(
            35, self.h - 90, 
            "Avoid", 
            0
        )
        pyxel.text(
            self.w - 65, self.h - 80, 
            "The Objects", 
            0
        )
        pyxel.text(
            15, self.h - 70, 
            "Destruct The Gems", 
            0
        )
        
        pyxel.rect(0, 40, self.w, 20, 2)
        
        pyxel.text(
            10, self.h - 54, 
            "PLAY - PRESS ENTER", 
            7
        )
        # pyxel.text(
            # self.w / 3, self.h - 40, 
            # "CASUAL \nPRESS C", 
            # 3
        # )
        # pyxel.text(
            # self.w / 3, self.h - 26, 
            # "SKINS \nPRESS F", 
            # 8
        # )