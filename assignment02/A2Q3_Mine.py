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


class MinSumListHeap:
    def __init__(self):
        self.heap = []

    def add_list(self, new_plan):
        self.heap.append(new_plan)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self,index):
        while index > 0:
            parent = (index - 1) // 2
            if self._get_sum(self.heap[index]) < self._get_sum(self.heap[parent]):
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if (left_child_index < len(self.heap) and
                    self._get_sum(self.heap[left_child_index]) < self._get_sum(self.heap[smallest])):
                smallest = left_child_index

            if (right_child_index < len(self.heap) and
                    self._get_sum(self.heap[right_child_index]) < self._get_sum(self.heap[smallest])):
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
    def _get_sum(self, lst):
        return sum(lst)
    
    def __iter__(self):
        return iter(self.data)
    
print("========Testing minSumListHeap========")
minSumListHeap = MinSumListHeap()
minSumListHeap.add_list([1,0,0])
minSumListHeap.add_list([0,0,2])
minSumListHeap.add_list([0,0,3])    
minSumListHeap.add_list([0,4,3])    
minSumListHeap.add_list([0,2,0])
minSumListHeap.add_list([2,0,0])
minSumListHeap.add_list([5,0,0])

for plan in minSumListHeap.heap:
    print(plan)

# maybe we start by modifying minCoin
# I need it to not just store the smallest number of coins, but use a deque based on the number of coins to be stored

# denom = [(1,2), (2,1)]
# n = 4

# m = len(denom)
# n = 12897
# n = 6006
# n = 88

# start_time = time.time()


# min_coin_with_plan = [None] * (n + 1)
# min_coin_with_plan[0] = MinCoin(0, [0] * m)

# for i in range(m):
#     for j in range(1, n+1):
#         # This if statement builds up the possibility where we can use the current denomination
#         # + some other previously completed sum to hit the target j 
#         # j = 4m >=2, 4-2 = 2
#         # When it goes through the plan 
#         if j >= denom[i][0] and min_coin_with_plan[j - denom[i][0]] is not None: 
#             for p in min_coin_with_plan[j - denom[i][0]].plan: 
#                 if p[i] < denom[i][1]: 
#                     if min_coin_with_plan[j] is None or min_coin_with_plan[j - denom[i][0]].num_coin + 1 < min_coin_with_plan[j].num_coin: 
#                         p_new = p.copy()
#                         p_new[i] += 1 
#                         min_coin_with_plan[j] = MinCoin(min_coin_with_plan[j - denom[i][0]].num_coin + 1, p_new)
#                     elif min_coin_with_plan[j - denom[i][0]].num_coin + 1 == min_coin_with_plan[j].num_coin: 
#                         p_new = p.copy()
#                         p_new[i] += 1 
#                         min_coin_with_plan[j].add_plan(p_new)
#                 else:
#                     print(f"Checking for {j}, we minus {denom[i][0]} * {p[i]} and get {j - denom[i][0] * p[i]} and the plan for that is {min_coin_with_plan[j - denom[i][0] * p[i]].plan}" )
#                     print(f"J is {j}, j - denom[i][0] * p[i] is {j - denom[i][0] * p[i]}")
#                     pass
#         else:
#             print(f"We are checking for {j} and denom {i} which is {denom[i][0]}")
#             pass
       
# for _ in min_coin_with_plan:
#     print(_.plan, _.num_coin)
# # print(min_coin_with_plan[4].num_coin, min_coin_with_plan[88].plan)
# # print(min_coin_with_plan[6006].num_coin, min_coin_with_plan[6006].plan)





# print("--- %s seconds ---" % (time.time() - start_time))

