import sys

def binary_exponention(m,k,n): # 2 ^ 12 
    # Approach found through ChatGPT
    # Me trying to convince myself I understand how it works
    # 2 ^ 12 = 2^(2*6) = 4^6 = 4^(2*3) = 16^3 = 16^(2*1) = 256 * 16
    # If the original number is 0 or 1, it will always be 1
    if m == 0 or m == 1: 
        return 1
    
    if k == 0:
        return 1
    res = binary_exponention(m, k // 2, n) # 2 ^ 6
    if k % 2 : # 12
        return (res * res * m) % n # Taking modulo at every step makes it faster
    else:
        return (res * res) % n
    
def power_modulo(m, k, n):
    m = m % n
    res = binary_exponention(m, k, n)
    return res

num_line = int(sys.stdin.readline())

for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    m, k, n = a[0], a[1], a[2]
    print(power_modulo(m, k, n))
