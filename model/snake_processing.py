# TRAIN NEURAL NETWORK SNAKE WITH GENETIC ALGORITHM

# Importing Libraries
import json
import time
import datetime
import os
import pymongo

# Importing local modules
from .func import *
from .Population import *
from .Snake import *
from .Initialize import *


# Start Training
class PlaySnake:
    def __init__(self):
        self.direct = './data/coords.json'
        #self.access_to_mongodb()

    def create_file(self):
        open(self.direct, 'w+')

    def delete_file(self):
        os.remove(self.direct)

    def write_to_json(self):
        with open(self.direct, 'w') as file:
            json.dump(self.coordData, file)

    def access_to_mongodb(self):
        client = pymongo.MongoClient("mongodb+srv://AlexMongoDB:Takemetoyoureleader2291773@cluster0-p5ad5.mongodb.net/test?retryWrites=true&w=majority")
        self.db = client.dataSnake

    def save_weights_in_db(self, weights):
        weights = [arr.tolist() for arr in weights]
        doc = {'weights': weights, 'date': datetime.datetime.now()}
        self.db.data_weights.insert_one(doc)

    def execute(self):
        snake_position = [[12, 12], [12, 13], [12, 14], [12, 15]]
        population_num = 1500
        weights = 0
        best_weights = 0

        while True:
            dead_snakes = []

            # Initialize snakes
            initClass = Initialize(snake_position, population_num, weights)
            population = initClass.get_pop()

            # Initialize visualize snake
            visualize_snake = Snake(snake_position, best_weights)
            Alive = True
            self.coordData = []

            while population != [] or Alive:

                # Visualize snake
                if Alive:

                    # Add steps
                    step = dict({'snake': visualize_snake.snake_position[:], 'apple': visualize_snake.apple_position[:]})
                    self.coordData.append(step)

                    visualize_snake.calcOutput()
                    visualize_snake.nextStep()
                    visualize_snake.generate()
                    visualize_snake.calcInput()

                    if (is_direction_blocked(visualize_snake.snake_position, visualize_snake.coordinate_next_step) == 1) \
                            or (visualize_snake.stayAlive == visualize_snake.lifetime):
                        Alive = False

                # All population
                if population != []:
                    # All population make a step
                    new_population = []
                    for i in range(len(population)):

                        population[i].calcOutput()
                        population[i].nextStep()
                        population[i].generate()
                        population[i].calcInput()

                        if (is_direction_blocked(population[i].snake_position, population[i].coordinate_next_step) == 1) \
                                or (population[i].stayAlive == population[i].lifetime):

                            dead_snakes.append(population[i])
                        else:
                            new_population.append(population[i])

                    population = new_population[:]

            self.create_file()
            self.write_to_json()

            pop = Population(num_parents=250, population=dead_snakes, mutation_rate=0.25)
            pop.exec_genetic_algorithm()
            weights = pop.new_pop()
            best_weights = list(pop.best_weights)

            #self.save_weights_in_db(best_weights)
            self.delete_file()
