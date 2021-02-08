# suppress tensorflow warnings (must be called before importing tensorflow)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
import numpy as np
import tensorflow_probability as tfp

tf.keras.backend.set_floatx("float64")

class tfp_Trainer(object):
    def __init__(self, model, x_train, y_train, first_order_trainer='rmsprop', batch_size=128, 
                 first_order_epochs=10, maxiter=100):
        self.model = model
        self.x_train = x_train
        self.y_train = y_train
        self.first_order_trainer = first_order_trainer
        self.batch_size = batch_size
        self.first_order_epochs = first_order_epochs
        self.bfgs_iter = maxiter
        self.iter = tf.Variable(0)
        self.loss = tf.keras.losses.MeanSquaredError()
        self.shapes = tf.shape_n(self.model.trainable_variables)
        self.n_tensors = len(self.shapes)

        # we'll use tf.dynamic_stitch and tf.dynamic_partition later, so we need to
        # prepare required information first
        self.count = 0
        self.idx = [] # stitch indices
        self.part = [] # partition indices

        for i, shape in enumerate(self.shapes):
            n = np.product(shape)
            self.idx.append(tf.reshape(tf.range(self.count, self.count+n, dtype=tf.int32), shape))
            self.part.extend([i]*n)
            self.count += n

        self.part = tf.constant(self.part)
        
        self.init_params = tf.dynamic_stitch(self.idx, self.model.trainable_variables)
        
    def set_weights(self, params_1d):
        params = tf.dynamic_partition(params_1d, self.part, self.n_tensors)
        for i, (shape, param) in enumerate(zip(self.shapes, params)):
            self.model.trainable_variables[i].assign(tf.reshape(param, shape))
    
    def tf_evaluate(self, x, y):
        with tf.GradientTape() as g:
            loss = self.loss(self.model(x, training=True), y)
        grads = g.gradient(loss, self.model.trainable_variables)
        return loss, grads

    def grad_and_loss_func(self, weights):
        self.set_weights(weights)
        loss, grads = self.tf_evaluate(self.x_train, self.y_train)
        grads = tf.dynamic_stitch(self.idx, grads)

        self.iter.assign_add(1)
        tf.print("Iterations:", self.iter, "Loss Value:", loss)
  
        return loss, grads

    def train(self, use_second_order=False):
        self.model.compile(optimizer=self.first_order_trainer, loss='mse')
        print('Running First order optimizer: \n')
        self.model.fit(x=self.x_train, y=self.y_train, batch_size=self.batch_size, epochs=self.first_order_epochs)
        if use_second_order:
            print('\nRunning L-BFGS Optimizer: \n')
            results = tfp.optimizer.lbfgs_minimize(value_and_gradients_function=self.grad_and_loss_func, 
                                                   initial_position=self.init_params, max_iterations=self.bfgs_iter)
            self.set_weights(results.position)


def set_weights(trainer, model, params_1d):
    params = tf.dynamic_partition(params_1d, trainer.part, trainer.n_tensors)
    for i, (shape, param) in enumerate(zip(trainer.shapes, params)):
        model.trainable_variables[i].assign(tf.reshape(param, shape))
