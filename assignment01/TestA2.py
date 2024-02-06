import sys

def your_function(n,m):
    # Use this as a wrapper function to call your combinadics
    print("Calling!")

num_line = int(sys.stdin.readline())
gn, gc = 0, [[1]]
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, m = a[0], a[1]
    your_function(n, m)
