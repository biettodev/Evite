class PlayerData:
    def __init__(self, file):
        self.file = file
        self.data = {
            'survival_level_id': 1,
            'survivel_life': 3,
            'casual_score': 0,
            'survival_skins': 0,
            'casual_skins': 0
        } 
    
    def viewData(self):
        return self.data
             
    # def increaseCScore(self, points):
        # self.data['casual_score'] += points
        # self.recordData(self.data['casual_score'])
        
    def recordData(self, data):
        data = open(self.file, 'a')
        data.write(f'{data}')