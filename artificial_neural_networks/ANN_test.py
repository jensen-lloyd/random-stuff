import multiprocessing
import numpy as np

np.random.seed(0)

X = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


class Layer:

    def __init__(self, n_inputs, n_neurons, activation_function):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        self.activation_function = activation_function


    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

        if self.activation_function == 'relu':
            self.output = np.maximum(0.0, self.output)

        elif self.activation_function == 'sigmoid':
            self.output = 1 / (1 + np.exp(-self.output))


    # def backpropagate(self, targets):
    #     error = self.output - targets 

    #     if self.activation_function == 'sigmoid':
    #         network_outputs = self.output * (1 - self.output)

    #     adjustments = error * network_outputs

    #     self.weights = np.dot(self.inputs * adjustments)

        






layer1 = Layer(12,8,'sigmoid')
layer2 = Layer(8,8,'sigmoid')
layer3 = Layer(8,8,'sigmoid')
layer4 = Layer(8,8,'sigmoid')
layer5 = Layer(8,2,'relu')

layer1.forward(X)
layer2.forward(layer1.output)
layer3.forward(layer2.output)
layer4.forward(layer3.output)
layer5.forward(layer4.output)

print(layer5.output)


# layer5.backpropagate(0)



def train():
    pass



print('')