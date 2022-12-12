from collections import defaultdict
from numpy import array as np_array
from utils import parse_input


class Graph:
    def __init__(self, grid):
        self.edges = defaultdict(list)
        self.weights = {}
        self.grid = np_array([[ord(val) for val in line] for line in grid])
        self.shape = np_array(self.grid.shape)
        self._parse_grid()

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight

    def _parse_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                pos = np_array((i,j))
                val = self.grid[tuple(pos)]
                if val == 83: # ord('S')
                    val = 97 # ord('a')
                # check all movement operations
                for vec in [np_array((-1, 0)), np_array((1, 0)), np_array((0, -1)), np_array((0, 1))]:
                    new_pos = pos + vec
                    # if not moving outside grid
                    if all(new_pos >= 0) and all(new_pos < self.shape):
                        new_val = self.grid[tuple(new_pos)]
                        # fix end point
                        if new_val == 69: # ord('E')
                            new_val = 123 # ord('z')+1
                        # add edge if move possible
                        if (new_val - val) <= 1:
                            self.add_edge(tuple(pos), tuple(new_pos), 1)

    def find(self, val):
        if isinstance(val, str):
            val = ord(val)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i,j] == val:
                    return (i, j)

    def shortest_path(self, start, end):
        # shortest paths start with initial node
        # it has no previous nodes and distance 0
        # keep track of previous nodes to update distance
        shortest_paths = {start: (None, 0)}
        curr_node = start
        visited = set()

        # loop until find end
        while curr_node != end:
            visited.add(curr_node)
            neighbours = self.edges[curr_node]

            for node in neighbours:
                # find the distance from start to next node
                node_dist = shortest_paths[curr_node][1] + self.weights[(curr_node, node)]
                # if not in shortest then by default this
                # is the new shortest
                if node not in shortest_paths:
                    shortest_paths[node] = (curr_node, node_dist)
                # otherwise only update if the new distance is shorter
                elif shortest_paths[node][1] > node_dist:
                    shortest_paths[node] = (curr_node, node_dist)
            #print(curr_node, next_nodes)

            next_nodes = {node: shortest_paths[node][1] for node in shortest_paths if node not in visited}
            if len(next_nodes) == 0:
                # no more moves and haven't found end
                return None
            else:
                curr_node = min(next_nodes, key=next_nodes.get)

        # return the distance to end
        return shortest_paths[end][1]


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    graph = Graph(contents)
    start = graph.find('S')
    end = graph.find('E')
    part_1 = graph.shortest_path(start, end)
    print(f'Part 1: {part_1}')

    part_2 = []
    for i in range(graph.shape[0]):
        for j in range(graph.shape[1]):
            if graph.grid[i,j] == ord('a'):
                path = graph.shortest_path((i, j), end)
                if path is not None:
                    part_2.append(path)
    part_2.sort()
    print(f'Part 2: {part_2[0]}')


if __name__ == '__main__':
    __main__()
