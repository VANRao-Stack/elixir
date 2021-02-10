import tensorflow as tf

class Network:
    """
    Build a Neural Network that will be used to simulate a differential equation
    """

    @classmethod
    def build(cls, num_inputs=1, layers=[20, 20, 20, 20, 20, 20, 20, 20],
              activation='tanh', num_outputs=1):
        """
        Build a NN model for the differential equation.
        Args:
            num_inputs: number of input variables. Default is 1 for (x).
            layers: number of hidden layers.
            activation: activation function in hidden layers.
            num_outpus: number of output variables. Default is 1 for u(x).
        Returns:
            keras network model.
        """

        # input layer
        inputs = tf.keras.layers.Input(shape=(num_inputs,))
        # hidden layers
        x = inputs
        for layer in layers:
          # I have chosen to go with he_normal initialization here after a little experimentation,
          # although I do suggest we stich with glorot for the final rpoduct
          x = tf.keras.layers.Dense(layer, activation=activation, kernel_initializer='he_normal')(x)
        # output layer
        outputs = tf.keras.layers.Dense(num_outputs,
            kernel_initializer='he_normal')(x)

        return tf.keras.models.Model(inputs=inputs, outputs=outputs)
