class Edge:
    def __init__(self, node_one, node_two, dist):
        self.node_one_ = node_one
        self.node_two_ = node_two
        self.dist_ = dist


class Node:
    def __init__(self, node_id):
        self.id_ = node_id
        self.edges = []

    def set_id(self, node_id):
        self.id_ = node_id


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




# g = Graph()
# g.addNode(Node(1))