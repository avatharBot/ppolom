__author__ = 'avathar'

import json
from darwin.ga import GeneticAlgorithm
from darwin.genotype import Genotype


def read_distance():
    with open('all_distances.json', 'r') as input:
        distances = json.load(input)
        data = {}
        for country in distances:
            data[country['id']] = (country['code'], country['distance'])
        return data


def fitness_function(chromosome):
    dec_value = 0
    global distances
    dec_value += distances[chromosome.genes[0]][1]
    dec_value += chromosome.genes[1]*10000
    return dec_value

def fitness(chrom):
    value = 0
    for locus in chrom.genes:
        value += locus

    return value

def main():

    global distances
    distances = read_distance()

    labels = [
        'country',
        'units',
    ]
    values = [
        [code for code in distances.keys()],
        [i for i in range(1,111)]
    ]

    sample = Genotype(labels, values)
    ga = GeneticAlgorithm(population_size=200,
                          sample_genotype=sample,
                          crossover_rate=0.6,
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
