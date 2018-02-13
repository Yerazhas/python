#assign 49
def identify(parameter):
    return type(parameter)

print(identify(str(23.4)))

#assign 50
def get_area_of_triangle_from(base, height):
    return base * height / 2

print(get_area_of_triangle_from(2, 4))

#assign 51
def get_quotient_from(number, divisor):
    return float(number) / float(divisor)

print(get_quotient_from("14", 5))

#assign 52
def get_remainder(number, divisor):
    return number - number / divisor * divisor
print(get_remainder(19, 4))

#assign 53
def is_equal(first, second):
    return first == second

print(is_equal("asd", "asd"))

#assign 54
def clarify_sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0
print(clarify_sign(-0))

#assign 55
def check_for_six(firstNumber, secondNumber):
    sum = firstNumber + secondNumber
    diff = abs(firstNumber - secondNumber)
    return (firstNumber == 6 or secondNumber == 6) or (sum == 6) or (diff == 6)

print(check_for_six(4, 3))

#assign 56
def isTriangle(firstNumber, secondNumber, thirdNumber):
    firstSum = firstNumber + secondNumber
    secondSum = secondNumber + thirdNumber
    thirdSum = thirdNumber + firstNumber
    return firstSum > thirdNumber and secondSum > firstNumber and thirdSum > secondNumber
print(isTriangle(1,4,5))

#assign 57
def calculate_result(firstDigit, secondDigit, thirdDigit):
    all_are_two = firstDigit == 2 and secondDigit == 2 and thirdDigit == 2
    all_are_same = (firstDigit == secondDigit) and (secondDigit == thirdDigit)
    all_are_not_same = firstDigit != secondDigit and secondDigit != thirdDigit
    if all_are_two:
        return 10
    elif (not all_are_two) and (all_are_same):
        return 5
    elif (all_are_not_same):
        return 1
    else:
        return 0

print(calculate_result(1,3,3))

#assign 58
def alarm_clock(day, is_vacation):
    for i in range(1,10):
        print(i)

alarm_clock(1,True)








