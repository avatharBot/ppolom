
class Chromosome(object):
    """
    Chromosome represents an individual
    """
    def __init__(self, genes):
        self._genes = genes
        self._fitness = 0

    @property
    def fitness(self):
        """
        fitness score
        """
        return self._fitness

    @fitness.setter
    def fitness(self, fitness):
        """
        setter for fitness property
        """
        self._fitness = fitness

    @property
    def genes(self):
        """
        genes = list of gene values
        """
        return self._genes


    def __str__(self):
        str = "%3.3i:\t[" % self._fitness
        for gen in self.genes:
            str += "%i," % gen
        return str + "]"
