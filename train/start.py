# TRAIN NEURAL NETWORK SNAKE WITH GENETIC ALGORITHM

# Importing Libraries
import json

# Importing local modules
from func import *
from population import *
from snakes import *
from inital import *


# ----------------------------------------------PLAY--------------------------------------------------


# Initialize data for start
snake_position = [[600, 600], [600, 650], [600, 700], [600, 750]]
population_num = 1500

display_width = 1200
display_height = 1200


# Start Training
def play(snake_position, population_num):
    weights = 0
    best_weights = 0

    for _ in range(5000):
        dead_snakes = []

        # Initialize snakes
        initClass = Initialize(snake_position, population_num, weights)
        population = initClass.population


        # Initialize visualize snake
        visualize_snake = Snake(snake_position, best_weights)
        Alive = True

        while population != [] or Alive:

            # Visualize snake
            if Alive:

                # Transmission
                coordData = {'snake': visualize_snake.snake_position, 'apple': visualize_snake.apple_position}
                with open("snake_front.json", "w") as frontsnake:
                    json.dump(coordData, frontsnake)

                visualize_snake.calcOutput()
                visualize_snake.nextStep()
                visualize_snake.generate()
                visualize_snake.calcInput()
                if is_direction_blocked(visualize_snake.snake_position, visualize_snake.coordinate_next_step) == 1 or visualize_snake.stayAlive == visualize_snake.lifetime:
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

                    if is_direction_blocked(population[i].snake_position, population[i].coordinate_next_step) == 1 or population[i].stayAlive == population[i].lifetime:
                        dead_snakes.append(population[i])
                    else:
                        new_population.append(population[i])

                population = new_population[:]

        pop = Population(num_parents=150, population=dead_snakes, mutation_rate=0.2)
        weights = pop.new_pop()
        best_weights = list(pop.best_weights)


if __name__=="__main__":
    play(snake_position, population_num)
