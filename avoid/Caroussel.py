class Caroussel:
    def __init__(self, car_objects):
        self.car_objects = car_objects
        self.initCaroussel(self.car_objects)
        
    def initCaroussel(self, car_objects):
        for i, b in enumerate(car_objects):
            b.posx = (20 * (i+1))