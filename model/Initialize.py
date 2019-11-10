# -------------------------------------------INITIALIZE-----------------------------------------------

# Importing local files
from .Snake import *


class Initialize:
    def __init__(self, snake_position, pop_num, weights):
        self.snake_position = snake_position[:]
        self.pop_num = pop_num
        self.weights = weights

        self.population = []

        if weights == 0:
            self.start()
        else:
            self.update()

    def start(self):
        for _ in range(self.pop_num):
            self.population.append(Snake(self.snake_position, self.weights))

    def update(self):
        for i in range(self.pop_num):
            self.population.append(Snake(self.snake_position, self.weights[i][:]))

    def get_pop(self):
        return self.population[:]

