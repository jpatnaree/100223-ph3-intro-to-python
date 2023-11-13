########### Lists ###########

# JS:
# const animals = ["Aardvark", "Bobcat", "Cardinal", "Deer"]
# console.log(animals)

#list 

animals = ["Aardvark", "Bobcat", "Cardinal", "Deer"]

# console.log(`First animal: ${animals[0]}`)
print(animals)

# animals.push("Elephant")
# console.log(animals)
animals.append("Kiwi Bird")
animals.append("Kangaroo")
print(animals)

# animals.pop()
# console.log(animals)
animals.insert(0, "Dingo")
animals.insert(5, "Dingo")
print(animals)

# console.log(`There are ${animals.length} animals`)
print(len(animals))

animals.remove("Dingo") # equal find 1st "Dingo" and remove it
print(animals)

animals.pop()
print(animals)
animals.pop(1)
print(animals)

# const randomAnimal = animals[Math.floor(Math.random() * animals.length())]
# console.log(randomAnimal)
from random import choice
print(choice(animals))

# const firstTwoAnimals = animals.slice(0, 2)
# console.log(`First two animals: ${firstTwoAnimals}`)

animals[2:]
animals[:2]
animals[1:3]

# const lastAnimal = animals[animals.length - 1]
# console.log(lastAnimal)
animals[-2:]


# function printEachAnimal() {
#     for (let i = 0; i < animals.length; i++) {
#         console.log( animals[i] )
#     }
# }

def print_each_animal():
    for animal in animals:
        print(animals)

print(print_each_animal())

# printEachAnimal()

# const animalsToLowerCase = animals.map( animal => animal.toLowerCase() )
# console.log(animalsToLowerCase)

lower_case_animals = [animal.lower for animal in animals] # => equal .map()
# print(lower_case_animals)

# also.... WHAT THE HECK IS A TUPLE???
#tuple is immutable Data => kinda equal to const variable

my_tuple = ("Kitty", "Onyx", "Zilly")
print(my_tuple[2])
my_tuple = list(my_tuple)
print(my_tuple) # can be convert into list to be mutable

my_one_item_tuple = ("Kitty",) # always need , to make it tuple
print(type(my_one_item_tuple))

print(tuple(animals)) # this create whole new tuple => non destructive => not mutate the original list
print(animals)