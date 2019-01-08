from numpy import random as numpy_random


class Selection:
    def select(self, population):
        population = self._get_population(population)
        probability = self._get_probability(population)
        indexes = numpy_random.choice(len(population), size=len(population), p=probability)
        new_population = [population[index] for index in indexes]
        return new_population

    def _get_population(self, population):
        raise NotImplementedError

    def _get_probability(self, population):
        raise NotImplementedError


class ProportionalSelection(Selection):
    def __init__(self, a):
        self.a = a

    def _get_population(self, population):
        return population

    def _get_probability(self, population):
        probability = [0] * len(population)
        sum_ = 0
        for chromosome in population:
            sum_ += chromosome.profit() + self.a
        for index, chromosome in enumerate(population):
            probability[index] = (chromosome.profit() + self.a) / sum_
        return probability


class TournamentSelection(Selection):
    def __init__(self, s):
        self.s = s

    def _get_population(self, population):
        return sorted(population, key=lambda chromosome: chromosome.profit(), reverse=True)

    def _get_probability(self, population):
        probability = [0] * len(population)
        pop_len = len(population)
        for i in range(1, pop_len+1):
            probability[i-1] = (pow(pop_len-i+1, self.s) - pow(pop_len-i, self.s))/(pow(pop_len, self.s))
        return probability


class ThresholdSelection(Selection):
    def __init__(self, q):
        self.q = q

    def _get_population(self, population):
        return sorted(population, key=lambda chromosome: chromosome.profit(), reverse=True)

    def _get_probability(self, population):
        probability = [0] * len(population)
        pop_len = len(population)
        if int(pop_len*self.q) == 0:
            raise Exception("To small threshold for data !")
        for index, chromosome in enumerate(population):
            if index+1 <= pop_len*self.q:
                probability[index] = 1/(int(pop_len*self.q))
            else:
                probability[index] = 0
        return probability
