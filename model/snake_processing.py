# TRAIN NEURAL NETWORK SNAKE WITH GENETIC ALGORITHM

# Importing Libraries
import json
import time
import datetime
import os

# Importing local modules
#from .func import *
from .Population import *
from .Snake import *
from .Initialize import *


# Start Training
class PlaySnake:

    def __init__(self):
        self.direct = './data/coords.json'
        self.coordData = []


    def create_file(self):
        open(self.direct, 'w+')

    def delete_file(self):
        os.remove(self.direct)

    def write_to_json(self):
        with open(self.direct, 'w') as file:
            json.dump(self.coordData, file)
            

    def handling_step(self, snake_object):
        snake_object.calcOutput()
        snake_object.nextStep()
        snake_object.generate()
        snake_object.calcInput()
        return snake_object


    def step_of_best_snake(self, snake_object):  # Best snake make a step
        snake_object = self.handling_step(snake_object)
        if (is_direction_blocked(snake_object.snake_position, snake_object.coordinate_next_step) == 1) or (snake_object.stayAlive == snake_object.lifetime):
            self.Alive = False
        return snake_object


    def step_of_other_snakes(self, population, dead_snakes):  # All population make a step
        new_population = []
        for i in range(len(population)):
            population[i] = self.handling_step(population[i])

            if (is_direction_blocked(population[i].snake_position, population[i].coordinate_next_step) == 1) or (population[i].stayAlive == population[i].lifetime):
                dead_snakes.append(population[i])
            else:
                new_population.append(population[i])
        population = new_population[:]
        return population, dead_snakes


    def sequence_of_process_model(self, snake_position, population_num, weights, best_weights):
        # Initialize population
        initClass = Initialize(snake_position, population_num, weights)
        population = initClass.get_pop()

        # Initialize visualize snake
        visualize_snake = Snake(snake_position, best_weights)

        dead_snakes = []
        self.coordData = []
        self.Alive = True

        while population != [] or self.Alive:
            if self.Alive:  # Best snake processing
                # Add coordinates to coordData for json file
                step = dict({'snake': visualize_snake.snake_position[:], 'apple': visualize_snake.apple_position[:]})
                self.coordData.append(step)

                visualize_snake = self.step_of_best_snake(visualize_snake)

            if population != []:  # All population processing
                population, dead_snakes = self.step_of_other_snakes(population, dead_snakes)

        pop = Population(num_parents=250, population=dead_snakes, mutation_rate=0.1)
        pop.exec_genetic_algorithm()
        weights = pop.new_pop()
        best_weights = list(pop.best_weights)
        return weights, best_weights


    def execute(self):
        snake_position = [[12, 12], [12, 13], [12, 14], [12, 15]]
        population_num = 1500
        weights = 0
        best_weights = 0
        generations = 0
        while True:
            # Create json file and write coordData
            self.create_file()
            self.write_to_json()

            # Process model
            weights, best_weights = self.sequence_of_process_model(snake_position, population_num, weights, best_weights)

            # Delete json file
            self.delete_file()

            # Translate num of generations
            generations += 1
            print(f"Generation # -> {generations}")

