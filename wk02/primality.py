import math, time
import pandas as pd

def naive(upper_bound):
    prime = [2]
    for i in range(3, upper_bound, 2):
        for j in range(3, i, 2):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime

def improved(upper_bound): 
    prime = [2]
    for i in range(3, upper_bound, 2):
        found = False
        stop = math.floor(math.sqrt(i))
        for j in prime: # try only those identified primes 
            if i % j == 0:
                found = True
                break
            if j > stop:
                break
        if not found:
            prime.append(i)
    return prime

def sieve(upper_bound):
    flag = [True] * (upper_bound + 1) # all numbers are initially considered potentially prime
    prime = []
    for i in range(2, upper_bound + 1):
        if flag[i]:
            for j in range(2 * i, upper_bound + 1, i):
                flag[j] = False # any number which is a multiple of some other number is not a prime
            prime.append(i)
    return prime

if __name__ == '__main__':
    runtime = []
    for i in range(4, 9, 4):
        upper_bound = 1 << i
        start = time.time()
        naive(upper_bound)
        time_n = time.time() - start
        start = time.time()
        improved(upper_bound)
        time_i = time.time() - start
        start = time.time()
        sieve(upper_bound)
        time_s = time.time() - start
        runtime.append([i, time_n, time_i, time_s])
    df = pd.DataFrame.from_records(runtime, columns = ['bits', 'naive', 'improved', 'sieve'], index = 'bits')
    df.plot(xticks = list(range(4, 9, 4)))
