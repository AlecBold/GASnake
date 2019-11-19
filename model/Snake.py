# ----------------------------------------SNAKES--------------------------------------------------

# Importing libraries
import random as rd
import math
import numpy as np

# Importing local modules
from .func import *


class Snake:
    def __init__(self, snake_position, weights):
        self.snake_position = snake_position[:]
        self.coordinate_next_step = snake_position[0]

        while True:
            self.apple_position = [rd.randrange(0, 25), rd.randrange(0, 25)]
            if self.apple_position not in self.snake_position:
                break

        self.weights = weights
        if self.weights == 0:
            self.weights = weights_initialize()

        self.stayAlive = 100
        self.lifetime = 0
        self.sum_apple = 0
        self.fitness = 0

        self.calcInput()

    def oneBlockWall(self):
        block_right = 0
        block_up = 0
        block_left = 0
        block_down = 0

        if self.snake_position[0][0] + 1 > 24 or [self.snake_position[0][0] + 1, self.snake_position[0][1]] in self.snake_position[1:]:
            block_right = 1
        if self.snake_position[0][0] - 1 < 0 or [self.snake_position[0][0] - 1, self.snake_position[0][1]] in self.snake_position[1:]:
            block_left = 1
        if self.snake_position[0][1] + 1 > 24 or [self.snake_position[0][0], self.snake_position[0][1] + 1] in self.snake_position[1:]:
            block_down = 1
        if self.snake_position[0][1] - 1 < 0 or [self.snake_position[0][0], self.snake_position[0][1] - 1] in self.snake_position[1:]:
            block_up = 1

        return block_right, block_up, block_left, block_down

    def oneBlockTale(self):
        block_R = 0
        block_U = 0
        block_L = 0
        block_D = 0

        if [self.snake_position[0][0] + 1, self.snake_position[0][1]] in self.snake_position[1:]:
            block_R = 1
        if [self.snake_position[0][0] - 1, self.snake_position[0][1]] in self.snake_position[1:]:
            block_L = 1
        if [self.snake_position[0][0], self.snake_position[0][1] + 1] in self.snake_position[1:]:
            block_D = 1
        if [self.snake_position[0][0], self.snake_position[0][1] - 1] in self.snake_position[1:]:
            block_U = 1

        return block_R, block_U, block_L, block_D

    def myDirection(self):  # Check what direction snake goes (need to change or delete)
        dirR = 0
        dirU = 0
        dirL = 0
        dirD = 0

        if [self.snake_position[1][0] + 1, self.snake_position[1][1]] == self.snake_position[0]:
            dirR = 1
        elif [self.snake_position[1][0] - 1, self.snake_position[1][1]] == self.snake_position[0]:
            dirL = 1
        elif [self.snake_position[1][0], self.snake_position[1][1] + 1] == self.snake_position[0]:
            dirD = 1
        elif [self.snake_position[1][0], self.snake_position[1][1] - 1] == self.snake_position[0]:
            dirU = 1

        return dirR, dirU, dirL, dirD

    def distance_to_wall(self):
        wall_direction_vector_R = abs(25 - self.snake_position[0][0])
        wall_direction_vector_U = abs(0 - self.snake_position[0][1])
        wall_direction_vector_L = abs(0 - self.snake_position[0][0])
        wall_direction_vector_D = abs(25 - self.snake_position[0][1])

        if wall_direction_vector_R > wall_direction_vector_U:  # compute distance to upper right corner
            wall_direction_vector_RU = wall_direction_vector_U / math.cos(45)
        else:
            wall_direction_vector_RU = wall_direction_vector_R / math.cos(45)

        if wall_direction_vector_R > wall_direction_vector_D:  # compute distance to down right corner
            wall_direction_vector_RD = wall_direction_vector_D / math.cos(45)
        else:
            wall_direction_vector_RD = wall_direction_vector_R / math.cos(45)

        if wall_direction_vector_L > wall_direction_vector_U:  # compute distance to up left corner
            wall_direction_vector_LU = wall_direction_vector_U / math.cos(45)
        else:
            wall_direction_vector_LU = wall_direction_vector_L / math.cos(45)

        if wall_direction_vector_L > wall_direction_vector_D:  # compute distance to down left corner
            wall_direction_vector_LD = wall_direction_vector_D / math.cos(45)
        else:
            wall_direction_vector_LD = wall_direction_vector_L / math.cos(45)

        # Normalize distance for tail
        wall_direction_vector_R_norm = 1 - wall_direction_vector_R / 25
        wall_direction_vector_U_norm = 1 - wall_direction_vector_U / 25
        wall_direction_vector_L_norm = 1 - wall_direction_vector_L / 25
        wall_direction_vector_D_norm = 1 - wall_direction_vector_D / 25

        # NEED TO CHANGE SCALES (DON'T FORGET)
        wall_direction_vector_RU_norm = 1 - wall_direction_vector_RU / 1700
        wall_direction_vector_RD_norm = 1 - wall_direction_vector_RD / 1700
        wall_direction_vector_LU_norm = 1 - wall_direction_vector_LU / 1700
        wall_direction_vector_LD_norm = 1 - wall_direction_vector_LD / 1700

        return wall_direction_vector_R_norm, wall_direction_vector_U_norm, wall_direction_vector_L_norm, wall_direction_vector_D_norm, wall_direction_vector_RU_norm, wall_direction_vector_RD_norm, wall_direction_vector_LU_norm, wall_direction_vector_LD_norm

    def direction_to_apple(self):
        apple_direction_vector_R = 1
        apple_direction_vector_U = 1
        apple_direction_vector_L = 1
        apple_direction_vector_D = 1
        apple_direction_vector_RU = 1
        apple_direction_vector_RD = 1
        apple_direction_vector_LU = 1
        apple_direction_vector_LD = 1

        # Check if apple exist in 8 directions relative to head

        if (self.apple_position[0] - self.snake_position[0][0] < 0) and self.apple_position[1] == self.snake_position[0][1]:
            apple_direction_vector_L = 0 #- abs(self.apple_position[0] - self.snake_position[0][0]) / 1200
            #apple_direction_vector_R = 0
        elif (self.apple_position[0] - self.snake_position[0][0] > 0) and self.apple_position[1] == self.snake_position[0][1]:
            apple_direction_vector_R = 0 #- abs(self.apple_position[0] - self.snake_position[0][0]) /
            #apple_direction_vector_L = 0
        elif (self.apple_position[1] - self.snake_position[0][1] < 0) and self.apple_position[0] == self.snake_position[0][0]:
            apple_direction_vector_U = 0 #- abs(self.apple_position[1] - self.snake_position[0][1]) / 1200
            #apple_direction_vector_D = 0
        elif (self.apple_position[1] - self.snake_position[0][1] > 0) and self.apple_position[0] == self.snake_position[0][0]:
            apple_direction_vector_D = 0 #- abs(self.apple_position[1] - self.snake_position[0][1]) / 1200
            #apple_direction_vector_U = 0

        # 1 if apple on certain diagonal
        elif ((self.apple_position[0] - self.snake_position[0][0]) > 0) and ((self.apple_position[1] - self.snake_position[0][1]) < 0) and (abs(self.snake_position[0][0] - self.apple_position[0]) == abs(self.snake_position[0][1] - self.apple_position[1])):
            apple_direction_vector_RU = 0
        elif ((self.apple_position[0] - self.snake_position[0][0]) > 0) and ((self.apple_position[1] - self.snake_position[0][1]) > 0) and (abs(self.snake_position[0][0] - self.apple_position[0]) == abs(self.snake_position[0][1] - self.apple_position[1])):
            apple_direction_vector_RD = 0
        elif ((self.apple_position[0] - self.snake_position[0][0]) < 0) and ((self.apple_position[1] - self.snake_position[0][1]) < 0) and (abs(self.snake_position[0][0] - self.apple_position[0]) == abs(self.snake_position[0][1] - self.apple_position[1])):
            apple_direction_vector_LU = 0
        elif ((self.apple_position[0] - self.snake_position[0][0]) < 0) and ((self.apple_position[1] - self.snake_position[0][1]) > 0) and (abs(self.snake_position[0][0] - self.apple_position[0]) == abs(self.snake_position[0][1] - self.apple_position[1])):
            apple_direction_vector_LD = 0

        return apple_direction_vector_R, apple_direction_vector_U, apple_direction_vector_L, apple_direction_vector_D, apple_direction_vector_RU, apple_direction_vector_RD, apple_direction_vector_LU, apple_direction_vector_LD

    def distance_to_tale(self):

        tail_direction_vector_R = 0
        checkR = True
        tail_direction_vector_L = 0
        checkL = True
        tail_direction_vector_D = 0
        checkD = True
        tail_direction_vector_U = 0
        checkU = True

        for i in range(1, len(self.snake_position)):
            if self.snake_position[0][0] - self.snake_position[i][0] < 0 and self.snake_position[0][1] == self.snake_position[i][1] and checkR:  #Right check
                tail_direction_vector_R = 1 - abs(self.snake_position[0][0] - self.snake_position[i][0]) / 25
                checkR = False
            if self.snake_position[0][0] - self.snake_position[i][0] > 0 and self.snake_position[0][1] == self.snake_position[i][1] and checkL:  #Left check
                tail_direction_vector_L = 1 - abs(self.snake_position[0][0] - self.snake_position[i][0]) / 25
                checkL = False
            if self.snake_position[0][1] - self.snake_position[i][1] < 0 and self.snake_position[0][0] == self.snake_position[i][0] and checkD:  #Down check
                tail_direction_vector_D = 1 - abs(self.snake_position[0][0] - self.snake_position[i][0]) / 25
                checkD = False
            if self.snake_position[0][1] - self.snake_position[i][1] > 0 and self.snake_position[0][0] == self.snake_position[i][0] and checkU:  #Up check
                tail_direction_vector_U = 1 - abs(self.snake_position[0][0] - self.snake_position[i][0]) / 25
                checkU = False

        return tail_direction_vector_R, tail_direction_vector_U, tail_direction_vector_L, tail_direction_vector_D

    def calcInput(self):
        # dstwR, dstwU, dstwL, dstwD, dstwRU, dstwRD, dstwLU, dstwLD = self.distance_to_wall()
        diraR, diraU, diraL, diraD, diraRU, diraRD, diraLU, diraLD = self.direction_to_apple()
        # dsttR, dsttU, dsttL, dsttD = self.distance_to_tale()
        onbwR, onbwU, onbwL, onbwD = self.oneBlockWall()
        # onbtR, onbtU, onbtL, onbtD = self.oneBlockTale()
        dirR, dirU, dirL, dirD = self.myDirection()
        self.input = [onbwR, onbwU, onbwL, onbwD, dirR,   dirU,   dirL,   dirD,
                      diraR, diraU, diraL, diraD, diraRU, diraRD, diraLU, diraLD]

    def calcOutput(self):
        self.output = outputData(self.input, self.weights)

    def nextStep(self):  # Calculate coordinate next step
        predicted_direction = np.argmax(self.output)

        if predicted_direction == 0:  # Right
            self.coordinate_next_step = (self.snake_position[0] + np.array([1, 0])).tolist()
        elif predicted_direction == 2:  # Left
            self.coordinate_next_step = (self.snake_position[0] + np.array([-1, 0])).tolist()
        elif predicted_direction == 3:  # Down
            self.coordinate_next_step = (self.snake_position[0] + np.array([0, 1])).tolist()
        elif predicted_direction == 1:  # Up
            self.coordinate_next_step = (self.snake_position[0] + np.array([0, -1])).tolist()

    def calcFitness(self):
        if len(self.snake_position) < 10:
            self.fitness = int(self.lifetime**2 * 2**int(len(self.snake_position)))
        else:
            self.fitness = self.lifetime**2 * 2*10 * (len(self.snake_position) - 9)

    def generate(self):
        self.lifetime += 1

        if self.coordinate_next_step == self.apple_position:
            self.stayAlive *= 2
            self.sum_apple += 1

            # Generate new random apple
            while True:
                self.apple_position = [rd.randrange(0, 25), rd.randrange(0, 25)]
                if self.apple_position not in self.snake_position:
                    break
            self.snake_position.append(self.snake_position[-1])

        self.snake_position.insert(0, self.coordinate_next_step)
        self.snake_position.pop()
