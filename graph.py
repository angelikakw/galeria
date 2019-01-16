from heapq import heappush, heappop


class Edge:
    def __init__(self, node_one, node_two, dist):
        self.node_one = node_one
        self.node_two = node_two
        self.dist = dist


class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.edges = []

    def set_id(self, node_id):
        self.id = node_id


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.id] = node

    def add_edge(self, node_one, node_two, dist):
        edge = Edge(node_one, node_two, dist)
        node_one.edges.append(edge)

        edge = Edge(node_two, node_one, dist)
        node_two.edges.append(edge)

    def get_node(self, node_id):
        return self.nodes[node_id]

    def dijkstra(self, node):
        dist = {node.id: 0}
        nodes_to_check = []

        for edge in node.edges:
            dest = edge.node_two
            heappush(nodes_to_check, (edge.dist, dest.id))

        while nodes_to_check:
            distance, node_id = heappop(nodes_to_check)
            if node_id not in dist:
                node = self.get_node(node_id)
                dist[node.id] = distance

                for edge in node.edges:
                    dest = edge.node_two
                    heappush(nodes_to_check, (edge.dist + dist[node.id], dest.id))
        return dist
