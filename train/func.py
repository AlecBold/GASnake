# -------------------------------------------FUNCTIONS-------------------------------------------

# Importing libraries
import numpy as np

# Initialize random weights
def weights_initialize():
    n_input = 16
    n_hidden1 = 8
    n_hidden2 = 8
    n_output = 4
    w_hidden1 = 2 * np.random.random((n_input, n_hidden1)) - 1
    w_hidden2 = 2 * np.random.random((n_hidden1, n_hidden2)) - 1
    w_output = 2 * np.random.random((n_hidden2, n_output)) - 1
    w_arr = [w_hidden1, w_hidden2, w_output]
    return list(w_arr)


# Sigmoid function
def sigmoid(x, deriv = False):
    if deriv == True:
        return x*(1-x)
    return 1 / (1 + np.exp(-x))


# TanH
def tanH(x, deriv = False):
    if deriv == True:
        return 1 - (2/(1+np.exp(-2*x)) - 1)**2
    else:
        return 2 / (1+np.exp(-2*x)) -1


# Calculate output
def outputData(input_data, weights):
    arr_layers = list([input_data])

    for i in range(len(weights)):
        layer = sigmoid(np.dot(arr_layers[i], weights[i]))
        arr_layers.append(layer)

    return arr_layers[-1]


# Check if snake smash in the wall
def collision_with_wall(head_snake):
    if head_snake[0] < 0 or head_snake[0] > 24 or head_snake[1] < 0 or head_snake[1] > 24:
        return 1
    else:
        return 0


# Check if snake smash in the tail
def collision_with_self(head_snake, snake_position):
    if head_snake in snake_position[1:]:
        return 1
    else:
        return 0


# Check if direction is blocked
def is_direction_blocked(snake_position, coordinate_next_step):
    if collision_with_wall(head_snake=coordinate_next_step) == 1 or collision_with_self(head_snake=coordinate_next_step,
                                                                                        snake_position=snake_position):
        return 1
    else:
        return 0
