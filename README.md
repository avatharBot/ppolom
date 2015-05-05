# P'polom
Find best conditions to import products based on mexican legislation; using Genetic Algorithms

---

_P'polom_ means «market» in mayan.


Ppolom tries to find the best conditions to import products from another country into México, taking into consideration some International Trade concepts and mexican legislation.
It is important to state that this is not meant to be a solution tool, but rather a solution model for this problem. Some simplification on import taxes and product selection was done to reduce the scope of the project (this was mostly due to time constraints)

---

### Darwin

To achieve this, «Darwin» a small GA Framework is used and then configured to match Ppolom needs. 
_I may separate darwin on a different repository. For now, it stays here._


The basics of Darwin are really simple:

*   Define a list of labels and possible values for each label
*   Define a fitness function
*   A Rank Selector is used to select best individuals from a generation (only the top half chromosomes survive each generation)
*   A random-sized Crossover operation is used (based on a crossover rate)
*   A simple Mutation operation is used (mutates a third of the population based on a mutation rate)

---

### Ppolom


_This project was created for both «Artificial Intelligence» and «Optimization and Linear Programming» courses on Spring'15 at Tecnológico de Monterrey, campus Querétaro by me._

_Theoretical information of International Trade and of the mexican legislation  with help from Sandy Ortega :grin: Thank you!_