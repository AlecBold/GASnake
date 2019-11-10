# -----------------------------------------POPULATION--------------------------------------------

# Importing libraries
import random as rd
import numpy as np

# Importing local modules
from .func import *
from .Snake import *


class Population:
    def __init__(self, num_parents, population, mutation_rate):
        self.num_parents = num_parents
        self.population = list(population)
        self.score = 0
        self.offspring_size = len(self.population) - num_parents
        self.mutation_num = int(mutation_rate * 224)

    def exec_genetic_algorithm(self):
        self.select_mating_pool()
        self.crossover()
        self.mutation()

    def select_mating_pool(self):
        scores = []
        for i in range(len(self.population)):
            self.population[i].calcFitness()
            scores.append(self.population[i].fitness)

        self.parents = []
        self.maxFitness = max(scores)
        self.checkScores = []
        for _ in range(self.num_parents):
            max_scr_index = scores.index(max(scores))
            self.parents.append(self.population[max_scr_index].weights)
            self.checkScores.append(max(scores))
            scores[max_scr_index] = -99999999999

        self.best_weights = self.parents[0]

    def accept_reject(self):
        while True:
            idx = int(rd.uniform(0, len(self.parents)))
            partner = self.parents[idx]
            r = rd.uniform(0, self.maxFitness)
            if r < self.checkScores[idx]:
                return partner, idx

    def crossover(self):
        self.offspring = []
        for _ in range(self.offspring_size):
            child = weights_initialize()

            while True:
                parent1_w, idx1 = self.accept_reject()
                parent2_w, idx2 = self.accept_reject()

                if idx1 != idx2:
                    for l in range(len(parent1_w)):
                        layer = parent1_w[l]

                        for n in range(layer.shape[0]):

                            for w in range(layer.shape[1]):
                                if rd.uniform(0, 1) < 0.5:
                                    child[l][n, w] = parent1_w[l][n, w]
                                else:
                                    child[l][n, w] = parent2_w[l][n, w]

                    self.offspring.append(child)
                    break

    def mutation(self):
        for _ in range(self.mutation_num):
            for idx in range(len(self.offspring)):
                i = rd.randint(0, len(self.offspring[0]) - 1)
                random_layer = self.offspring[idx][i]
                i_x = rd.randint(0, random_layer.shape[0] - 1)
                i_y = rd.randint(0, random_layer.shape[1] - 1)

                random_value = np.random.choice(np.arange(-1, 1, step=0.001), size=(1), replace=False)
                self.offspring[idx][i][i_x, i_y] = random_value

    def new_pop(self):
        new_population = self.parents + self.offspring
        return new_population
