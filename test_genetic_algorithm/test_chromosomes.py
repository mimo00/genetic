from genetic_algorithm import chromosomes


class TestChromosomes:
    def test_profit_weights_are_sort_by_values(self):
        pw1 = chromosomes.ProfitWeight(profit=50, weight=40)
        pw2 = chromosomes.ProfitWeight(profit=100, weight=1)
        profit_weights = [pw1, pw2]
        chromosome = chromosomes.Chromosome(profit_weights, 40, [1, 0])
        assert chromosome.profit_weights == [pw2, pw1]

    def test_getting_profit(self):
        pw1 = chromosomes.ProfitWeight(profit=50, weight=15)
        pw2 = chromosomes.ProfitWeight(profit=100, weight=20)
        profit_weights = [pw1, pw2]
        chromosome = chromosomes.Chromosome(profit_weights, 40, [1, 0])
        assert chromosome.profit() == 100

    def test_getting_weight(self):
        pw1 = chromosomes.ProfitWeight(profit=50, weight=15)
        pw2 = chromosomes.ProfitWeight(profit=100, weight=20)
        profit_weights = [pw1, pw2]
        chromosome = chromosomes.Chromosome(profit_weights, 40, [1, 1])
        assert chromosome.weight() == 35

    def test_fitness(self):
        pw1 = chromosomes.ProfitWeight(profit=50, weight=15)
        pw2 = chromosomes.ProfitWeight(profit=100, weight=20)
        profit_weights = [pw1, pw2]
        chromosome = chromosomes.Chromosome(profit_weights, 10, [1, 1])
        chromosome.fitness()
        assert chromosome.data == [0, 0]
