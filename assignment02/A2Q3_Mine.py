import random, time

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


class MinCoin:
    def __init__(self, n, p):
        self.num_coin = n
        self.plan = [p]
    def add_plan(self, p):
        self.plan.append(p)

m = len(denom)
n = 12897
n = 6006
# n = 88

start_time = time.time()


min_coin_with_plan = [None] * (n + 1)
min_coin_with_plan[0] = MinCoin(0, [0] * m)

for i in range(m): # suppose we already have solutions using denom[0], denom[1], ..., denom[i-1], now we consider using denom[i]
    for j in range(1, n+1): # consider the min coin problem with sum j cents
        if j == 6006:
            print(f"Checking for target {j} and denom {i} which is {denom[i][0]}")
            print(f"Condition 1 {j >= denom[i][0]} and {min_coin_with_plan[j - denom[i][0]] is not None}")
            try:
                print(f" we are checking if {j - denom[i][0]} is not None, and it is indeed {min_coin_with_plan[j - denom[i][0]].plan}")
            except:
                pass
        if j >= denom[i][0] and min_coin_with_plan[j - denom[i][0]] is not None: # is it possible to use denom[i][0]? if yes, we can make up j cents by putting 1 coin of denom[i][0] and the min coin solution for j-denom[i][0]
            for p in min_coin_with_plan[j - denom[i][0]].plan: # for each possible plan of making j-denom[i][0]
                if p[i] < denom[i][1]: # now I have a better solution, build a new obj as a solution for j
                    if min_coin_with_plan[j] is None or min_coin_with_plan[j - denom[i][0]].num_coin + 1 < min_coin_with_plan[j].num_coin: # must check if there is enough supply of denom[i][0]
                        p_new = p.copy()
                        p_new[i] += 1 # add one coin of denom[i][0]
                        min_coin_with_plan[j] = MinCoin(min_coin_with_plan[j - denom[i][0]].num_coin + 1, p_new)
                    elif min_coin_with_plan[j - denom[i][0]].num_coin + 1 == min_coin_with_plan[j].num_coin: # now I have an equally good solution, only need to add the plan
                        p_new = p.copy()
                        p_new[i] += 1 # add one coin of denom[i][0]
                        min_coin_with_plan[j].add_plan(p_new)
                else:
                    # Since we used up all our denoms, why not I take J - the sum of all of the curret denom and find it?

                    # If I get here, what it means is that the current sum j is greater than my denom considered
                    # If I take j - the current denom, i have a solution for the remainder
                    # But I do not have any more coins of the current denom to use
                    # So what should I do? 
                    p_new = min_coin_with_plan[j - p[i] * denom[i][0]].plan[0].copy()
                    p_new[i] += p[i]
                    if min_coin_with_plan[j] is None or min_coin_with_plan[j - p[i] * denom[i][0]].num_coin + p[i] < min_coin_with_plan[j].num_coin:
                        min_coin_with_plan[j] = MinCoin(min_coin_with_plan[j - p[i] * denom[i][0]].num_coin + p[i], p_new)
                    elif min_coin_with_plan[j - p[i] * denom[i][0]].num_coin + p[i] == min_coin_with_plan[j].num_coin:
                        min_coin_with_plan[j].add_plan(p_new)

                    print(f"We got here! We are looking at denom {denom[i][0]} for target {j} and p is {p} and p[i] is {p[i]} and denom[i][1] is {denom[i][1]}")
                    print(f"So if we minus {p[i] * denom[i][0]} from {j} we get  {j - p[i] * denom[i][0]}, and the plan for that is {min_coin_with_plan[j - p[i] * denom[i][0]].plan}")
                    pass
                # If I do not have a solution using the current denomination, i should take 
                # j - all the various denoms in front 
                # else:
                #     print("We are here")
                #     for i2 in range(m):
                #         if i2 == i:
                #             continue
                #         # 6006 - 1 = 6005 
                #         if min_coin_with_plan[j - denom[i2][0]] is not None:
                #             for p in min_coin_with_plan[j - denom[i2][0]].plan:
                #                 if p[i2] < denom[i2][1]:
                #                     if min_coin_with_plan[j] is None or min_coin_with_plan[j - denom[i2][0]].num_coin + 1 < min_coin_with_plan[j].num_coin:
                #                         p_new = p.copy()
                #                         p_new[i2] += 1
                #                         min_coin_with_plan[j] = MinCoin(min_coin_with_plan[j - denom[i2][0]].num_coin + 1, p_new)
                #                     elif min_coin_with_plan[j - denom[i2][0]].num_coin + 1 == min_coin_with_plan[j].num_coin:
                #                         p_new = p.copy()
                #                         p_new[i2] += 1
                #                         min_coin_with_plan[j].add_plan(p_new)


# print(min_coin_with_plan[88].num_coin, min_coin_with_plan[88].plan)
print(min_coin_with_plan[6006].num_coin, min_coin_with_plan[6006].plan)





print("--- %s seconds ---" % (time.time() - start_time))

