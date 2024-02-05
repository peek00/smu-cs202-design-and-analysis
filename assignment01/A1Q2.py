import sys
import math

'''
def gen_comb1(n:int, m:int, p:int, s:str):
    if p == n:
        if m == 0:
            combs.append(s)
    else:
        gen_comb1(n, m-1, p+1, s+char[p]) # with the character s[start]
        gen_comb1(n, m, p+1, s) # skip the character s[start]

char = 'abcdefghij'
n, m, combs = len(char), 3, []
gen_comb1(n, m, 0, '')
print(combs)

def gen_comb2(n:int, m:int, p:int, q:int, s:str):
    # n, m: generate all combinations of m from n numbers 0, 1, 2,..., n-1
    # p: from which position to start choosing next integer
    # q: number of remaining numbers to be chosen
    if q == 0:
        combs.append(s)
    else:
        for i in range(p, n-q+1):
            gen_comb2(n, m, i+1, q-1, s+char[i])

char = 'abcdefghij'
n, m, combs = len(char), 3, []
gen_comb2(n, m, 0, m, '')
print(combs)

generate(10,3) -> generate 10c3 from 0,1,2,3,4,5,6,7,8,9

'''

def p10_lines(n, m):
    # Generage mCn from 0,1,2,...,m-1
    output = []
    pass

# number of unique sets = n-m+1

# gen(10,1) -> {0,1,2,3,4,5,6,7,8,9}
# n-m+1 = 10
# 0,1,2,3,4,5,6,7,8,9
# There are 10 sets, each set having one item
# There are n-1 sets, with m items each
# PRINT OUT 
# 0 
# 9

# gen(5,2) -> {0,1,2,3,4}, list 2- combinations
# n-m+1 = 4
# 01,02,03,04,12,13,14,23,24,34
# Length 4, 3, 2, 1
# There are 4 sets, starting with 4 items, then 3 items, then 2 then 1 item.
# There are n-1 sets starting with length of m
# 4 * 0 starting, 3 * 1 starting ...
# print out 
# 0,1 
# 3,4

# gen(6,3) -> {0,1,2,3,4,5}, list 3-combinations
# 10, 6, 3 , 1 <- actual length, decrease by 4 3 2 
# difference is 4, 3, 2
# 0, 10, 16, 19
# 012,013,014,015,023,024,025,034,035,045,123,124,125,134,135,145,234,235,245,345
# There are 4 sets, starting with 10 items, then 6, then 3, then 1
# print out
# 0,1,2
# 0,4,5

# n - m + 1

# Given (n,m), ...
# Given (6,3), can I get the numbers 10, 6 ,3 and 1?
# Given (5,2), can I get the numbers 4, 3, 2, 1?
# Given (10,1) can I get the numbers 1,1,1,1,1,1,1,1?

# A MAJOR set is a set that has the same first digit.
# Etc, 0123, 0234, 0345 are MAJOR sets of 0
# There are n-m+1 MAJOR sets in total

# Observation
# Given f(n,m), it will appear that the first MAJOR set (first) contains
# n + n-1 + n-2 ... 1 elements

# The second MAJOR set contains a total of 
# n-1 + n-2 + ... 1 elements

# The last MAJOR set contains a total of 1 element only. 

from typing import List

# ChatGPT generated for b_search
def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    
    Parameters:
    - arr: A sorted list or array.
    - target: The target element to search for.
    
    Returns:
    - The index of the target element if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    if arr[right] < target:
        return right
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index
        
        # Check if the target is present at the middle
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # If the element is not present in the array
    return left

def sum_of_integers(n):
    _  = int (( n + 1 ) * n / 2)
    return _

def generate_smartly(n,m): # 5 , 2
    # First figure out X in 0___X
    # First digit can go from 0 to n-m, eg if (6,3), can go from 012 to 345. If (5,2), can go from 01 to 34
    starting_last_digit = n - m - 1
    ending_last_digit = n - 1
    number_of_digits = ending_last_digit - starting_last_digit + 1

    # Number of major sets
    number_of_major_sets = n - m + 1

    # Generate the starting index
    starting_idxs = []
    prev_idx = 0
    # This one below gets length, visualize as 2d matrix
    for i in range(number_of_major_sets):
        starting_idxs.append(prev_idx + sum_of_integers(number_of_digits))
        number_of_digits -= 1
        prev_idx = starting_idxs[-1]
    return starting_idxs

def get_closest_index(starting_idxs:List[int]):
    # Given the starting_idxes, print every 10th line
    # If we do a binary search for the particular number,
    # and bias the left, we will find the closest index
    # Problem with this is that now you might overlap
    target_line = 10
    res = [(0,0)]
    while True:
        idx = binary_search(starting_idxs, target_line) 
        starting_digit = starting_idxs.index(starting_idxs[idx])
        res.append((starting_digit, starting_idxs[idx]))
        target_line *= 10
        if starting_idxs[idx] == starting_idxs[-1]:
            break
    # Check if the last digit is out of range
    if idx != target_line:
        res.pop() # means it's out of range
    # Eg [(0, 0), (0, 10)] means starting from the first digit 0, return the number
    # Starting from 0, return the 10th increment of this number
    return res
 

def generate_full_number(first_digit, m, diff):
    # First, generates the initial number at the starting index.
    # Iterate through lexicgraphically for diff times
    # Generate start number
    starting_number = ""
    for i in range(m): # m = 3 |  0, 1
        starting_number += str(first_digit + i)
    if m == 0:
        return starting_number
    # Iterate through and return the number
    # Help me iterate from the start number liek this
    # Find the difference and increment it from starting number to that, then return
    return starting_number

def increment_number(starting_number, m, diff):
    # Base case
    if diff == 0 or len(starting_number) == 0:
        return starting_number, 0
    from_right_number, remaining_diff = increment_number(starting_number[1:], m, diff)
    if len(starting_number) == 0:
        return starting_number, diff
    if remaining_diff > 0:
        # Increment the first digit of this by 1, then recursively call again
        # Every number to the right must be + 1 of the prefix
        prefix = str(int(starting_number[0]) + 1)
        for i in range(len(starting_number)-1):
            prefix += str(int(starting_number[i+1]) + 1)
        print(f"New string here is {prefix}")
        return increment_number(prefix, m, remaining_diff - 1)
    # Check how many to increment in this place before having to increment the prev place
    difference_from_max = m - int(starting_number[-1])
  
    return starting_number, diff
    

def targetted_print(closest_index, m):
    res = []
    target_line = 1
    # Abusing the fact that Python dictionary returns in the same order you inserting
    for k,v in closest_index:
        # print(f"Starting index: {v}, Target line: {target_line}")
        if target_line == k:
            res.append(generate_full_number(k,m,0))
            print(f"First Digit {k}, index {v}, target line {target_line}, diff 0")
        else:
            # Find the difference
            diff = target_line - v
            res.append(generate_full_number(k,m,diff))
            print(f"First Digit {k}, index {v}, target line {target_line}, diff {diff}")
        target_line *= 10

    return res

def increment_number_v2(starting_number, m, diff):
        # Base case
    if diff == 0 or len(starting_number) == 0:
        return starting_number, 0

    # Calculate the difference from the maximum allowed digit
    difference_from_max = m - int(starting_number[-1])

    # If the difference is greater than the difference from max, then we need to carry over
    if diff > difference_from_max:
        # Carry over to the next digit
        print(starting_number)
        prefix = str(int(starting_number[:-1]) + 1)
        print(prefix)
        for i in range(len(starting_number)-1):
            prefix += str(int(starting_number[i+1]) + 1)
        print(prefix)
        return increment_number(prefix, m, diff - difference_from_max)

    # No carryover needed, increment the last digit by the difference
    new_last_digit = int(starting_number[-1]) + diff
    if new_last_digit >= m:
        # If the new last digit exceeds the maximum allowed, propagate the carry
        return increment_number(str(int(starting_number[:-1]) + 1) + str(new_last_digit - m), m, 1)

    # No carryover needed, construct the new number
    new_number = starting_number[:-1] + str(new_last_digit)
    return new_number, 0

def increment_v3(starting_number, m, diff):
    print(f"Starting number {starting_number}, m {m}, diff {diff}")
    if diff == 0 or len(starting_number) == 0:
        return starting_number, m, diff
    # Calculate if we need to roll over
    next_number, m, diff = increment_v3(starting_number[1:], m, diff)
    if diff > m - int(starting_number[-1]):
        remaining_diff = diff - (m - int(starting_number[-1]))
        return increment_v3(next_number, m, remaining_diff)
    # Calculate the proper increment
    if len(starting_number) == 1:
        print("GOt here!")
        _ = str(int(starting_number) + diff)
        print(_)
        return _, m, 0
    _ = next_number + str(int(starting_number[-1]) + diff)
    return _, m , 0
        # Roll over to the next digit

def AQQ2():
    # print(f"Starting A1Q2")
    # print("Generating for f(10,1)")
    # starting_idxs = generate_smartly(10,1)
    # closest_idx = get_closest_index(starting_idxs)
    # res = targetted_print(closest_idx, 1)
    # # print(res)
    # print()
    # I wantr the beklow
    # starting_idxs = generate_smartly(6,3)
    # closest_idx = get_closest_index(starting_idxs)
    # res = targetted_print(closest_idx, 3)
    # print(res)
    
    print(increment_v3("014", 6, 1))

if __name__ == "__main__":
    AQQ2()


#def p10_lines(n, m): # may include other args
#     # think about how to print the 1st, 10th, 100th, ... lines only
#     # you can use and modify from either recursion function above

# # num_line = int(sys.stdin.readline())
# # gn, gc = 0, [[1]]
# # for _ in range(num_line):
# #     a = [int(s) for s in sys.stdin.readline().split()]
# #     n, m = a[0], a[1]
# #     p10_lines(n, m)
