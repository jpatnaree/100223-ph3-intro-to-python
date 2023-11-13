########### Functions ###########

# JS:
# function doStuff() {
#   return "This function does stuff!"
# }
def do_stuff():
    return "This function does stuff!"

# console.log( doStuff() )
print(do_stuff())

# function addition(x,y) {
#   return x + y
# }
def addition(x,y):
    return x + y

print(addition(4,4))
print(addition(-1.88,8))
print(addition("fast","food"))

# console.log( addition(1,2) )
# console.log( addition("3", 4) )
# console.log( addition(5.6, 7) )

# let name = "Bob"

# function sayHiBob() {
#   return `Hello ${name}`
# }

# console.log( sayHiBob() )

# function countdown(number) {
#   let i = number
#   while (i > 0) {
#     console.log(i)
#     i -= 1
#   }
#   console.log('HAPPY NEW YEAR!')
# }
def countdown(number = 10):
    i = number
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
# countdown()

def countdown2(number = 10):
    i = number
    while i > 0:
        print(i)
        i -= 1
        print("Happy New Year!")
# countdown2()

from time import sleep # resverse syntax comparet to JS
countdown()