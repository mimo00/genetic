import argparse
import csv

import matplotlib.pyplot as plt
import pandas as pd

import genetic_algorithm.chromosomes
from genetic_algorithm import crossovers
from genetic_algorithm import genetic_algorithms
from genetic_algorithm import mutations
from genetic_algorithm import selections


def get_profit_weights(profits_csv, weights_csv):
    profits = []
    weights = []
    with open(profits_csv, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            profits += row
    profits = [float(i) for i in profits]
    with open(weights_csv, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            weights += row
    weights = [float(i) for i in weights]
    profit_weights = []
    for i in zip(profits, weights):
        profit_weights.append(genetic_algorithm.chromosomes.ProfitWeight(i[0], i[1]))
    return profit_weights


def experiment(genetic_algorithm: genetic_algorithms.GeneticAlgorithm):
    genetic_algorithm.start()
    df = pd.DataFrame({
        'max': genetic_algorithm.maxs,
        'mean': genetic_algorithm.means,
        'min': genetic_algorithm.mins,
    }, index=genetic_algorithm.generations)
    df.plot()
    plt.show()


def selection_strategy(selection_type):
    selector_map = {
        'proportional': selections.ProportionalSelection,
        'tournament': selections.TournamentSelection,
        'threshold': selections.ThresholdSelection,
    }
    return selector_map[selection_type]


parser = argparse.ArgumentParser(description='Run genetic algorithm')
parser.add_argument('profits', metavar='profits_csv', type=str, help='path to profit csv file')
parser.add_argument('weights', metavar='weights_csv', type=str, help='path to weights csv file')
parser.add_argument('max_weight', metavar='max_weight', type=int, help='Max weight of knapsack')
parser.add_argument('population_size', metavar='population_size', type=int, help='Population size')
parser.add_argument('max_generations', metavar='max_generations', type=int, help='Max generation number')
parser.add_argument('selection_type', metavar='selection_type', type=str, help='Selection type')
parser.add_argument('selection_parameter', metavar='selection_parameter', type=float, help='Selection parameter')
parser.add_argument('crossover_parameter', metavar='crossover_parameter',
                    type=float, help='Percent of population to crossover')
parser.add_argument('mutation_parameter', metavar='mutation_parameter',
                    type=float, help='Probability of changing bit in mutation')


if __name__ == "__main__":
    args = parser.parse_args()
    profit_weights = get_profit_weights(args.profits, args.weights)
    selector = selection_strategy(args.selection_type)(args.selection_parameter)
    crossover_obj = crossovers.SinglePointCrossover(args.crossover_parameter)
    mutator = mutations.Mutation(args.mutation_parameter)
    genetic_algorithm = genetic_algorithms.GeneticAlgorithm(
        profit_weights, args.max_weight, args.population_size, args.max_generations,
        selector=selector, crossover_obj=crossover_obj, mutator=mutator)
    experiment(genetic_algorithm)
