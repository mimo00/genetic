from numpy import random as numpy_random
import random
from genetic_algorithm import chromosomes


class Crossover:
    def crossover(self, population):
        raise NotImplementedError


class SinglePointCrossover:
    def __init__(self, proportion):
        assert proportion <= 1
        self.proportion = proportion

    def crossover(self, population):
        not_crossed_part = int((1 - self.proportion) * len(population))
        crossed_size = len(population) - not_crossed_part
        not_cossed_population_indexes = numpy_random.choice(len(population), size=not_crossed_part, replace=False)
        not_cossed_population = [population[index] for index in not_cossed_population_indexes]
        crossed_population = []
        for i in range(crossed_size):
            crossed_population_indexes = numpy_random.choice(len(population), size=2, replace=False)
            chrom0 = population[crossed_population_indexes[0]]
            chrom1 = population[crossed_population_indexes[1]]
            crossed_population.append(self.cross_chromosomes(chrom0, chrom1))
        new_population = crossed_population + not_cossed_population
        assert len(new_population) == len(population)
        return new_population

    def cross_chromosomes(self, chrom1, chrom2):
        point = random.randint(0, len(chrom1)-1)
        return chromosomes.Chromosome(chrom1.profit_weights, chrom1.max_weight, chrom1[:point] + chrom2[point:])
