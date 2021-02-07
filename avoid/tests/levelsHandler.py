def handlerLevels():
    if len(self.actlist.death_list) < 1: 
        self.endGame(status=1)
        if self.actlist == self.blockList1:
            self.actlist = self.blockList2
        elif self.actlist == self.blockList2:
            self.actlist = self.blockList3
        elif self.actlist == self.blockList3:
            self.actlist = self.blockList4
        elif self.actlist == self.blockList4:
            self.actlist = self.blockList5