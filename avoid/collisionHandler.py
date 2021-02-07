def collidex(obj1, obj2):
    inter = set.intersection(set(obj1), set(obj2))
    
    if len(inter) > 0:
        return True
        
def collidey(obj1, obj2):
    inter = set.intersection(set(obj1), set(obj2))
    
    if len(inter) > 0:
        return True

def hasCollision(obj1, obj2):
    if collidey(obj1.maskInx(), obj2.maskInx()) and collidex(obj1.maskIny(), obj2.maskIny()):
        return True
    else:
        return False