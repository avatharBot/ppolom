"""

    Selectors choose candidate parents from a given population

    input: population of chromosomes
    output: pairs of selected parent chromosomes

    types:
        RankSelector: only selects parents with fitness rank above specified threshold
        RouletteSelector: uses probabilistic model to select parents based on relative fitness
"""
import random
import numpy as np


class SelectionOperator(object):
    def select_pairs(self, population):
        raise NotImplementedError


class ThresholdSelector(SelectionOperator):
    def __init__(self, threshold, maximize):
        self.threshold = threshold
        self.maximize = maximize

    def select_pairs(self, population):
        pop_size = len(population)
        parent_size = pop_size / 2

        # sort population by rank
        population.sort(key=lambda x: x.fitness, reverse=self.maximize)

        # take individuals above threshold
        parent_pool = population[0:self.threshold]
        # pair off
        parents = []
        while len(parents) < parent_size:
            random_1 = random.randint(0, len(parent_pool)-1)
            random_2 = random.randint(0, len(parent_pool)-1)
            parent_1 = parent_pool[random_1]
            parent_2 = parent_pool[random_2]
            parents.append([parent_1, parent_2])

        return parents


class RouletteSelector(SelectionOperator):
    def select_pairs(self, population):
        # create wheel points
        size = len(population)
        pointer_size = 1.0 / float(size)
        spin = random.random() * pointer_size
        wheel_pointers = np.empty(size)
        wheel_pointers.fill(pointer_size)
        wheel_pointers = np.multiply(wheel_pointers[0], range(size))
        wheel_pointers = np.add(wheel_pointers, spin)
        wheel_pointers = np.reshape(wheel_pointers, (size, 1))

        # create wheel spaces
        fitness = []
        for chrom in population:
            fitness.append(chrom.fitness)
        total_fitness = np.sum(fitness)
        norm_fitness = np.divide(fitness, total_fitness)
        current_pointer = 0
        wheel_spaces = []
        for fit in norm_fitness:
            space = fit + current_pointer
            wheel_spaces.append(space)
            current_pointer = space

        # select from wheel
        parent_pool = []
        wheel_selections = np.less_equal(wheel_pointers, wheel_spaces)
        for wheel in wheel_selections:
            index = wheel.argmax()
            parent_pool.append(population[index])

        # pair off parents
        parents = []
        for i in range(0, size, 2):
            parent_1 = parent_pool[i]
            parent_2 = parent_pool[i+1]
            parents.append([parent_1, parent_2])

        return parents
