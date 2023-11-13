##### Scope #####

# Global variables #

# JS:

# let name = "Bob the Raccoon"

name = "Bob the Raccoon"

for item in range(6):
    print(name)

def say_hi():
    print(f"hi {name}")
say_hi()

def change_name(new_name):
    name = new_name
    print(name)

change_name("Milly")
print(name)

def change_name(new_name):
    global name
    name = new_name

change_name("Milly")
print(name)

def outer_function():
    outer_var = "whatever"

    def inner_function():
        # global outer_var
        outer_var = "new stuff"
    
    inner_function()
    return outer_var

print(outer_var)
print(outer_function())

newthing = outer_function()
print(newthing)

# for (let i = 0; i < 5; i++) {
#   console.log(`Hello ${name}`)
# }

# function sayHiToBob() {
#   console.log(`Hello ${name}`)
# }

# function changeName(newName) {
#   name = newName
# }

# changeName("Rocket")

# console.log(name)



# Closure #

# JS:

# function speechGenerator(introduction) {
#   return function(speech) {
#     return `${introduction} ${speech}`
#   }
# }

# const fourScore = speechGenerator("Four score and seven years ago")

# const newSpeech = fourScore("something something speech goes here")

# console.log(newSpeech)