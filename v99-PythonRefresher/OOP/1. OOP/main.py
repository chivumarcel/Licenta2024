from Enemy import *

enemy = Enemy('Cucubau', 30, 10)
enemy.get_type_of_enemy()
big_zombie = Enemy('Big shit zomb', 50, 20)

big_zombie.type_of_enemy = "Bazooka"
# print(zombie)

# zombie.type_of_enemy = 'Zombie'
# zombie.health_points = 40
# zombie.attack_damage = 10
print(f'{enemy.get_type_of_enemy()} has {enemy.health_points} health points and can do attack of {enemy.attack_damage}')

#print(f'{zombie.type_of_enemy} has {zombie.health_points} health points and can do attack of {zombie.attack_damage}')
print(f'{big_zombie.type_of_enemy} has {big_zombie.health_points} health points and can do attack of {big_zombie.attack_damage}')


# zombie.talk()
# zombie.walk_forward()
# zombie.attack()

big_zombie.talk()
big_zombie.walk_forward()
big_zombie.attack()

# enemy = Enemy ('zombie2', 15, 4)
# print(f'{enemy.type_of_enemy} has {enemy.health_points} health points and can do attack of {enemy.attack_damage}')