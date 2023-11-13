########### Additional Python Exercises ###########

##### square_number #####

# Create a function called 'square_number'. 

# It accepts one number as an argument. 

# It returns the number squared.
import math

def square_number(number):
    return number ** 2

print(square_number(9))

def sqaure_root(number):
    return math.sqrt(number)

print(sqaure_root(9))
##### sum_list #####

# Create a function called 'sum_list'. 

# It accepts a list of numbers as an argument (for example [1,2,3]). 

# It returns the sum of all the numbers inside the list (the return from the example would be 6).

def sum_list(list):
    return sum(list)

def sum_list2(list):
    sum = 0
    for element in list: #take every index in list and add to the next one
        sum += element
    return sum
def sum_list3(list):
    total = 0
    for num in list:
        total += num
    return total

print(sum_list([1,2,3]))

##### farenheit_to_celcius #####

# Create a function called 'farenheit_to_celcius'. 

# It accepts a number as an argument which represents a temperature in farenheit. 

# It returns the temperature in celsius. You will have to look up the math to convert it.

# If the number is a float, round down to the nearest whole number.

def farenheit_to_celcius(farenheit):
    return ((farenheit - 32) /9) * 5 # (farenheit - 32) * (5/9)

print(farenheit_to_celcius(100))
##### is_planet #####

# Create a function called 'is_planet'. 

# It accepts a string as an argument. 

# If that string is a planet in our solar system ('Mercury', 'Venus', 'Earth', etc.) return True and otherwise return False.

# This ought to work regardless of capitalization and whitespace.

def is_planet(string):
    return True if string.lower().capitalize() in ["Mercury", "Venus", "Earth", "Jupiter", "Saturn", "Uranus", "Neptune", "Mars"] else False

# def is_planet(string:)
print(is_planet("mercury"))
print(is_planet("Sun"))

def is_planet2(string):
    string = string.title().strip()
    planet = ["Mercury", "Venus", "Earth", "Jupiter", "Saturn", "Uranus", "Neptune", "Mars"] 
    return string in [pl. title() for pl in planet]

print(is_planet2("mars"))
##### is_palindrome #####

# Create a function called 'is_palindrome'. 

# It accepts a string as an argument. 

# If the string is a palindrome (it's the same forward as backwards) then return True, otherwise return False. An example of a palindrome is 'abba' or 'radar'.

# As an additional challenge the function ignores white space so something like 'taco cat' would also be considered a palindrome.

def is_palindrome(string):
    string = "".join(string.split())
    if string.lower().capitalize() == (string[::-1]).lower().capitalize():
        return True
    else:
        return False
    
print(is_palindrome("taco cat"))

def is_palindrome2(string):
    new_string = string.replace(" ", "").lower()
    return new_string == new_string[::-1]

is_palindrome2("a man a plan a canal panama")