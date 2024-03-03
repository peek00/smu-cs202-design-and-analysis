import random

# random generate 10 denominations
# the next denomination ~= the previous * 2, or plus/minus 1
# for each denomination, generate a quantity between 10 and 20 inclusive

random.seed('coin')
curr = 1
denom = [(curr, random.randint(10, 20))]
for i in range(9):
    curr = 2 * curr + 1 - random.randrange(3)
    denom.append((curr, random.randint(10, 20)))
print(f"The denominations are in denom: quantity \n {denom}")

# solution to each subproblem, contain (1) the min number of coins, and (2) all plans with sum of coins being the min num of coins, this is because there is limited supply for each coin, one plan of x cents may allow us to reach x+5 cents, another plan may allow us to reach x+10 cents, depending on whether we have extra coins of 5 cents or 10 cents

class MinCoin:
    def __init__(self, n, p):
        self.num_coin = n
        self.plan = [p]
    def add_plan(self, p):
        self.plan.append(p)

m = len(denom)
n = 116
n = 12897
## This creates a list from 0 to 2000
min_coin_with_plan = [None] * (n + 1)
## This populates them with the MinCoin object, which is initalized with 0 number of coins
## and a plan of 0 coins for each denomination. The index of the min coin will refer to the sum.
min_coin_with_plan[0] = MinCoin(0, [0] * m)
## For all the coin denomination we have
for i in range(m): # suppose we already have solutions using denom[0], denom[1], ..., denom[i-1], now we consider using denom[i]
    ## Why is n hard coded to 2000? J appears to be the target that we want to find the minimum number of coins for
    for j in range(1, n+1): # consider the min coin problem with sum j cents
        ## Denom[i][0] refers to the value of the coin
        ## Following if statement is basically if J is greater than denom
        ## min_coin_with_plan[j - denom[i][0]] is not None, means the remainder of J-denom[i][0] is possible to be made up by the previous denominations
        if j >= denom[i][0] and min_coin_with_plan[j - denom[i][0]] is not None: # is it possible to use denom[i][0]? if yes, we can make up j cents by putting 1 coin of denom[i][0] and the min coin solution for j-denom[i][0]
            for p in min_coin_with_plan[j - denom[i][0]].plan: # for each possible plan of making j-denom[i][0]
                ## This checks that in that plan for j-current denom, we have extra coins of denom[i][0] to use.
                # print(f"P is {p}, p[i] is {p[i]} and denom[i][1] is {denom[i][1]}")

                if p[i] < denom[i][1]: # now I have a better solution, build a new obj as a solution for j
                    ## First if means that that there is no solution yet for current plan
                    ## or verify that if we do j - denom and add in one of the current denom, the number of coins is less than the current solution
                    if min_coin_with_plan[j] is None or min_coin_with_plan[j - denom[i][0]].num_coin + 1 < min_coin_with_plan[j].num_coin: # must check if there is enough supply of denom[i][0]
                        p_new = p.copy()
                        p_new[i] += 1 # add one coin of denom[i][0]
                        ## Initalize a new object of 
                        min_coin_with_plan[j] = MinCoin(min_coin_with_plan[j - denom[i][0]].num_coin + 1, p_new)
                    elif min_coin_with_plan[j - denom[i][0]].num_coin + 1 == min_coin_with_plan[j].num_coin: # now I have an equally good solution, only need to add the plan
                        p_new = p.copy()
                        p_new[i] += 1 # add one coin of denom[i][0]
                        min_coin_with_plan[j].add_plan(p_new)
                    # If the number of coins used here is greater, it will not save
            # try:
            #     print(f"The plan becomes {min_coin_with_plan[j].num_coin, min_coin_with_plan[j].plan}")
            # except:
            #     pass

'''T
# may print out and check
for i in range(1, n+1):
    if min_coin_with_plan[i] is not None:
        print(i, min_coin_with_plan[i].num_coin, min_coin_with_plan[i].plan)
# '''
# for i in range(1, n+1):
# # for i in range(1, n+1):
#     if min_coin_with_plan[i] is not None:
#         print()
#         print("============ Start ============")
#         print(f"The denominations are in denom: quantity \n {denom}")
#         print(f"Target is {i}")
#         print(min_coin_with_plan[i].num_coin)
#         print(min_coin_with_plan[i].plan)
#         print("============ End ============")
# print()
print("============ Start ============")
# print(f"The denominations are in denom: quantity \n {denom}")
print(f"Target is {n}")
print(len(min_coin_with_plan))
for i,mc in enumerate(min_coin_with_plan):
    if mc is not None:
        pass
    if mc is None:
        print(i)
        break
print(min_coin_with_plan[i-1].num_coin)
print(min_coin_with_plan[i-1].plan)
print("============ End ============")


# # # if we only consider the minimum number of coins without considering the plans

# min_coin_num_only = [[float('inf')] * (n+1) for _ in range(m+1)]
# for i in range(m+1): 
#     min_coin_num_only[i][0] = 0
# for i in range(m): # For all the types of denom
#     for j in range(1, n+1): # From 1 to the target 2k
#         min_coin_num_only[i+1][j] = min_coin_num_only[i][j] # if do not use denom[i][0] cents
#         for k in range(1, denom[i][1]+1): # using k pieces of denom[i][0] cents
#             if j >= k * denom[i][0]:
#                 min_coin_num_only[i+1][j] = min(min_coin_num_only[i+1][j], min_coin_num_only[i][j - k*denom[i][0]] + k)


# print()
# print("============ Start ============")
# print(f"The denominations are in denom: quantity \n {denom}")
# print(f"Target is {n}")
# print(len(min_coin_num_only))
# print(min_coin_num_only[m][n])
# # # Can array min_coin_num_only be changed to a 1-dimensional array?

# # all_same = True
# # for i in range(1, n+1):
# #     if min_coin_with_plan[i].num_coin != min_coin_num_only[m][i]:
# #         print('inconsistent result:', min_coin_with_plan[i].num_coin, min_coin_num_only[m][i])
# #         all_same = False
# # if all_same:
# #     print('all the same')

# # Now we try another example

# random.seed('coin')
# curr = 1
# denom = [(curr, random.randint(2, 3))]
# for i in range(5):
#     curr = 2 * curr + 1 - random.randrange(3)
#     denom.append((curr, random.randint(2, 3)))
# # print('another set of denomations:', denom)
# # should be [(1, 2), (2, 2), (3, 2), (7, 3), (14, 3), (29, 2)]

# n = 100
