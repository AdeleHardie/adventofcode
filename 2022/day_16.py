from collections import defaultdict
from utils import parse_input
import heapq


class Graph:
    def __init__(self, contents):
        self.edges = defaultdict(list)
        self.distances = {}
        self.nodes = {}
        self._parse_input(contents)
        self._compute_paths()
        self._memo = {}
        self.best_score = 0

    def _parse_input(self, contents):
        for line in contents:
            parts = line.split()
            node = parts[1]
            flow = int(parts[4].split('=')[1][:-1])
            if flow > 0:
                self.nodes[node] = flow
                self.edges[node].append(f'{node}_flow')
            for valve in parts[9:]:
                self.edges[node].append(valve.replace(',', ''))
                if flow > 0:
                    self.edges[f'{node}_flow'].append(valve.replace(',', ''))

    def shortest_path(self, start, end):
        shortest_paths = {start: (None, 0)}
        curr_node = start
        visited = set()

        # loop until find end
        while curr_node != end:
            visited.add(curr_node)
            neighbours = self.edges[curr_node]

            for node in neighbours:
                node_dist = shortest_paths[curr_node][1] + 1
                if node not in shortest_paths:
                    shortest_paths[node] = (curr_node, node_dist)
                elif shortest_paths[node][1] > node_dist:
                    shortest_paths[node] = (curr_node, node_dist)

            next_nodes = {node: shortest_paths[node][1] for node in shortest_paths if node not in visited}
            if len(next_nodes) == 0:
                return None
            else:
                curr_node = min(next_nodes, key=next_nodes.get)

        return shortest_paths[end][1]

    def _compute_paths(self):
        nodes = [valve for valve in self.nodes]
        for node1 in nodes + ['AA']:
            for node2 in nodes:
                if node1 != node2:
                    self.distances[(node1, node2)] = self.shortest_path(node1, node2)

    def open_valve(self, pos, next_pos, time_limit, total_pressure):
        if isinstance(pos, str):
            time_limit -= (self.distances[pos, next_pos] + 1)
        else:
            time_limit -= (pos + 1)
        total_pressure -= time_limit*self.nodes[next_pos]

        return total_pressure, time_limit

    def get_max_pressure(self, start, time_limit):
        self.paths = []
        valves = [valve for valve in self.nodes]
        
        # initialize
        for valve in valves:
            results = self.open_valve(start, valve, time_limit, 0)
            self.paths.append([results[0], results[1], [valve]])
        heapq.heapify(self.paths)

        pressure = 0
        pressures = {}

        while self.paths:
            p, t, path = heapq.heappop(self.paths)
            for valve in valves:
                if valve not in path:
                    p2, t2 = self.open_valve(path[-1], valve, t, p)
                    if t2 >= 0:
                        heapq.heappush(self.paths, [p2, t2, path+[valve]])
                        pressures[tuple(path+[valve])] = (p2*-1)
        
        pressure = pressures[max(pressures, key=pressures.get)]
        return pressure

    def check_max(self, unseen, time, pressure, max_pressure):
        for valve in unseen:
            pressure -= self.nodes[valve]*time
        return pressure >= max_pressure

    def get_max_pressure_2(self, start, time_limit):
        paths = []
        heapq.heapify(paths)
        
        # initialize
        for valve in self.nodes:
            seen = [valve]
            v1 = (self.distances[start, valve], valve)
            for valve2 in self.nodes:
                if valve2 not in seen:
                    seen2 = seen.copy()
                    seen2.append(valve2)
                    v2 = (self.distances[start, valve2], valve2)
                    heapq.heappush(paths, [0, time_limit, v1, v2, seen2])
        
        pressure = 0
        while paths:
            p, t, v1, v2, seen = heapq.heappop(paths)
            # sort valves by distance
            v1, v2 = sorted((v1, v2))
            p2, t2 = self.open_valve(v1[0], v1[1], t, p)
            #update v2:
            v2 = (v2[0]-(t-t2), v2[1])

            # check time
            if t2 >= 0:
                # check pressure
                if p2 < pressure:
                    pressure = p2
                # check max possible score
                unseen = [node for node in self.nodes if node not in seen] + [v2[1]]
                if self.check_max(unseen, t2, p2, pressure):
                    continue
                # new v1
                for valve in self.nodes:
                    if valve not in seen:
                        new_v1 = (self.distances[v1[1], valve], valve)
                        new_seen = seen.copy()
                        new_seen.append(valve)
                        heapq.heappush(paths, [p2, t2, new_v1, v2, new_seen])
                if len(seen) == len(self.nodes):
                    p2, t2 = self.open_valve(v2[0], v2[1], t2, p2)
                    if t2 >= 0 and  p2<pressure:
                        pressure = p2

        return pressure*-1




def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))

    test_graph = Graph(test)
    graph = Graph(contents)
    
    #assert test_graph.get_max_pressure('AA', 30) == 1651, 'failed part 1 test'
    print(f'Part 1: {graph.get_max_pressure("AA", 30)}')

    #assert test_graph.get_max_pressure_2('AA', 26) == 1707, 'failed part 2 test'
    print(f'Part 2: {graph.get_max_pressure_2("AA", 26)}')


if __name__ == '__main__':
    __main__()
