from typing import List
from math import comb
from typing import List
from math import comb
import sys

def Main():
    print("\nBegin combinadic demo ")

    numCombs = Choose(7, 4)
    print("Number (n=100, k=10) combinations: ")
    print(f"{numCombs:,}")

    n = 7
    k = 4
    m = 10
    c = Element(m, n, k)
    print("\nCombination m=[" + str(m) + "]" +
        " of C(n=100,k=10): ")
    ShowComb(c)

    print("\nEnd combinadic demo \n")

def ShowComb(comb: List[int]):
    n = len(comb)
    for i in range(n):
        print(comb[i], end=" ")
    print("")
# m = target, n = 7, k = m
def Element(m: int, n: int, k: int) -> List[int]:
    # compute element [m] using the combinadic
    maxM = Choose(n, k) - 1
    print(m,n,k)

    if m > maxM:
        raise Exception("m value too large in Element")

    ans = [0] * k
    
    a = n
    b = k
    x = maxM - m  # x is the "dual" of m
    print("Hi")
    print(a,b,x)

    for i in range(k):
        print(a,b,x)

        ans[i] = LargestV(a, b, x)  # see helper below
        x -= Choose(ans[i], b)
        a = ans[i]
        b -= 1

    for i in range(k):
        ans[i] = (n - 1) - ans[i]

    return ans

def LargestV(a: int, b: int, x: int) -> int:
    # helper for Element()
    v = a - 1
    while Choose(v, b) > x:
        v -= 1
    return v

def Choose(n: int, k: int) -> int:
    # number combinations
    if n < 0 or k < 0:
        raise Exception("Negative arg in Choose()")
    if n < k: return 0  # special
    if n == k: return 1  # short-circuit

    delta, iMax = (n - k, k) if k < n - k else (k, n - k)

    ans = delta + 1
    for i in range(2, iMax + 1):
        ans = (ans * (delta + i)) // i

    return ans

if __name__ == "__main__":
    Main()
