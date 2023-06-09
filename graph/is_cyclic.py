def is_cyclic(graph: dict, start: str) -> bool:

	# stores vertex is visited or not
	visited = {start}

	# create a queue used to do BFS
	queue = []

	# push source vertex and its parent info into the queue
	queue.append((start, -1))

	# loop till queue is empty
	while queue:

		# pop front node from queue and print it
		(v, parent) = queue.pop(0)

		# do for every edge (v -> u)
		for u in graph[v]:
			if u not in visited:
				# mark it visited
				visited.add(u)

				# construct the queue node containing info
				# about vertex and push it into the queue
				queue.append((u, v))

			# u is visited and u is not a parent
			elif u != parent:
				# we found a cross-edge ie. cycle is found
				return True

	# No cross-edges found in the graph
	return False

if __name__ == "__main__":
    graph_adj_list = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }

    print(is_cyclic(graph_adj_list, "A"))