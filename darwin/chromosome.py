
class Chromosome(object):
    """
    Chromosome represents an individual
    """
    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0


    def __str__(self):
        """
            String representation of a chromosome, with fitness and genes
        """
        str = "%3.3i:\t[ " % self.fitness
        for gen in self.genes:
            str += "%i " % gen
        return str + "]"
