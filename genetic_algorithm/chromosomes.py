import random
from typing import List


class ProfitWeight:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

    @property
    def value(self):
        return self.profit/self.weight


class Chromosome:
    def __init__(self, profit_weights: List[ProfitWeight], max_weight, data=None):
        self.max_weight = max_weight
        self.profit_weights = sorted(profit_weights, key=lambda profit_weight: profit_weight.value, reverse=True)
        if data:
            self.data = data
        else:
            self.data = [random.randint(0, 1) for _ in range(len(profit_weights))]

    def profit(self):
        profit = 0
        for index, i in enumerate(self.data):
            if i == 1:
                profit += self.profit_weights[index].profit
        return profit

    def weight(self):
        weight = 0
        for bit_index, bit in enumerate(self.data):
            if bit == 1:
                weight += self.profit_weights[bit_index].weight
        return weight

    def fitness(self):
        while self.weight() > self.max_weight:
            self._fit()

    def _fit(self):
        ones_indexes = [index for index, element in enumerate(self.data) if element == 1]
        random_index = random.choice(ones_indexes)
        self.data[random_index] = 0

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __len__(self):
        return len(self.data)
