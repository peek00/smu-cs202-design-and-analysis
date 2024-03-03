import sys
import pprint

def LCMS(a, b):
    # Let's try getting the most common subsequence first
    # Then we do mountaining from there.
    commoners = get_longest_common_subsequence(a, b)
    print("Commoners: ", len(commoners), commoners)
    # answer = do_the_mountain_thing(commoners)
    answer = do_the_mountain_thing_correctly_this_time(commoners)
    return answer
    

def get_longest_common_subsequence(a,b):
    # Solve this using bottom up dynammic programming
    # Created 2D matrix with +1 length for both A and B
    # Start from top left, if it matches, move diagonal.
    # Else, move either right or down. 
    # commoners = []
    # dp = [[0] * (len(a) + 1) for _ in range(len(b) + 1) ] # b + 1* a + 1
    # # Initially the last row and colum to be 0
    # # Setting last row
    # dp[len(b)] = [0] * (len(a) + 1)
    # # Setting last column
    # for i in range(len(b) + 1):
    #     dp[i][-1] = 0
    # # 1 + value of diagonal if match, else max of left and top
    # for i in range(len(b)-1, -1, -1):
    #     for j in range(len(a)-1, -1, -1):
    #         if a[j] == b[i]:
    #             commoners.append(a[j])
    #             dp[i][j] = 1 + dp[i+1][j+1]
    #         else:
    #             dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    # return commoners
    dp = [[0] * (len(a) + 1) for _ in range(len(b) + 1) ] 
    prev_indices = [[None] * (len(a) + 1) for _ in range(len(b) + 1)]

    for i in range(1, len(b) + 1):
        dp[i % 2][0] = 0
        for j in range(1, len(a) + 1):
            if a[j - 1] == b[i - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                prev_indices[i][j] = (i - 1, j - 1)
            else:
                if dp[(i - 1) % 2][j] > dp[i % 2][j - 1]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j]
                    prev_indices[i][j] = (i - 1, j)
                else:
                    dp[i % 2][j] = dp[i % 2][j - 1]
                    prev_indices[i][j] = (i, j - 1)
    # Retrieve path
    commoners = []
    i, j = len(b), len(a)
    while i > 0 and j > 0:
        if a[j - 1] == b[i - 1]:
            commoners.append(a[j - 1])
        i, j = prev_indices[i][j]
    return commoners[::-1]

def do_the_mountain_thing(commoners):
    """
    Return all possible mountains given a list of commmon subsequence.
    Create an up and a down list.
    At a particular index, the number should mean how many elements
    before this index are smaller than this index.
    For the down list, it should mean how many index are smaller.
    Iterate through the commoners list.
    At each step, check if it is bigger than the previous element.
    If it is, increment i-1 for up list and down list.
    """
    up = [0] * len(commoners)
    down = [0] * len(commoners)

    prev = commoners[0]
    for i in range(1, len(commoners)):
        if commoners[i] > prev:
            up[i] = up[i-1] + 1
        else:
            up[i] = 0
        prev = commoners[i]
    for i in range(len(commoners)-2, -1, -1):
        if commoners[i] > commoners[i+1]:
            down[i] = down[i+1] + 1
        else:
            down[i] = 0

    max_sum = 0
    # Sum up both rows and return the max

    for num1, num2 in zip(up, down):
        max_sum = max(max_sum, num1 + num2)
    return max_sum + 1

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
        for j in range(i):
            if commoners[j] < commoners[i]:
                strictly_up[i] = max(strictly_up[i], strictly_up[j] + 1)
    strictly_down = [0] * len(commoners)
    for i in range(len(commoners)-2, -1, -1):
        for j in range(len(commoners)-1, i, -1):
            if commoners[j] < commoners[i]:
                strictly_down[i] = max(strictly_down[i], strictly_down[j] + 1)
    print(strictly_up)
    print(strictly_down)
    max_sum = 0
    peak = 0
    for num1, num2 in zip(strictly_up, strictly_down):
        max_sum = max(max_sum, num1 + num2)
        if max_sum == num1 + num2:
            peak = strictly_up.index(num1)
    print("Peak index is ", peak)
    return max_sum + 1


num_pair = int(sys.stdin.readline())
for _ in range(num_pair):
    print("Case #", _+1, ": ", sep='', end='')
    a = [int(s) for s in sys.stdin.readline().split()]
    b = [int(s) for s in sys.stdin.readline().split()]
    print(LCMS(a, b))
    print()
