class BlockList:
    def __init__(self, blocks):
        self.blocks = blocks
        self.death_list = []
        
        self.initDestructList()
    
    def initDestructList(self):
        for b in self.blocks:
            if b.group == 'DESTRUCT':
                self.death_list.append(b)
    
    def reinitList(self):
        pass
    
    def delBlock(self, block):
        self.death_list.remove(block)