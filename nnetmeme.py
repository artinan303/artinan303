import numpy as np
import matplotlib.pyplot as plt

# create array with our six inputs
inputs = np.array([[1, 0, 0],
                   [1, 0, 1],
                   [1, 1, 1],
                   [0, 1, 0],
                   [0, 0, 1],
                   [0, 1, 1]])

# create array with our six corresponding outputs
outputs = np.array([[1], [1], [1], [0], [0], [0]])


# create NN class
class NeuralNet:

    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
        self.weights = np.array([[.50], [.50], [.50]])
        self.lossHistory = []  # for graph
        self.epochList = []  # for graph

    # use sigmoid function
    def sigmoid(self, x, deriv=False):
        if deriv:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

    def feedforeward(self):
        self.hidden = self.sigmoid(np.dot(self.inputs, self.weights))

    def backpropogation(self):
        self.error = self.outputs - self.hidden
        delta = self.error * self.sigmoid(self.hidden, deriv=True)
        self.weights += np.dot(self.inputs.T, delta)

    def train(self, epochs=5000):
        for epoch in range(epochs):
            self.feedforeward()
            self.backpropogation()

            self.lossHistory.append(np.average(np.abs(self.error)))
            self.epochList.append(epoch)

    def predict(self, newInput):
        prediction = self.sigmoid(np.dot(newInput, self.weights))
        return prediction


NN = NeuralNet(inputs, outputs)
NN.train()

example = np.array([[0, 1, 1]])
example2 = np.array([[1, 1, 0]])

print(NN.predict(example), " - Correct: ", example[0][0])
print(NN.predict(example2), " - Correct: ", example2[0][0])

plt.figure(figsize=(15,5))
plt.plot(NN.epochList, NN.lossHistory)
plt.xlabel("Epoch")
plt.ylabel("loss")
plt.show()
