import enum
import random
import matplotlib.pyplot as plt

from genom import Genom
from graph import Graph, Node
from shops import SHOPS, DISTANCES


class SelectionMethod(enum.Enum):
    ROULETTE = 1
    TOURNAMENT = 2
    RANKING = 3


EPOCHS = 500
MUTATION = 0.001
CROSSING = 0.7
POPULATION_SIZE = 100
CHOOSEN_SHOPS = [1, 2, 3, 7, 16, 9, 5, 8, 22, 34]
SELECTION_METHOD = SelectionMethod.TOURNAMENT



def choose_best_examples(method, shops, k):
    if method == SelectionMethod.ROULETTE:
        return random.choices(shops, weights=[-1 / shop.score for shop in shops], k=k)
    elif method == SelectionMethod.TOURNAMENT:
        return [a if a.score > b.score else b for a, b in
                [random.choices(shops, weights=[-1 / shop.score for shop in shops], k=2) for _ in range(k)]]
    elif method == SelectionMethod.RANKING:
        return sorted(shops, key=lambda x: -x.score)[:k]


def main():
    mall = Graph()
    for shop_id in SHOPS.keys():
        mall.add_node(Node(shop_id))

    for node_one_id, node_two_id, distance in DISTANCES:
        mall.add_edge(mall.get_node(node_one_id), mall.get_node(node_two_id), distance)

    for node in mall.nodes.values():
        node.distances = mall.dijkstra(node)

    choosen_shops = [mall.get_node(node_id) for node_id in CHOOSEN_SHOPS]
    print ('Wybrano sklepy: {}'.format(', '.join([SHOPS[shop_id] for shop_id in CHOOSEN_SHOPS])))
    population = [Genom(choosen_shops, MUTATION) for _ in range(POPULATION_SIZE)]

    scores = []
    for epoch in range(EPOCHS):
        best_examples = choose_best_examples(SELECTION_METHOD, population, 30)
        # print([x.score for x in best_examples])
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            mom, dad = random.sample(best_examples, k=2)
            new_population += mom.cross(dad, CROSSING)
        population = new_population
        for shop in population:
            shop.mutate(MUTATION)

        scores.append(-sorted(population, key=lambda x: -x.score)[0].score)
    print ('Najlepsza trasa: {}'.format(', '.join([SHOPS[shop.id] for shop in sorted(population, key=lambda x: -x.score)[0].shops])))

    plt.plot(scores)
    plt.xlabel("Epoka")
    plt.ylabel("Odległość")
    plt.savefig('score.png')


if __name__ == '__main__':
    main()
