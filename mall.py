from graph import Graph, Node
from shops import SHOPS


def main():
    mall = Graph()
    for shop_id in SHOPS.keys():
        mall.add_node(Node(shop_id))

    mall.add_edge(mall.get_node(1), mall.get_node(2), 5.4)
