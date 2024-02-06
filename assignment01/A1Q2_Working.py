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
    3. Modified get_element to be a recursive function instead

    """
    # Get number of combination
    number_of_combinations = comb(n,m) # Sources state that this complexity is O(n**2)
    target = 0
    for i in range(len(str(number_of_combinations))): # O()
        res = get_element(n,m,target)
        # Increment from 0,9,99,999...
        target += 9 * max(1, 10 ** i)  
        results.append(", ".join([str(x) for x in res]))

def get_largest_choice(a:int, b:int, x:int)->int:
    v = a - 1
    while comb(v,b) > x:
        v -= 1
    return v

def get_element(n, m, target): 
    # Account for Python's 0 index
    total_combinations = comb(n,m) - 1 
    combination = [0] * m 
    # Making copies as we have to modify a,b
    a,b  = n,m
    # x is the `dual`
    x = total_combinations - target
    # Finding the combinandic of x
    for i in range(m):
        combination[i] = get_largest_choice(a, b, x)
        x -= comb(combination[i], b)
        a = combination[i]
        b -= 1

    # Taking the inverse of combinadic 
    for i in range(m):
        combination[i] = (n - 1) - combination[i]

    return combination

def binomial_coefficient(n, k):
    # O(n**2k)
    # Initialize the array to store binomial coefficients
    dp = [0] * (k + 1)
    dp[0] = 1  # Base case: C(n, 0) = 1

    # Iterate over the numbers 1 to n
    for i in range(1, n + 1):
        # Compute the binomial coefficient for current row
        for j in range(min(i, k), 0, -1):
            dp[j] = dp[j] + dp[j - 1]

    return dp[k]

num_line = int(sys.stdin.readline())
results = []
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, m = a[0], a[1]
    A1Q2(n, m, results)

for res in results:
    print(res)