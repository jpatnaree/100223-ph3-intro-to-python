########### Variables ###########

# JS:
# let name = "Bob"
# console.log(name)
name = "Bob"
name = "Billy"
print(name)

# let species = "Raccoon"
# console.log(species)
species = "Raccoon"
print(species)

# let rabid = false
# console.log(rabid)
rabid = True
rabid = False
print(rabid)

# name = `Bob the ${species}`
# console.log(name)
name = f'Rocket the {species}'
print(name)

numberOfRaccoonsInNYC = "300"
# console.log( `number of raccoons in NYC: ${numberOfRaccoonsInNewYork}` )

print(f'There are {numberOfRaccoonsInNYC} racoons in NYC')


# numberOfRaccoonsInNewYork = parseInt( numberOfRaccoonsInNewYork )
print(int("6000"))
numberOfRaccoonsInNYC = int(numberOfRaccoonsInNYC)


# numberOfRaccoonsInNewYork += 1
# console.log( `number of raccoons in NYC: ${numberOfRaccoonsInNewYork}` )
print(type(numberOfRaccoonsInNYC))
numberOfRaccoonsInNYC += 1
numberOfRaccoonsInNYC += 2
numberOfRaccoonsInNYC -= 2
print(numberOfRaccoonsInNYC)

# const minutesPerHour = 60
# minutesPerHour = 55 // in JS this will break!
# console.log(minutesPerHour)
minutes_per_hour = 60 # equal let
MINUTES_PER_HOUR = 55 # equal const // doesn't do anything under the hood => just to notify other developer