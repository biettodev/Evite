import pyxel
from time import sleep

from constants import *

from bodies.Player import Player
from bodies.Body import Body
from bodies.Gems import *
from bodies.AvoidObjects import *

from resources.sprites import sprites

from data.blocksData import list1, list2, list3, list4, list5
from BlockList import BlockList

from Caroussel import Caroussel

from ui.MainMenuScreen import MainMenuScreen
from ui.GameScreen import GameScreen
from ui.GameOverScreen import GameOverScreen
from ui.SkinsMenuScreen import SkinsMenuScreen

from LevelsHandler import LevelsHandler
from collisionHandler import hasCollision
from listHandler import *
from screensHandler import *

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption=WINDOW_TITLE)

        self.w = pyxel.width
        self.h = pyxel.height
        self.borders = BORDERS
        self.level = 1
        
        sprites()
        
        # Fireball
        self.player = Player(40, 50, {'w':10, 'h':10}, 9)  
        
        self.blockList1 = BlockList(list1)
        self.blockList2 = BlockList(list2)
        self.blockList3 = BlockList(list3)
        self.blockList4 = BlockList(list4)
        self.blockList5 = BlockList(list5)
        
        self.allLists = [
            self.blockList1,
            self.blockList2, 
            self.blockList3,
            self.blockList4, 
            self.blockList5
        ]
        
        # self.allLists = {
            # 'level 1':self.blockList1,
            # 'level 2':self.blockList2, 
            # 'level 3':self.blockList3,
            # 'level 4':self.blockList4, 
            # 'level 5':self.blockList5
        # }
        
        for bl in self.allLists:
            Caroussel(bl.blocks)
        
        self.levelsHandler = LevelsHandler(self.allLists)
        self.actlist = self.levelsHandler.init_level
        
        self.mainMenuScreen = MainMenuScreen(self.w, self.h)
        self.gameScreen = GameScreen(self.player, self.actlist.blocks)
        self.gameOverScreen = GameOverScreen()
        self.skinsMenuScreen = SkinsMenuScreen(-10, -10, 10, 10, 3)
        
        self.actscreen = MAIN_MENU_SCREEN
        
        pyxel.run(self.update, self.draw)
    
    def endGame(self, status):
        self.actscreen = GAMEOVER_SCREEN
        if status:
            self.end_game_screen = 'WIN'
        else:
            self.end_game_screen = 'LOSE'
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q): pyxel.quit()
        
        self.player.checkOnLimit(self.borders['top'])
                
        handleScreenUpdate(self, self.actscreen, MAIN_MENU_SCREEN, GAME_SCREEN, GAMEOVER_SCREEN, SKINS_MENU_SCREEN)
        
    def update_main_menu_screen(self):
        if pyxel.btnp(pyxel.KEY_ENTER):
            self.actscreen = GAME_SCREEN
        if pyxel.btnp(pyxel.KEY_F):
            self.actscreen = SKINS_MENU_SCREEN
            
    def update_game_screen(self):
        for b in self.actlist.blocks:
            if hasCollision(b, self.player):
                if b.group == 'AVOID':
                    b.giveDamage(self.player)
                    if type(b) is DBlock: b.decreaseSpeed(self.player)
                        
                elif b.group == 'DESTRUCT':
                    b.die()
                    self.actlist.delBlock(b)
                    if type(b) is Ruby: b.setSpecial()
                    if type(b) is Saphire: b.setSpecial(self.player)
                    if type(b) is Emerald: b.setSpecial()
                    if len(self.actlist.death_list) < 1:
                        self.endGame(status=1)
                        self.levelsHandler.update()
                        self.actlist = self.levelsHandler.next_level
                        self.level += 1
                    
        self.player.update()
        
        cleanup_list(self.actlist.blocks)
        update_list(self.actlist.blocks)
        
    def update_gameover_screen(self):
        self.gameOverScreen.nextLevel(self.level)
        if pyxel.btnp(pyxel.KEY_ENTER):
            self.gameScreen.update(self.actlist.blocks)
            self.actscreen = GAME_SCREEN
        
        self.player.update()
        
        update_list(self.actlist.blocks)
        cleanup_list(self.actlist.blocks)
    
    def update_skins_menu_screen(self):
        pass
    
    def draw(self):
        pyxel.cls(7)
        
        handleScreenDraw(self, self.actscreen, MAIN_MENU_SCREEN, GAME_SCREEN, GAMEOVER_SCREEN, SKINS_MENU_SCREEN)
        
App()
