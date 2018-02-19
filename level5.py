#assign 79
def sum(n):
    result = 0
    i = 0
    while i <= n:
        result += i
        i += 1
    return result

print(sum(8))

#assign 80
def sum_with_range(begin, end, step):
    newBegin = begin
    sum = 0
    while newBegin <= end:
        sum += newBegin
        newBegin += step
    return sum

print(sum_with_range(1, 13, 2))

#assign 81
def squares(number):
    for num in range(1,number + 1):
        print(num ** 2)
squares(5)

#assign 98
ops = {
       "+": (lambda a, b: a + b),
       "-": (lambda a, b: a - b),
       "*": (lambda a, b: a * b),
       "/": (lambda a, b: a / b)
}

def eval(expression):
    tokens = expression.split(" ")
    stack = []

    for token in tokens:
        if token in ops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = ops[token](arg1, arg2)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()

print(eval("1 2 +"))
print(eval("990 1 2 + *"))

#assign 99
def eval_prefix(expression):
    tokens = list(reversed(expression.split(" ")))
    stack = []

    for token in tokens:
        if token in ops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = ops[token](arg1, arg2)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()

print(eval_prefix("* + 2 1 990"))

"1 + 23 + 23"

#assign 102
def nth_character(string, number):
    chars = list(string)
    print(chars[number])

nth_character("qwe",1)

#infix evaluation

def eval_infix(expression):
    tokens = expression.split(" ")
    stack = []
    
    for token in tokens:
        if token in ops:
            stack.append(token)
        else:
            if stack:
                operator = stack.pop()
                arg1 = stack.pop()
                result = ops[operator](int(arg1), int(token))
                stack.append(result)
            else:
                stack.append(token)
    return stack.pop()
                      
print(eval_infix("1 + 2 / 3"))






