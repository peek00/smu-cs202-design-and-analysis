import sys
from math import comb

def A1Q2(n,m, results = []):
    """
    Sources: 
    1. [Generation of a Vector from the Lexicographical Index](https://dl.acm.org/doi/10.1145/355732.355739)
    2. [Generating the mth lexicographical element of a combination using the combinaidc](https://jamesmccaffrey.wordpress.com/2022/06/28/generating-the-mth-lexicographical-element-of-a-combination-using-the-combinadic/)

    Algorithm below was adapted from the above sources. Changes made are to 
    1. account for Python 0 indexing
    2. Swap the order of parameters argumen - source n = k, and k = target
    3. Modified a part of get_element to be a recursive function instead for that extra 2 marks

    For this particular algorithm, I assume the complexity of math.comb(n,m) to be O(m).

    T(m) * O(a * comb(b)) * O(log base 10 * number of combinatiion)

    """
    # Get number of combination
    number_of_combinations = comb(n,m) # O(m)
    target = 0
    # Length of combination directly translate to how many results there will be.
    # Eg 9 combinations -> 1 iteration, 25 combinations -> 2 iterations, 133 combinations -> 3 iterations
    for i in range(len(str(number_of_combinations))): # O(log base 10 number_of_combinations)
        # T(m) * O(a * comb(b)) 
        res = get_element(n,m,target)
        # Increment from 0,9,99,999...
        target += 9 * max(1, 10 ** i)  
        results.append(", ".join([str(x) for x in res]))

def get_largest_choice(a:int, b:int, x:int)->int:
    # Complexity of this function is O(v * cost of dong comb(v,b) )
    v = a - 1
    while comb(v,b) > x: 
        v -= 1
    return v

def get_element(n, m, target): 
    # Account for Python's 0 index
    total_combinations = comb(n,m) - 1 # O(m)
    combination = [0] * m 
    # Making copies as we have to modify a,b
    a,b  = n,m
    # x is the `dual`
    x = total_combinations - target
     # T(m) * O(a * comb(b))
    get_combination_recursive(a, b, x, m , combination)    

    # Taking the inverse of combinadic 
    for i in range(m):
        combination[i] = (n - 1) - combination[i]

    return combination[::-1]

def get_combination_recursive(a, b, x, m, combination):
    # T(m) * O(a * comb(b))
    if m == 0:
        return

    combination[m - 1] = get_largest_choice(a, b, x) #O(a * comb(b))
    x -= comb(combination[m - 1], b)
    get_combination_recursive(combination[m - 1], b - 1, x, m - 1, combination)

num_line = int(sys.stdin.readline())
results = []
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, m = a[0], a[1]

    A1Q2(n, m, results)

for res in results:
    print(res)