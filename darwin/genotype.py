"""
    Properties:
        labels: user friendly label for each gene
        values: possible values for each gene
"""
import random
from chromosome import Chromosome


class Genotype(object):
    """
    Genotype defines the structure of a chromosome
    """
    def __init__(self, labels, values):
        self._labels = labels
        self._values = values
        self._formatter = None

    @property
    def formatter(self):
        """
        formatter: function that takes chromosome instance and returns a string
        """
        return self._formatter

    @formatter.setter
    def formatter(self, f_function):
        """
        setter for formatter
        """
        self._formatter = f_function

    def describe(self):
        """
        describe: tuple with genotype info
        """
        description = (len(self._values), self._labels, self._values)
        return description

    def num_genes(self):
        """
        num_genes: # genes in genotype
        """
        return len(self._values)

    def create_random_instance(self):
        """
        create_random_instance: creates chromosome with randomized gene values
        """
        instance = []
        for each in self._values:
            num = len(each) - 1
            index = random.randint(0, num)
            gene_value = each[index]
            instance.append(gene_value)

        chromosome = Chromosome(genes=instance)
        return chromosome

    def print_instance(self, instance):
        """
        string representation of a instance
        """
        c_string = ""
        if self._formatter is None:
            for gene in instance.genes:
                c_string += str(gene)
        else:
            c_string = self._formatter(instance)

        return c_string

    def get_label(self, pos):
        """
        get_label: label from gene position
        """
        return self._labels[pos]

    def get_pos(self, label):
        """
        get_pos: gene position from label
        """
        index = self._labels.index(label)
        return index

