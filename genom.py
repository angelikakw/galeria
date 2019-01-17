import random
from copy import copy


class Genom(object):

    def __init__(self, shops, shuffle=True):
        self.shops = copy(shops)
        if shuffle:
            random.shuffle(self.shops)
        self.score = self.evaluate()

    def mutate(self, prob):
        if random.random() < prob:
            a, b = random.sample(range(len(self.shops)), k=2)
            temp_town = copy(self.shops[b])
            self.shops[b] = self.shops[a]
            self.shops[a] = temp_town
            self.score = self.evaluate()

    def cross(self, other_genom, prob):
        cross_min, cross_max = sorted(random.sample(range(len(self.shops)), k=2))
        shops_a = copy(self.shops)
        shops_b = copy(other_genom.shops)

        if random.random() < prob:
            trans_a = {}
            trans_b = {}

            for shop_a, shop_b in zip(shops_a[cross_min:cross_max], shops_b[cross_min:cross_max]):
                trans_a[shop_b.id] = shop_a
                trans_b[shop_a.id] = shop_b

            for shops, trans, trans_2 in [(shops_a, trans_a, trans_b), (shops_b, trans_b, trans_a)]:
                for i in range(len(shops_a)):
                    if cross_min <= i < cross_max:
                        shops[i] = trans_2[shops[i].id]
                    else:
                        new_shop = shops[i]
                        while new_shop.id in trans:
                            new_shop = trans[new_shop.id]
                        shops[i] = new_shop

        return [Genom(shops_a, False), Genom(shops_b, False)]

    def evaluate(self):
        sum_dist = 0
        for prev_shop, shop in zip(self.shops[:-1], self.shops[1:]):
            sum_dist += prev_shop.distances[shop.id]
        return -sum_dist
