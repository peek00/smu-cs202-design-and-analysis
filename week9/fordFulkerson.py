# Python program for implementation
# of Ford Fulkerson algorithm
from collections import defaultdict

# This class represents a directed graph
# using adjacency matrix representation
class Graph:
	def __init__(self, graph):
		self.graph = graph # residual graph
		self.ROW = len(graph)

	def BFS(self, s, t, parent):
		# Mark all the vertices as not visited
		visited = [False]*(self.ROW)

		# Create a queue for BFS
		queue = []

		# Mark the source node as visited and enqueue it
		queue.append(s)
		visited[s] = True

		# Standard BFS Loop
		while queue:
			u = queue.pop(0)
			for ind, val in enumerate(self.graph[u]):
				if visited[ind] == False and val > 0:
					queue.append(ind)
					visited[ind] = True
					parent[ind] = u
					if ind == t:
						return True

		return False
				
	# Returns the maximum flow from s to t in the given graph
	def FordFulkerson(self, source, sink):
		# This array is filled by BFS and to store path
		parent = [-1]*(self.ROW)
		max_flow = 0 # There is no flow initially

		# Augment the flow while there is path from source to sink
		while self.BFS(source, sink, parent) :
			## XY: This looks for an augmenting path, if there exists you push one across.
			# Find minimum residual capacity of the edges along the
			# path filled by BFS. Or we can say find the maximum flow
			# through the path found.
			path_flow = float("Inf")
			s = sink
			while(s != source):
				path_flow = min (path_flow, self.graph[parent[s]][s])
				s = parent[s]

			# Add path flow to overall flow
			max_flow += path_flow

			# update residual capacities of the edges and reverse edges
			# along the path
			v = sink
			while(v != source):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v = parent[v]

		return max_flow

# Create a graph given in the above diagram

graph = [[0, 16, 13, 0, 0, 0],
		[0, 0, 10, 12, 0, 0],
		[0, 4, 0, 0, 14, 0],
		[0, 0, 9, 0, 0, 20],
		[0, 0, 0, 7, 0, 4],
		[0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0; sink = 5

print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))

#the following is the textbook example
graph2 = [[0, 16, 13, 0, 0, 0],
		[0, 0, 0, 12, 0, 0],
		[0, 4, 0, 0, 14, 0],
		[0, 0, 9, 0, 0, 20],
		[0, 0, 0, 7, 0, 4],
		[0, 0, 0, 0, 0, 0]]

g2 = Graph(graph2)

source2 = 0; sink2 = 5

print ("The maximum possible flow is %d " % g2.FordFulkerson(source2, sink2))

# This code is contributed by Neelam Yadav
