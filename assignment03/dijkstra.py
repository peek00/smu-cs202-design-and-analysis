import math

class Heap:
    def __init__ (self, lst):
        self.__size = len(lst)
        self.__capacity = 2 ** math.ceil(math.log(self.__size + 1, 2))
        self.__content = [None] * self.__capacity
        # Added in
        self.__key_pos = {} #Helps track node ID (key) to its position 
        for i in range(self.__size):
            self.__content[i+1] = lst[i]
            self.__key_pos[lst[i][1]] = i+1

    def __try_swap (self, i, j):
        # Need to update
        if self.__content[j][0] < self.__content[i][0]:
            self.__content[i], self.__content[j] = self.__content[j], self.__content[i]
            # Double check
            self.__key_pos[self.__content[i][1]], self.__key_pos[self.__content[j][1]] = i, j
            return True
        else:
            return False

    def __heapify_at (self, i):
        if 2*i > self.__size: 
            return
        if 2*i == self.__size or self.__content[2*i][0] <= self.__content[2*i+1][0]: 
        # If either last node with single child or left child smaller than right
            if self.__try_swap(i, 2*i): # Swap with left child
                self.__heapify_at(2*i)
        else:
            if self.__try_swap(i, 2*i+1): #Swap with right child
                self.__heapify_at(2*i+1)

    def heapify (self):
        for i in range (self.__size // 2, 0, -1): # Start at last internal node. 
            self.__heapify_at(i)

    def update(self, k):
        # k is a list of 2 elements
        # k[0] is the value you wish to update to
        # k[1] is the key of the node
        # if there is no such id, insert a node with value k[0] and key k[1]
        if k[1] in self.__key_pos:
            i = self.__key_pos[k[1]]  # Take back original position
            if self.__content[i][0] > k[0]:  # For edge relaxation
                # First update value to k0 then heapify up
                self.__content[i][0] = k[0]
                while i > 1 and self.__try_swap(i // 2, i):
                    i = i // 2
        else:  # k[1] not in key_pos, meaning this is a new node
            # Extend this list if necessary
            if self.__size + 1 == self.__capacity:
                self.__content.extend([None] * self.__capacity)
                self.__capacity *= 2
            self.__size += 1
            i = self.__size
            self.__content[i] = k
            self.__key_pos[k[1]] = i
            while i > 1 and self.__try_swap(i // 2, i):
                i = i // 2

    def pop (self):
        if self.__size == 0:
            return None
        else:
            k = self.__content[1]
            if self.__size > 1:
                del self.__key_pos[self.__content[i][1]]
                self.__content[1], self.__content[self.__size] = self.__content[self.__size], None
                self.__key_pos[self.__content[1][1]] = 1
                self.__size -= 1
                self.__heapify_at(1)
            else:
                self.__size = 0
            return k

    def len (self):
        return self.__size

    def print (self):
        print ('the content is', self.__content[1:self.__size+1])

wg = [(1, 2, 4), (2, 3, 9), (3, 4, 6), (4, 5, 3),
      (5, 3, 4), (5, 6, 2), (6, 2, 9), (6, 3, 2),
      (6, 7, 8), (7, 2, 7), (7, 5, 9), (7, 8, 8),
      (8, 4, 9), (8, 5, 9), (8, 9, 18), (9, 1, 4),
      (9, 7, 10), (9, 10, 3), (10, 1, 1), (10, 2, 5), (10, 7, 9)]

vertex = set()
for u, v, w in wg:
    vertex.add(u)
    vertex.add(v)
vertex = list(vertex)

adjlist = {u:[] for u in vertex}
for u, v, w in wg:
    adjlist[u].append((v, w))
    adjlist[v].append((u, w))
print('to vertex |', end='')
for u in vertex:
    print('%4d' % u, end='')
print()
print('-' * 51)
for u in vertex:
    heap = Heap([[0, u]])
    dist = {}
    while heap.len() > 0:
        mindist, v = heap.pop()
        dist[v] = mindist
        for i, w in adjlist[v]:
            if i not in dist:
                heap.update([mindist + w, i])
    print('from %4d |' % u, end='')
    for v in vertex:
        print('%4d' % dist[v], end='')
    print()
