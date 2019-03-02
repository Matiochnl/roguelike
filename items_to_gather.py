import random


 def weapons():
    weapons_list = [("sword", 3), ("axe", 4), ("stick", 1),
                    ("spear", 9), ("stone", 6)]
    return weapons_list[random.randint(0, len(weapons_list)-1)]


 def food():
    food_list = [("ham", 8), ("meat", 6), ("melon", 6), ("pear", 5),
                 ("potato", 5), ("green peas", 4)]
    return food_list[random.randint(0, len(food_list)-1)]


 def clothes():
   clothes_list = [("silver helmet", 1), ("plate armor", 4),
                    ("wooden shield", 1), ("leather armor", 2),
                    ("steel boots", 1)]
    return clothes_list[random.randint(0, len(clothes_list)-1)]