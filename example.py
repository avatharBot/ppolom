__author__ = 'avathar'

from darwin.ga import GeneticAlgorithm
from darwin.genotype import Genotype

def fitness(chromosome):
    value = 0
    for locus in chromosome.genes:
        value += locus
    return value


def main():
    labels = ['slot 1', 'slot 2', 'slot 3', 'slot 4']
    values = [
        [i for i in range(10)],
        [i for i in range(20)],
        [i for i in range(30)],
        [i for i in range(40)]
    ]

    sample = Genotype(labels, values)
    ga = GeneticAlgorithm(population_size=50,
                          sample_genotype=sample,
                          crossover_rate=0.6,
                          mutation_rate=0.2,
                          maximize=True)
    best_generation = ga.evolve(fitness_function=fitness,
                                num_generations=5000)

    fittest = ga.best_individual(best_generation)

    print " Values for fittest "
    for locus in fittest:
        print locus[0], locus[1]


if __name__ == '__main__':
    main()