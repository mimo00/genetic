import csv

import genetic_algorithm.chromosomes

profits = []
with open('test_data/p1w.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        profits += row
profits = [float(i) for i in profits]

weights = []
with open('test_data/w1u.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        weights += row
weights = [float(i) for i in weights]

from genetic_algorithm import genetic_algorithms

profit_weights = []
for i in zip(profits, weights):
    profit_weights.append(genetic_algorithm.chromosomes.ProfitWeight(i[0], i[1]))


g_a = genetic_algorithms.GeneticAlgorithm(profit_weights, 100, 50, 100000)
g_a.start()