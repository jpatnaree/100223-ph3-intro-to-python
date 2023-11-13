##### Scope #####

# Global variables #

# JS:

# let name = "Bob the Raccoon"

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