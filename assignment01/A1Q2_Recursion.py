import sys
from math import comb

def A1Q2(n,m):
    # Get number of combination
    number_of_combinations = get_number_of_combinations(n,m)
    target = 0
    results = []
    for i in range(len(str(number_of_combinations))):
        res = get_element(n,m,target, number_of_combinations, res)
        #0, 9, 99
        target += 9 * max(1, 10 ** i)  # Update target based on the logic
        results.append(", ".join([str(x) for x in res]))

def get_largest_choice(a:int, b:int, x:int)->int:
    v = a - 1
    while get_number_of_combinations(v,b) > x:
        v -= 1
    return v

def get_number_of_combinations(n,m):
    return comb(n,m)

def get_element(n, m, target): #n = 7, m =4
    total_combinations = get_number_of_combinations(n,m) - 1 # to account for 0 index
    combination = [0] * m 
    a = n
    b = m
    x = total_combinations - target

    for i in range(m):
        combination[i] = get_largest_choice(a, b, x)
        x -= get_number_of_combinations(combination[i], b)
        a = combination[i]
        b -= 1

    for i in range(m):
        combination[i] = (n - 1) - combination[i]

    return combination


num_line = int(sys.stdin.readline())
results = []
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, m = a[0], a[1]
    results.append(A1Q2(n, m, results))

for res in results:
    print(res)