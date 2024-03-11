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


class MinSumListHeap:
    def __init__(self):
        self.plan = []

    def add_list(self, new_plan):
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

denom = [(1,2), (2,1)]
n = 4

m = len(denom)
# n = 12897
n = 6006

# min_coin_with_plan = [None] * (n + 1)
# min_coin_with_plan[0] = MinCoin(0, [0] * m)
min_coin_with_plan = [None] * (n + 1)
min_coin_with_plan[0] = MinSumListHeap()
min_coin_with_plan[0].add_list([0] * m)

for i in range(m):
    print(f"Checking for denom {i} which is {denom[i][0]}")
    for j in range(1, n+1):
        print("Checking for target", j, "and denom", i, "which is", denom[i][0])
        if j >= denom[i][0] and min_coin_with_plan[j - denom[i][0]] is not None: 
            for p in min_coin_with_plan[j - denom[i][0]].plan: 
                if p[i] < denom[i][1]: 
                    if min_coin_with_plan[j] is None: 
                        p_new = p.copy()
                        p_new[i] += 1 
                        min_coin_with_plan[j] = MinSumListHeap()
                        min_coin_with_plan[j].add_list(p_new)
                    else: 
                        p_new = p.copy()
                        p_new[i] += 1 
                        min_coin_with_plan[j].add_list(p_new)
                else:
                    # Dont loop anymore
                    break 
       
# for _ in min_coin_with_plan:
#     print(_.plan, _.num_coin)
print(min_coin_with_plan[4].plan)
print(min_coin_with_plan[6006].plan)





# print("--- %s seconds ---" % (time.time() - start_time))

