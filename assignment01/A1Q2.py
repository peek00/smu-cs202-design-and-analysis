# # num_line = int(sys.stdin.readline())
# # gn, gc = 0, [[1]]
# # for _ in range(num_line):
# #     a = [int(s) for s in sys.stdin.readline().split()]
# #     n, m = a[0], a[1]
# #     p10_lines(n, m)
from math import comb

def p10_lines(n,m):
    c = get_element(n,m,10)
    print(c)

def get_largest_choice(a:int, b:int, x:int)->int:
    v = a - 1
    while get_number_of_combinations(v,b) > x:
        print(v,b, get_number_of_combinations(v,b), x)
        v -= 1
    return v

def get_number_of_combinations(n,k):
    return comb(n,k)

def get_element(n, m, target): #n = 7, m =4
    total_combinations = get_number_of_combinations(n,m) - 1 # to account for 0 index
    print(n,m,target)
    combination = [0] * m 
    a = n
    b = m
    x = total_combinations - target
    print("Hi")
    print(a,b, x)

    for i in range(m):
        print(a,b,x)
        combination[i] = get_largest_choice(a, b, x)
        x -= get_number_of_combinations(combination[i], b)
        a = combination[i]
        b -= 1

    for i in range(m):
        combination[i] = (n - 1) - combination[i]

    return combination

if __name__ == "__main__":
    print(get_number_of_combinations(7,4))
    n = 7
    m = 4
    p10_lines(n,m)