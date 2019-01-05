import random


class Mutation:
    def __init__(self, probability):
        self.probability = probability

    def mutate(self, population):
        for chromosome in population:
            for index, bit in enumerate(chromosome):
                if random.random() < self.probability:
                    if chromosome[index] == 1:
                        chromosome[index] = 0
                    else:
                        chromosome[index] = 1
        return population



