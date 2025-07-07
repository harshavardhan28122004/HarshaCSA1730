import numpy as np

class FeedForwardNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.bias_hidden = np.random.rand(1, hidden_size)
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.bias_output = np.random.rand(1, output_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def feed_forward(self, x):
        hidden_layer_activation = np.dot(x, self.weights_input_hidden) + self.bias_hidden
        hidden_layer_output = self.sigmoid(hidden_layer_activation)
        output_layer_activation = np.dot(hidden_layer_output, self.weights_hidden_output) + self.bias_output
        output = self.sigmoid(output_layer_activation)
        return output

# Sample input
nn = FeedForwardNN(2, 2, 1)
input_data = np.array([[1, 0]])

# Run feedforward
output = nn.feed_forward(input_data)
print("Output:", output)
