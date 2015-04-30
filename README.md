# P'polom
Find best conditions to import products based on mexican legislation; using Genetic Algorithms

---

_P'polom_ means «market» in mayan.

This project was created for both «Artificial Intelligence» and «Optimization and Linear Programming» courses on Spring '15 at Tecnológico de Monterrey, campus Querétaro.

Ppolom tries to find the best conditions to import products from another country into México, taking into consideration some International Trade concepts and mexican legislation.

---

## Darwin

To achieve this, «darwin» a small GA Framework is used and modified to match Ppolom needs.

The basics of darwin are really simple:

*   You must define a list of labels and possible values for each label
*   And a fitness function
*   It uses a Threshold Selector to select best individuals from a generation (only the top chromosomes survive each generation, based on a threshold using the fitness function)
*   A random-sized crossover is used

---

## 

_Theoretical information of International Trade and of the mexican legislation  with help from Sandy Ortega <3_