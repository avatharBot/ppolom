__author__ = 'avathar'

import json
import numpy as np
from darwin.ga import GeneticAlgorithm
from darwin.genotype import Genotype


distances = list()
trade_agreements = list()
quotas = list()
products = list()
item = '0708.20.01'


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


def read_file(filename):
    with open(filename, 'r') as input_file:
        return json.load(input_file)


def fitness_function(chromosome):
    fitness_value = 0
    global distances
    global trade_agreements
    global quotas
    global products
    global item
    country_code = chromosome.genes[0]
    quantity = chromosome.genes[1]
    tax = 0
    item_fta = None
    item_quota = 0
    # get distance to country
    country_distance = distances[country_code]['distance']
    # find tax for product
    for fta, countries in trade_agreements.items():
        if country_code in countries:
            tax = products[item]['fta'][fta]
            item_fta = fta
        else:
            tax = products[item]['tax']
    if tax is None:
        tax = products[item]['tax']
    if item in quotas:
        item_quota = quotas[item]['quota']
        if not isinstance(item_quota, int):
            if item_fta is not None and item_fta in item_quota:
                item_quota = quotas[item]['quota'][item_fta]
            else:
                item_quota = 0

    quota_delta = abs(item_quota - quantity)
    fitness_value = country_distance + quota_delta + (tax*quota_delta)
    return fitness_value


def main():
    global distances
    global trade_agreements
    global quotas
    global products
    distances = read_distance()
    trade_agreements = read_file('trade_agreements.json')
    quotas = read_file('quotas.json')
    products = read_file('products.json')

    labels = [
        'code',
        'units',
    ]
    values = [
        [code for code in distances.keys()],
        [i for i in range(1000, 10000000, 1000)]
    ]

    sample = Genotype(labels, values)
    ga = GeneticAlgorithm(population_size=200,
                          sample_genotype=sample,
                          crossover_rate=0.6,
                          mutation_rate=0.02,
                          maximize=False)
    best_generation = ga.evolve(fitness_function=fitness_function,
                                num_generations=500)

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
    print "\tcountry:", distances[fittest['code']]['country']
    print "\tunits:", fittest['units']

if __name__ == '__main__':
    main()
