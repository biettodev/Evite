def handleScreenUpdate(dad, screen, scene1, scene2, scene3, screen4):
    if screen == scene1:
        dad.update_main_menu_screen()
    elif screen == scene2:
        dad.update_game_screen()
    elif screen == scene3:
        dad.update_gameover_screen()
    # elif screen == screen4:
        # dad.update_skins_menu_screen()

def handleScreenDraw(dad, screen, scene1, scene2, scene3, screen4):
    if screen == scene1:
        dad.mainMenuScreen.draw()
    elif screen == scene2:
        dad.gameScreen.draw()
    elif screen == scene3:
        dad.gameOverScreen.draw(dad.end_game_screen)
    # elif screen == screen4:
        # dad.skinsMenuScreen.draw()