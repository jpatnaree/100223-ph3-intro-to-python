########### Dictionaries ###########

# JS:
# const teacher = {
#     name: "Chett",
#     city: "Brooklyn",
#     numberOfCats: 2,
#     occupation: "Instructor",
# }

teacher  = {
    "name": "Chett",
    "city": "Brooklyn",
    "numberOfCats": 2,
    "occupation": "Instructor"}

print(teacher["name"])

teacher["cat_names"] = ["Octavia", "Ursular"]
print(teacher)

teacher["cat_names"] = ["Rose"]
print(teacher)

# print(teacher["age"]) # error key age does not exist

teacher["age"] = [None]
print(teacher["age"])


# print(dict(**teacher, height = 600, ))
new_teacher = {"eyesight" : 2020, **teacher}
print(new_teacher)

# console.log(teacher)
# console.log(teacher.name)

# teacher.name = "Ricardo"
# console.log(teacher.name)

# const teacher.catNames = ["Octavia", "Ursula"]
# const firstPet = teacher.catNames[0]
# console.log( `Teacher's First Pet: ${firstPet}` )

# const doesNotExist = teacher.age
# console.log(doesNotExist)

# teacher = {...teacher, age: 500}
# console.log(teacher)

