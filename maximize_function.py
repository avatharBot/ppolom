from darwin.ga import GeneticAlgorithm
from darwin.genotype import Genotype
from pprint import pprint
import numpy as np


def fitness_function(chromosome):
    dec_value = 0
    for locus in chromosome.genes:
        dec_value += locus
    return dec_value


def main():
    labels = [
        '8_bit',
        '7_bit',
        '6_bit',
        '5_bit',
        '4_bit',
        '3_bit',
        '2_bit',
        '1_bit'
    ]
    values = [
        [i for i in range(1,5)],
        [i for i in range(1,5)],
        [i for i in range(1,5)],
        [i for i in range(1,5)],
        [i for i in range(1,5)],
        [i for i in range(1,5)],
        [i for i in range(1,5)],
        [i for i in range(1,5)]
    ]

    max_value = 5*1024*3
    sample = Genotype(labels, values)
    ga = GeneticAlgorithm(population_size=200,
                          sample_genotype=sample,
                          crossover_rate=0.6,
                          threshold=20,
                          maximize=False)
    best_generation = ga.evolve(fitness_function=fitness_function,
              num_generations=5000)


    # for i,gen in enumerate(ga.generations):
    #     print "Generation ", i
    #     all_fitness = []
    #     for chrom in gen:
    #         all_fitness.append(chrom.fitness)
    #     print "Avg fitness = " + str(np.average(all_fitness))
    #     print "Max fitness = " + str(np.max(all_fitness))
    #     print "Min fitness = " + str(np.min(all_fitness))
    #     print "Fitness std = " + str(np.std(all_fitness))
    #     print "\n"
    print "Best generation"
    for chrom in best_generation:
        print chrom



if __name__ == '__main__':
    main()
