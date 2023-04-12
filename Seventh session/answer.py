# question 1 : max
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [1,2,3,4,5,32,43,12,46,86,75]
print(find_largest(numbers))

# question 2 : join strings
def join_strings(*args):
    final_string = ''
    for arg in args:
        final_string += str(arg) + ' '
    return final_string

print(join_strings("amir hossein","hi my name is amir", 23, 12,"abcd"))

# question 3 : factorial
def calc_factorial(num):
    if num == 1:
        return 1
    else:
        return num * calc_factorial(num-1)

def calc__factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

print(calc_factorial(5))
print(calc__factorial(5))

# question 4 : two func and flag

def myFunction(flag, values):
    if flag == 1:
        print(find_largest(values))
    elif flag == 0:
        print(calc_factorial(values))
    else:
        print("Invalid flag!")

myFunction(0,4)
myFunction(1,[1,5,2,10,-2])

