import math

#assign 22
print("hi"*3)

#assign 18
seconds_in_a_year = 365 * 24 * 60 * 60
print(str(seconds_in_a_year) + " seconds")

#assign 19
number_of_grains = 1
current_square = 1

while current_square < 64:
    number_of_grains *= 2
    current_square += 1
print(number_of_grains)

#assign 20
inches = 69
feet = 12 * inches

#assign 21
spam = "spam"
eggs = "eggs"
breakfast = spam + " and " + eggs
print(breakfast)

#assign 24
singpath_is_good = True
singpath_is_terrible = False
print(singpath_is_good, singpath_is_terrible)

#assign 25
def double(number):
    return 2 * number

random_number = 4
print(double(random_number))

#assign 26
def square(number):
    return number ** 2
print(square(34))

#assign 27
def increment(number):
    return number + 1
print(increment(4))

#assign 33
area = round(circle_area(10),5)
print(area)