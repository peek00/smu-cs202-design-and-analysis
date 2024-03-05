import sys
import pprint
from collections import defaultdict

def LCMS(a, b):
    # Let's try getting the most common subsequence first
    # Then we do mountaining from there.
    # commoners = get_common_elements_in_relative_order(a, b)
    # print("Commoners: ", len(commoners))
    # print(commoners)
    # answer = do_the_mountain_thing(commoners)
    # answer = do_the_mountain_thing_correctly_this_time(commoners)
    # return answer

    commoners = get_longest_common_subsequence(a, b)
    # print("Commoners: ", len(commoners))
    # print(commoners)
    answer = do_the_mountain_thing_third_time(commoners)
    # answer = do_the_mountain_thing_correctly_this_time(commoners)
    return answer

# def get_common_elements_in_relative_order(a, b):
#     # Create sets of both
#     a_set = set(a)
#     b_set = set(b)
#     for i in range(len(a)):
#         if a[i] not in b_set:
#             a[i] = None
#     for i in range(len(b)):
#         if b[i] not in a_set:
#             b[i] = None
#     return []

def do_the_mountain_thing_third_time(commoners):
    strictly_up = get_longest_increasing_sequence(commoners)
    strictly_down = get_longest_decreasing_sequence(commoners)
    # print(f"Commoners: {commoners}")
    # print(f"Strictly up: {strictly_up}")
    # print(f"Strictly down: {strictly_down}")
    max_sum = 0
    for num1, num2 in zip(strictly_up, strictly_down):
        max_sum = max(max_sum, num1 + num2)
  
    return max_sum + 1

def get_longest_decreasing_sequence(nums):
    if not nums:
        return []

    n = len(nums)
    dp = [0] * n

    for i in range(n - 2, -1, -1):  # Iterate from the second to the last element backward
        for j in range(i + 1, n):  # Iterate over elements to the right of nums[i]
            if nums[i] > nums[j]:  # Adjusted condition for Longest Decreasing Subsequence
                dp[i] = max(dp[i], dp[j] + 1)

    return dp 

def get_longest_increasing_sequence(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [0] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp

def get_longest_common_subsequence(a,b):
    if len(a) < len(b):
        a, b = b, a
    dp = [[0] * (len(a) + 1) for _ in range(len(b) + 1) ]
    
    # Construct common subsequence length
    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            if a[j - 1] == b[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Retrieve length of common subsequence from DP table
    # Go from bottom right to top left
    # 
    commoners = []
    # Both index of string and dp table
    p1 = len(a)
    p2 = len(b)
    while p1 > 0 and p2 > 0:
        # Checks if the string at index matches
        if a[p1 - 1] == b[p2 - 1]: 
            commoners.append(a[p1 - 1])
            p1 -= 1
            p2 -= 1
        # Checks in DP table if it is greater left or upwards
        # If there is an increase, it means there is a common character in both string
        elif dp[p2][p1 - 1] > dp[p2 - 1][p1]:
            p1 -= 1
        else:
            p2 -= 1

    return commoners[::-1]
    
# def get_longest_common_subsequence(a,b):
#     # Solve this using bottom up dynammic programming
#     # Created 2D matrix with +1 length for both A and B
#     # Start from top left, if it matches, move diagonal.

#     dp = [[0] * (len(a) + 1) for _ in range(len(b) + 1) ] 
#     prev_indices = [[None] * (len(a) + 1) for _ in range(len(b) + 1)]

#     for i in range(1, len(b) + 1):
#         dp[i % 2][0] = 0
#         for j in range(1, len(a) + 1):
#             if a[j - 1] == b[i - 1]:
#                 dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
#                 prev_indices[i][j] = (i - 1, j - 1)
#             else:
#                 if dp[(i - 1) % 2][j] > dp[i % 2][j - 1]:
#                     dp[i % 2][j] = dp[(i - 1) % 2][j]
#                     prev_indices[i][j] = (i - 1, j)
#                 else:
#                     dp[i % 2][j] = dp[i % 2][j - 1]
#                     prev_indices[i][j] = (i, j - 1)
#     # Retrieve path
#     commoners = []
#     i, j = len(b), len(a)
#     while i > 0 and j > 0:
#         if a[j - 1] == b[i - 1]:
#             commoners.append(a[j - 1])
#         i, j = prev_indices[i][j]
#     return commoners[::-1]

def do_the_mountain_thing_correctly_this_time(commoners):
    """
    Previous mountain thing did like a mountain thing but 
    but it was not the correct mountain thing.

    Lets do a dumb thing and brute force it.

    For each number, we will keep a count of the things 
    smaller than or larger than in a strictly decreasing manner.
    For every one, we must loop all the way back
    """
    strictly_up = [0] * len(commoners)
    for i in range(1, len(commoners)):
        # Goes from 1 to 53
        largest_from_before = -1
        for j in range(i):
            # Goes from 0 to i
            if commoners[j] < commoners[i]:
                # If this condition never triggers, the number will be 0
                largest_from_before = max(largest_from_before, strictly_up[j])
        if largest_from_before != -1:
            strictly_up[i] = largest_from_before + 1
        largest_from_before = -1

    strictly_down = [0] * len(commoners)
    for i in range(len(commoners)-2, -1, -1):
        largest_from_before = -1
        for j in range(len(commoners)-1, i, -1):
            if commoners[j] < commoners[i]:
                largest_from_before = max(largest_from_before, strictly_down[j])
        if largest_from_before != -1:
            strictly_down[i] = largest_from_before + 1
        largest_from_before = -1
    # print(strictly_up)
    # print(strictly_down)


    max_sum = 0
    maxy = []
    count = 0
    _ = 0
    for num1, num2 in zip(strictly_up, strictly_down):
        max_sum = max(max_sum, num1 + num2)
        maxy.append(num1 + num2)
        count += 1
        if max_sum == num1 + num2:
            _ = count
    # print("maxy", maxy.index(max_sum), commoners[_])
    print(max_sum + 1)

    return max_sum + 1


num_pair = int(sys.stdin.readline())

for _ in range(num_pair):
    # print("Case #", _+1, ": ", sep='', end='')
    a = [int(s) for s in sys.stdin.readline().split()]
    b = [int(s) for s in sys.stdin.readline().split()]
    print(LCMS(a, b))
    # print()

