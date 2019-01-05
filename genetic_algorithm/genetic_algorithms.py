from typing import List

from genetic_algorithm import chromosomes
from . import selections
from . import crossovers
from . import mutations
import numpy

# population_size - ile na raz mozliwosci przechowujemy
# A - wagi przemiotow / ile zlota chca kupic pasazerowie ai
# V - za ile chce kupic swoją część złota


class GeneticAlgorithm:
    def __init__(self, profit_weights: List[chromosomes.ProfitWeight], max_weight, population_size, max_generation,
                 selector=selections.ProportionalSelection(0.1),
                 crossover_obj=crossovers.SinglePointCrossover(0.5),
                 mutator=mutations.Mutation(0.001)):
        self.profit_weights = profit_weights
        self.population_size = population_size
        self.max_weight = max_weight
        self.max_generation = max_generation
        self.selector = selector
        self.crossover_obj = crossover_obj
        self.mutator = mutator

    def start(self):
        population = self._generate_initial_population()
        self._fitness(population)
        generation_number = 0
        while not self._end(generation_number):
            population = self.mutate(self.crossover(self.select(population)))
            self._fitness(population)
            generation_number += 1
            print(self._get_data(population))

    def _generate_initial_population(self):
        population = [chromosomes.Chromosome(self.profit_weights, self.max_weight) for _ in range(self.population_size)]
        return population

    def _fitness(self, population):
        for chromosome in population:
            chromosome.fitness()

    def _end(self, generation_number):
        return generation_number > self.max_generation

    def select(self, population):
        return self.selector.select(population)

    def crossover(self, population):
        return self.crossover_obj.crossover(population)

    def mutate(self, population):
        return self.mutator.mutate(population)

    def _get_data(self, population):
        values = [chromosom.profit() for chromosom in population]
        return ((max(values), numpy.mean(values)))
