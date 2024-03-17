import math

class Heap:
    def __init__ (self, lst):
        self.__size = len(lst)
        self.__capacity = 2 ** math.ceil(math.log(self.__size + 1, 2))
        self.__content = [None] * self.__capacity
        self.__key_position = {}
        for i in range(self.__size):
            self.__content[i+1] = lst[i]
            self.__key_position[lst[i][1]] = i+1
    def __try_swap (self, i, j):
        if self.__content[j][0] < self.__content[i][0]:
            self.__content[i], self.__content[j] = self.__content[j], self.__content[i]
            self.__key_position[self.__content[i][1]], self.__key_position[self.__content[j][1]] = i, j
            return True
        else:
            return False
    def __heapify_at (self, i):
        if 2*i > self.__size:
            return
        if 2*i == self.__size or self.__content[2*i][0] <= self.__content[2*i+1][0]:
            if self.__try_swap(i, 2*i):
                self.__heapify_at(2*i)
        else:
            if self.__try_swap(i, 2*i+1):
                self.__heapify_at(2*i+1)
    def heapify (self):
        for i in range (self.__size // 2, 0, -1):
            self.__heapify_at(i)
    def update (self, k) -> bool:
        if k[1] in self.__key_position:
            i = self.__key_position[k[1]]
            if self.__content[i][0] > k[0]:
                self.__content[i][0] = k[0]
                while i > 1 and self.__try_swap(i // 2, i):
                    i = i // 2
            # ===== Changed Part =======
                return True
            else:
                # print(f"The existing edge is better! {self.__content[i][0]} > {k[0]}")
                return False
            # ===== Changed Part =======
        else:
            # print(f"Adding a new edge {k[0]}")
            if self.__size + 1 == self.__capacity:
                self.__content.extend([None] * self.__capacity)
                self.__capacity *= 2
            self.__size += 1
            i = self.__size
            self.__content[i] = k
            self.__key_position[k[1]] = i
            while i > 1 and self.__try_swap(i // 2, i):
                i = i // 2
            # ===== Changed Part =======
            return True
            # ===== Changed Part =======
    def pop (self):
        if self.__size == 0:
            return None
        else:
            k = self.__content[1]
            if self.__size > 1:
                del self.__key_position[self.__content[1][1]]
                self.__content[1], self.__content[self.__size] = self.__content[self.__size], None
                self.__key_position[self.__content[1][1]] = 1
                self.__size -= 1
                self.__heapify_at(1)
            else:
                self.__size = 0
            return k
    def len (self):
        return self.__size
    def print (self):
        print ('the content is', self.__content[1:self.__size+1])

wg_i= [(1, 2, 4), (2, 3, 9), (3, 4, 6), (4, 5, 3),
      (5, 3, 4), (5, 6, 2), (6, 2, 9), (6, 3, 2),
      (6, 7, 8), (7, 2, 7), (7, 5, 9), (7, 8, 8),
      (8, 4, 9), (8, 5, 9), (8, 9, 18), (9, 1, 4),
      (9, 7, 10), (9, 10, 3), (10, 1, 1), (10, 2, 5), (10, 7, 9)]

wg_p = [(1, 2, 0.4), (2, 3, 0.9), (3, 4, 0.6), (4, 5, 0.3),
      (5, 3, 0.4), (5, 6, 0.2), (6, 2, 0.9), (6, 3, 0.2),
      (6, 7, 0.8), (7, 2, 0.7), (7, 5, 0.9), (7, 8, 0.8),
      (8, 4, 0.9), (8, 5, 0.9), (8, 9, 0.18), (9, 1, 0.4),
      (9, 7, 0.10), (9, 10, 0.3), (10, 1, 0.1), (10, 2, 0.5), (10, 7, 0.9)]

wg_p_simple = [(1,2,0.9), (2,3,0.9), (3,4,0.9),
               (1,4,0.1), (4,5,0.1), (5,6,0.1),]

wg = wg_p_simple

# log transform
def transform_w(w: float) -> float:
    """
    Applies two set of transformation in the order below
    1. take 1 - w, this is to return a value of the probability of NOT being caught
    2. take natural log of the result from step 1, this is to convert it to log probabilities
    3. multiply by -1, this is to make the log probabilities positive
    This allows us to easily calculate the log probabilities of the path by summing the weights
    up. This particular transformation makes it so the smallest weight corrosponds to the lowest
    probability of being caught.
    """
    return -math.log(1 - w)

# Test the transformation
p_of_being_caught_1 = 0.5 # means 0.5 probability of not being caught
p_of_being_caught_2 = 0.1 # means 0.9 probability of not being caught
# I want the higher probabiltity of not being caught to have a smaller value so shortest path will work
assert transform_w(p_of_being_caught_1) > transform_w(p_of_being_caught_2), "The transformation is not working as expected"

# Unchanged
vertex = set()
for u, v, w in wg:
    vertex.add(u)
    vertex.add(v)
vertex = list(vertex)

# Creating the adj list
adjlist = {u:[] for u in vertex}
for u, v, w in wg:
    # Changed 
    adjlist[u].append((v, transform_w(w)))
    adjlist[v].append((u, transform_w(w)))
print('to vertex |', end='')
for u in vertex:
    print('%4d' % u, end='   ')
print()
print('-' * 51)
# Changed
"""
I need to modify this such that I store the previous vertex to this vertex.
Then I will have to write a helper funcion that will trace the path from the start to the end
"""
# Store in the form vertex: (previous_vertex, distance)
shortest_parent = {} 
for u in vertex:
    # Shortest path from each vertex
    heap = Heap([[0, u]])
    dist = {}
    while heap.len() > 0:
        mindist, v = heap.pop()
        dist[v] = mindist
        for i, w in adjlist[v]:
            if i not in dist:
                # ===== Changed Part =======
                if heap.update([mindist + w, i]):
                    # If true, this means we update the shortest path to this vertex
                    # else, we ignore
                    # print(f" We updated from {shortest_parent.get(i, (None, float('inf')))} to {(v, mindist + w)}")
                    shortest_parent[i] = (v, mindist + w)
                # ===== Changed Part =======
    # Break because we only need from the start, so only from one vertex
    break
    print('from %4d |' % u, end='')
    for v in vertex:
        print('%.2f' % dist[v], end=' | ')
        # print('%d' % dist[v], end='')
    print()

# ===== Changed Part =======
def trace_path(start, end, shortest_parent):
    """
    Traces the path from the start to the end using the shortest_parent dictionary
    """
    path = []
    current = end
    while current != start:
        print(f"Current is {current} and start is {start}")
        path.append(current)
        current = shortest_parent[current][0]
    path.append(start)
    return path[::-1]
# ===== Changed Part =======
print("Shortest path to goal:")
print(shortest_parent)
start = 1
end = 6
print(f"Shortest path from {start} to {end} is {trace_path(start, end, shortest_parent)}")


