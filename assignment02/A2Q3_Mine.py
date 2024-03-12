
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


# class MinCoin:
#     def __init__(self, n, p):
#         self.num_coin = n
#         self.plan = [p]
#     def add_plan(self, p):
#         self.plan.append(p)

# ========================= PROPOSED CHANGES ===============================
"""
I created a new data structure to maintain all possible ways combination you can 
get to a certain number of coins. This data structure is a min heap, where the key is
the total sum of the coins in the list aka the plan. 

The main motivator of this was I noticed that whenever the previous solution and 
MinCoin encountered a solution for a particular solution that uses a smaller number of coins,
it would delete and remove the older, larger solution. This made it problematic to "retrieve"
less optimal solutions where the number of coins had been exhausted. 

My initial solution was to create a min heap and store all possible combinations of coins 
that makes up the sum, such that when it was looped over the ones with the min coins used
would appear first. There will be some issues faced with larger inputs this way however.

Instead of having a pop method, I tried to implement an iterate method that will 
properly iterate through the min heap based on an array via indexing, but was unable to 
do that properly. The current implementation will only return the smallest element correct,
aka the one at 0 index but iterates through the index in strictly increasing order instead of 
"jumping" from indexes to simulate if we were to pop the min heap.

This part had the influence of ChatGPT (Prompts provided separately).
"""
class MinSumListHeap:
    def __init__(self):
        self.plan = []
        self.history = set()

    def add_list(self, new_plan):
        if str(new_plan) in self.history:
            print("We saved some space")
            return
        self.history.add(str(new_plan))
        self.plan.append(new_plan)
        self._heapify_up(len(self.plan) - 1)

    def _heapify_up(self,index):
        while index > 0:
            parent = (index - 1) // 2
            if self._get_sum(self.plan[index]) < self._get_sum(self.plan[parent]):
                self.plan[index], self.plan[parent] = self.plan[parent], self.plan[index]
                index = parent
            else:
                break
    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if (left_child_index < len(self.plan) and
                    self._get_sum(self.plan[left_child_index]) < self._get_sum(self.plan[smallest])):
                smallest = left_child_index

            if (right_child_index < len(self.plan) and
                    self._get_sum(self.plan[right_child_index]) < self._get_sum(self.plan[smallest])):
                smallest = right_child_index

            if smallest != index:
                self.plan[index], self.plan[smallest] = self.plan[smallest], self.plan[index]
                index = smallest
            else:
                break
    def _get_sum(self, lst):
        return sum(lst)
    
    def __iter__(self):
        return iter(self.data)
    
# print("========Testing minSumListHeap========")
# minSumListHeap = MinSumListHeap()
# minSumListHeap.add_list([1,0,0])
# minSumListHeap.add_list([0,0,2])
# minSumListHeap.add_list([0,0,3])    
# minSumListHeap.add_list([0,4,3])    
# minSumListHeap.add_list([0,2,0])
# minSumListHeap.add_list([2,0,0])
# minSumListHeap.add_list([5,0,0])

# for plan in minSumListHeap.plan:
#     print(plan)

# maybe we start by modifying minCoin
# I need it to not just store the smallest number of coins, but use a deque based on the number of coins to be stored

# ========================= PROPOSED CHANGES ===============================
n = 6006
n = 12897 # This is the biggest possible number, the total sum of all coins
"""
Uncomment the following to use the smaller test case.
"""
# denom = [(1,2), (2,1)]
# n = 4


m = len(denom)
min_coin_with_plan = [None] * (n + 1)
min_coin_with_plan[0] = MinSumListHeap()
min_coin_with_plan[0].add_list([0] * m)

# ========================= PROPOSED CHANGES ===============================
"""
Beyond initiating the above data structure, I did not change much of the original code.
I understood that the main problem in the original code was how it handled the 
situation where the the solution exceeded the current number of coins available for that denomination.
This caused incidents where like it would not be able to resolve for 6006, while it had a solution for 6005.

I initially believed that by replacing the MinCoin data structure to the one above, 
the algorithm below will loop through all the plans and will be able to find one where the
coins used would be a valid combination.

However, the main problem with my proposed change and implementation was the space complexity. 
It would quickly come up with a LOT of plans, while they were all feasible it made it impossible
for my computer to get a solution for the proposed denomination and n = 6006.

It does work correctly for smaller amounts. An example the original algorithm failed is for
denoms [(1,2), (2,1)] and n = 4. The original algorithm would not return a solution for 4, 
but the solution I implemented will. 
"""

start = time.time()
for i in range(m):
    # print(f"Checking for denom {i} which is {denom[i][0]}")
    for j in range(1, n+1):
        # print("Checking for target", j, "and denom", i, "which is", denom[i][0])
        if j >= denom[i][0] and min_coin_with_plan[j - denom[i][0]] is not None: 
            # print(f"There are {len(min_coin_with_plan[j - denom[i][0]].plan)} plans for {j - denom[i][0]}")
            for p in min_coin_with_plan[j - denom[i][0]].plan: 
                if p[i] < denom[i][1]: 
                    if min_coin_with_plan[j] is None: 
                        min_coin_with_plan[j] = MinSumListHeap()
                    p_new = p.copy()
                    p_new[i] += 1 
                    min_coin_with_plan[j].add_list(p_new)
          
print(min_coin_with_plan[n].plan)

print("--- %s seconds ---" % (time.time() - start))

# MAYBE EACH TIME WE REPLACE, WE ADD THE SUM OF THE NUMBER TOO