"""
    GeneticAlgorithm operates over populations of chromosomes

    Properties:
        population_size: # chromosomes in populations
        genotype: structure of each chromosome
        generations: list of successive populations

    Methods:
        fit: runs the genetic algorithm, using selection, crossover, and mutati
        on operations
"""

from selectors import RankSelector
from crossover import OnePointCrossover
from chromosome import Chromosome
from mutation import Mutation
import random


from pprint import pprint

class GeneticAlgorithm(object):

    def __init__(self, population_size, sample_genotype, crossover_rate=0.6, mutation_rate=0.4, maximize=True):
        self.population_size = population_size
        self.genotype = sample_genotype
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.selector = RankSelector(maximize)
        self.crossover = OnePointCrossover()
        self.mutation = Mutation()
        self.generations = []

    def evolve(self, fitness_function, num_generations=10):
        # initialize population
        population = []
        for _ in range(self.population_size):
            chromosome = self.genotype.create_random_instance()
            population.append(chromosome)

        # process each generation
        for _ in range(num_generations):
            # track generations
            self.generations.append(population)
            next_population = []

            # calculate fitness function
            for chromosome in population:
                chromosome.fitness = fitness_function(chromosome)

            # select parents for next generation
            parents = self.selector.select_pairs(population=population)

            # perform crossover
            for parent in parents:
                do_crossover = random.random() < self.crossover_rate
                if do_crossover:
                    child_1, child_2 = self.crossover.recombine(
                        parent[0].genes,
                        parent[1].genes
                    )
                    chrom_child_1 = Chromosome(genes=child_1)
                    chrom_child_2 = Chromosome(genes=child_2)

                    # add new children to next population
                    next_population.append(chrom_child_1)
                    next_population.append(chrom_child_2)
                else:
                    # no crossover, add parents as is
                    next_population.append(parent[0])
                    next_population.append(parent[1])
            do_mutation = random.random() > self.mutation_rate
            if do_mutation:
                next_population = self.mutation.mutate(self.genotype, next_population)

            population = next_population
        # returns last/best population
        return population
