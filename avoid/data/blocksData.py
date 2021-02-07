from bodies.AvoidObjects import SBlock, MBlock, LBlock, DBlock, MDBlock
from bodies.Gems import Gem, Ruby, Saphire, Emerald
from Sprite import Sprite

tam = {'w':7 ,'h':7}

sprPlant = Sprite({'simg':1, 'u':0, 'v':0, 'colk':0})

sblock_sprite = {'simg':1, 'u':0, 'v':0, 'colk':0}
mblock_sprite = {'simg':1, 'u':7, 'v':0, 'colk':0}
lblock_sprite = {'simg':1, 'u':16, 'v':0, 'colk':0}
dblock_sprite = {'simg':1, 'u':21, 'v':0, 'colk':1}
mdblock_sprite = {'simg':1, 'u':28, 'v':0, 'colk':1}

# Blocks avoid1
sblock1 = SBlock(0, 10, tam, sblock_sprite)
sblock2 = SBlock(0, 10, tam, sblock_sprite)
sblock3 = SBlock(0, 10, tam, sblock_sprite)
sblock4 = SBlock(0, 10, tam, sblock_sprite)
sblock5 = SBlock(0, 10, tam, sblock_sprite)

# Blocks avoid2
mblock1 = MBlock(0, 10, tam,  mblock_sprite)
mblock2 = MBlock(0, 10, tam, mblock_sprite)
mblock3 = MBlock(0, 10, tam, mblock_sprite)
mblock4 = MBlock(0, 10, tam, mblock_sprite)

# Blocks avoid3
lblock1 = LBlock(0, 10, tam, lblock_sprite)
lblock2 = LBlock(0, 10, tam, lblock_sprite)

# Blocks avoid4
dblock1 = DBlock(0, 10, tam, dblock_sprite)
dblock2 = DBlock(0, 10, tam, dblock_sprite)

# Block avoid5
mdblock1 = MDBlock(0, 10, tam, mdblock_sprite)
mdblock2 = MDBlock(0, 10, tam, mdblock_sprite)

ruby_animation = [
    {'simg':1, 'u':35, 'v':0, 'colk':0},
    {'simg':1, 'u':42, 'v':0, 'colk':0},
    {'simg':1, 'u':49, 'v':0, 'colk':0},
]
saph_sprite = {'simg':1, 'u':56, 'v':0, 'colk':1}
emer_sprite = {'simg':1, 'u':21, 'v':12, 'colk':1}

# Blocks destruct1
ruby1 = Ruby(0, 10, tam, ruby_animation)
ruby2 = Ruby(0, 10, tam, ruby_animation)
ruby3 = Ruby(0, 10, tam, ruby_animation)
ruby4 = Ruby(0, 10, tam, ruby_animation)
ruby5 = Ruby(0, 10, tam, ruby_animation)

# Blocks destruct2
saph1 = Saphire(0, 10, tam, ruby_animation)
saph2 = Saphire(0, 10, tam, ruby_animation)
saph3 = Saphire(0, 10, tam, ruby_animation)
saph4 = Saphire(0, 10, tam, ruby_animation)
saph5 = Saphire(0, 10, tam ,saph_sprite)

# Blocks destruct3
emer1 = Emerald(0, 10, tam, ruby_animation)
emer2 = Emerald(0, 10, tam, ruby_animation)
emer3 = Emerald(0, 10, tam, ruby_animation)
emer4 = Emerald(0, 10, tam, ruby_animation)
emer5 = Emerald(0, 10, tam, ruby_animation)

list1 = [sblock1, ruby1, sblock2, ruby2]
list2 = [ruby3, sblock3, saph1, mblock2, ruby4]
list3 = [sblock4, ruby5, sblock5, saph2, mblock3]
list4 = [saph3, lblock1, saph4, mblock4, emer1]
list5 = [emer2, dblock1, emer3]
