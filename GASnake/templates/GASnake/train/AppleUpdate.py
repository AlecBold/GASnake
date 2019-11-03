# --------------------------------------------APPLE UPDATE-------------------------------------------

# Importing libraries
import random as rd

class AppleUpdate:
    def __init__(self):
        self.all_apple = []

    def check_apple(self, snake):
        try:
            index_a = snake.sum_apple
            snake.apple_position = self.all_apple[index_a][:]
        except:
            self.all_apple.append([rd.randrange(0, 25), rd.randrange(0, 25)])
            snake.apple_position = self.all_apple[index_a][:]

        return snake
