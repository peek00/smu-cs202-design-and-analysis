from collections import defaultdict

input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 12, 1, 3, 5]

def q1(input):
    map = defaultdict(int)
    for i in input:
        map[i] += 1
    return map

print(q1(input))

