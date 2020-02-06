animal_types = ['bird', 'dog', 'cat']

print(animal_types)

new_animal = input("enter a new animal: ")

animal_types.append(new_animal)

print(animal_types)



import random
coin = ('Heads', 'tails')
flip = random.choice(coin)
your_choice = input("Pick Heads or tails: ")
Heads, tails = 0, 0
games = 0
print("Hit X to exit game.")

