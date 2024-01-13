input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def q2(input):
    return [x**2 for x in input if x % 2 == 0]

print(q2(input))