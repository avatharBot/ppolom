__author__ = 'avathar'

import json
import numpy as np
from darwin.ga import GeneticAlgorithm
from darwin.genotype import Genotype


global country_distance
global trade_agreements


def read_distance():
    with open('distances.json', 'r') as input_file:
        distances = json.load(input_file)
        data = {}
        for country in distances:
            data[country['id']] = {
                "country": country['country'],
                "distance": country['distance']
            }
        return data


def read_fta():
    with open('trade_agreements.json', 'r') as input_file:
        return json.load(input_file)


def fitness_function(chromosome):
    dec_value = 0
    global country_distance
    global trade_agreements
    country_code = chromosome.genes[0]
    quantity = chromosome.genes[1]
    dec_value += country_distance[country_code]['distance']
    dec_value += quantity

    for trade, countries in trade_agreements.items():
        if country_code not in countries:
            dec_value += 100000

    return dec_value


def main():

    global country_distance
    global trade_agreements
    country_distance = read_distance()
    trade_agreements = read_fta()

    labels = [
        'code',
        'units',
    ]
    values = [
        [code for code in country_distance.keys()],
        [i for i in range(0, 100000, 1000)]
    ]

    sample = Genotype(labels, values)
    ga = GeneticAlgorithm(population_size=500,
                          sample_genotype=sample,
                          crossover_rate=0.6,
                          mutation_rate=0.4,
                          maximize=True)
    best_generation = ga.evolve(fitness_function=fitness_function,
                                num_generations=6)

    print "Best Generation "
    all_fitness = []
    for chrom in best_generation:
        all_fitness.append(chrom.fitness)
    print "Avg fitness = " + str(np.average(all_fitness))
    print "Max fitness = " + str(np.max(all_fitness))
    print "Min fitness = " + str(np.min(all_fitness))
    print "Fitness std = " + str(np.std(all_fitness))
    print "\n"

    fittest = ga.best_individual(best_generation)
    print " Values for fittest individual"
    print "\tcountry:", country_distance[fittest['code']]['country']
    print "\tunits:", fittest['units']

if __name__ == '__main__':
    main()
