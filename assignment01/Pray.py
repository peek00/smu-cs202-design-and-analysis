# To find the combination element for index m, 
# first find its dual and call it x. 
# Next, find the combinadic of x. 
# Then subtract each digit of the combinadic of x from n-1 
# the result is the mth lexicographic combination element.
from math import comb
from typing import List
from collections import deque

def Element(m: int, n: int, k: int) -> List[int]:
    """
    Computes the element [m] using the combinadic.

    Parameters:
    - m: Target index of the combination.
    - n: Total number of items.
    - k: Size of combinations.

    Returns:
    - List of integers representing the element.
    """
    maxM = comb(n, k) - 1
    print(n,k,comb(n,k))
    print(m, maxM)

    if m > maxM:
        raise ValueError("m value too large in Element")

    ans = [0] * k

    a = n
    b = k
    x = maxM - m  # x is the "dual" of m

    for i in range(k):
        ans[i] = LargestV(a, b, x)  # see helper below
        x -= comb(ans[i], b)
        a = ans[i]
        b -= 1

    for i in range(k):
        ans[i] = (n - 1) - ans[i]

    return ans

def LargestV(a: int, b: int, x: int) -> int:
    """
    Helper function to find the largest v satisfying Choose(v,b) <= x.

    Parameters:
    - a: Value of a.
    - b: Value of b.
    - x: Value of x.

    Returns:
    - Largest value of v.
    """
    v = a - 1
    while comb(v, b) > x:
        v -= 1
    return v


def binom(n,k):
    if k == 0 or k == n:
        return 1
    return binom(n-1, k-1) + binom(n-1, k)

def jamesmccaffrey(n, m, target=0):
    # Find its dual
    combinations = binom(n, m)
    dual = combinations - target - 1 # -1 to account for Python 0 index

    # Find combinadic of x

    pass

    pass

if __name__ == "__main__":
    print(binom(7,4)) # 35
    print(Element(8,7,4))