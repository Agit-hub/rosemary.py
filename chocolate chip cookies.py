#import ingredients
from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl, BakingTray, Oven, Fridge
from kitchen.ingredients import Egg, Flour, Milk, Butter, Salt, Sugar, BakingPowder, ChocolateChips

# preheat oven 175
oven = Oven.use()
oven.preheat(degrees=175)

# one part butter 
bowl = Bowl.use(name='dough')
bowl.add(Butter.take(grams=150))

# mix  with 200 g sugar, little bits at a time, until your batter is smooth 
for i in range (4):
    bowl.add(Sugar.take(grams=50))
    bowl.mix()

# mix in each the two eggs
for egg in Egg.take(2):
    egg.crack()
    bowl.add(egg)
    bowl.mix()

# pinch of salt
bowl.add(Salt.take('dash'))

# add 300 grams of flour and 200 g of chocolate chip, in stages
for i in range (3):
    bowl.add(Flour.take(grams=100))
    bowl.mix()
for i in range (2):
    bowl.add(ChocolateChips.take(grams=100))

# add baking soda
bowl.add(BakingPowder.take('teaspoon'))

# baking tray: generous scoop of batter will form each cookie, leave some room between them
bakingtray = BakingTray.use(name='cookies')
plate = Plate.use()
for i in range (2):
    for i in range (12):
        bakingtray.add(bowl.take('1/24'))
    # cook 10
    oven.add(bakingtray)
    oven.bake(minutes=10)
    oven.take()
    cookies = bakingtray.take()
    plate.add(cookies)

# cool before serving
Rosemary.serve(plate)