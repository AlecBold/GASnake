# TRAIN NEURAL NETWORK SNAKE WITH GENETIC ALGORITHM

# Importing Libraries
import random as rd
from tqdm import tqdm
import time
import pygame
import os

# Change directory
print(os.getcwd())

# Importing local modules
from func import *
from population import *
from snakes import *

# -----------------------------------------DRAW SNAKE--------------------------------------------


# Display apple
def display_apple(apple_position, display):
    pygame.draw.rect(display, (230, 230, 230), (apple_position[0], apple_position[1], 50, 50))


# Display snake
def display_snake(snake_position, display):
    for cube in snake_position:
        pygame.draw.rect(display, (255, 255, 255), (cube[0], cube[1], 50, 50))


# -------------------------------------------INITIALIZE-----------------------------------------------


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


# ----------------------------------------------PLAY--------------------------------------------------


# Initialize data for start
snake_position = [[600, 600], [600, 650], [600, 700], [600, 750]]
population_num = 1500

display_width = 1200
display_height = 1200
pygame.init()
display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()


# Start Training
def play(snake_position, population_num, display = 0):
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
            display.fill((0, 0, 0))

            # Visualize snake
            if Alive:
                display_apple(visualize_snake.apple_position, display)
                display_snake(visualize_snake.snake_position, display)

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

            pygame.display.update()
            time.sleep(50.0 / 1000.0)

        pop = Population(num_parents=150, population=dead_snakes, mutation_rate=0.2)
        weights = pop.new_pop()
        best_weights = list(pop.best_weights)



# Display Snake
def snake(weights):
    while True:
        axis = rd.random()
        snake_position = []
        if axis > 0.5:
            tail = [rd.randrange(0, 1100), rd.randrange(0, 1100)]
            for _ in range(3):
                snake_position.append(tail[:])
                tail[0] += 50
        else:
            tail = [rd.randrange(0, 1100, 50), rd.randrange(0, 1100, 50)]
            for _ in range(3):
                snake_position.append(tail[:])
                tail[1] += 50

        while True:
            apple_position = [rd.randrange(0, 1200, 50), rd.randrange(0, 1200, 50)]
            if apple_position not in snake_position:
                break

        display_width = 1200
        display_height = 1200
        pygame.init()
        display = pygame.display.set_mode((display_width, display_height))
        clock = pygame.time.Clock()
        snake = Snake(snake_position, apple_position, weights)

        Live = True
        while Live:
            display.fill((0, 0, 0))

            for event in pygame.event.get():
                if event == pygame.QUIT:
                    Live = False

            display_apple(snake.apple_position, display)
            display_snake(snake.snake_position, display)

            snake.calcOutput()
            snake.nextStep()
            snake.generate()
            snake.calcInput()

            if  is_direction_blocked(snake.snake_position, snake.coordinate_next_step) == 1:
                Live = False

            pygame.display.update()
            time.sleep(50.0 / 1000.0)

if __name__=="__main__":
    play(snake_position, population_num, display)