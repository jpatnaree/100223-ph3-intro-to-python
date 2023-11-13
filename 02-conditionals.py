########### Conditionals ###########

# JS:
# let name = "Bob"
name = "Rocket"

# if (name === "Bob") {
#     console.log("OMG it's Bob!")
# } else {
#     console.log(`Hello ${name} the raccoon`)
# }

if name == "Bob":
    print("OMG it's Bob!")
else:
    print(f'Hello {name} the raccoon')


name = "Raphael"

# if (name === "Donatello" || name === "Raphael") {
#     console.log("Cowabunga dude!")
# } else if (name === "Leonardo" || name === "Michelangelo") {
#     console.log("It's turtle time!")
# }

if name == "Donatello" or name == "Raphael":
    print("Cowabunga dude!")
elif name == "Leonardo" or name == "Michelangelo":
    print("It's turtle time!")

print("Free Pineapple Pizza on Tuesdays!")

weekday = "Sunday"
# let myPizza = weekday === "Tuesday" ? "Pineapple Pizza" : "Pepperoni Pizza"

my_pizza =  "Pineapple Pizza" if weekday == "Tuesday" else "Pepperoni Pizza"

print(my_pizza)

print(f"Free {my_pizza} on {weekday}!")

test_pizza = "Pizza 1" if weekday == "Monday" else "Momo Pizza" if weekday == "Wednesday" else "Veggie Pizza"

print(test_pizza)