#import ingredients
from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Egg, Flour, Milk, Butter, Salt

#whisking the eggs in a bowl, until frothy
bowl = Bowl.use(name='batter')
for egg in Egg.take(2):
    egg.crack()
    bowl.add(egg)
bowl.mix()

#add a dash of salt
bowl.add(Salt.take('dash'))

#mix in all the flour (250g) in batches of 50g
flour1 = Flour.take(grams=50)
bowl.add(flour1)
bowl.mix()
flour2 = Flour.take(grams=50)
bowl.add(flour2)
bowl.mix()
flour3 = Flour.take(grams=50)
bowl.add(flour3)
bowl.mix()
flour4 = Flour.take(grams=50)
bowl.add(flour4)
bowl.mix()
flour5 = Flour.take(grams=50)
bowl.add(flour5)
bowl.mix()

#add in half the milk
milk1 = Milk.take(ml=250)
bowl.add(milk1)
#mix thoroughly
bowl.mix()
#add in the other half
milk2 = Milk.take(ml=250)
bowl.add(milk2)

#check
Rosemary.taste(bowl)

#pre-grease pan, add a little butter before baking each pancake
pan = Pan.use(name='pancakes')
plate = Plate.use()
for i in range (8):
    pan.add(Butter.take('slice'))
    pan.add(Salt.take('dash'))

    #8 pancakes in total
    pan.add(bowl.take('1/8'))
    #bake each pancake on both sides, until golden brown (roughly 60 seconds per side, several alternations of baking side usually gives the best result)
    for i in range (4):
        pan.cook(minutes=.5)
        pan.flip()
    pancakes = pan.take()
    plate.add(pancakes)

Rosemary.serve(plate)