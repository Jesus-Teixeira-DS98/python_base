"""
 using string concatenation in python with f string and format sintax
"""

name       = input('Name: ')
age        = input('Age: ') 
city       = input('City: ')
profession = input('Profession: ')
hobby      = input('Hobby: ')

madlib = f"Hi, my name is {name} I am {age} years old and I live in {city}. \n I'm a {profession}, during the weekends I like to spend my time {hobby}"

print(madlib)
print("Hi, my name is {} I am {} years old and I live in {}. \n I'm a {}, during the weekends I like to spend my time {}".format(name, age, city, profession, hobby))