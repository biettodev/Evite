from time import sleep

class LevelsHandler:
    def __init__(self, levels_queue):
        self.levels_queue = levels_queue
        self.init_level = levels_queue[0]
        
    def toNextLevel(self):
        if len(self.levels_queue) > 0:
            self.next_level = self.levels_queue[0]
            
    def update(self):
        del self.levels_queue[0]
        self.toNextLevel()
    
