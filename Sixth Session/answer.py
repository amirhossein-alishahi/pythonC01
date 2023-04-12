# question 1 : Wow

def wow(n):
    final_str = "W"
    for i in range(n):
        final_str += "o"
    final_str += "w!"
    return final_str

n = int(input())
print(wow(n))

# question 2 : factorial

def calc__factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

print(calc__factorial(5))

# question 3 : compare

def eye_test():
    n = int(input())
    word_given = input()
    word_writen = input()
    if len(word_given) != len(word_writen):
        print("Words are not the same size")
        return
    if len(word_given) != n:
        print("Words not the same size az n")
        return

    mistake_count = 0
    for i in range(n):
        if word_given[i] != word_writen[i]:
            mistake_count += 1

    print(mistake_count)

eye_test()

# question 4 : pascal triangle

def pascal_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle


n = int(input("Enter the number of rows: "))
triangle = pascal_triangle(n)
for row in triangle:
    print(row)
