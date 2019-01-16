from graph import Graph, Node
from shops import SHOPS, DISTANCES


def main():
    mall = Graph()
    for shop_id in SHOPS.keys():
        mall.add_node(Node(shop_id))

    for node_one_id, node_two_id, distance in DISTANCES:
        mall.add_edge(mall.get_node(node_one_id), mall.get_node(node_two_id), distance)

    for node in mall.nodes.values():
        node.distances = mall.dijkstra(node)


if __name__ == '__main__':
    main()
