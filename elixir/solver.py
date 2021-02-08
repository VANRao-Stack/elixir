from .cantorProject.network import Network
from .cantorProject.tfp_trainer import tfp_Trainer, set_weights
from .cantorProject.sci_trainer import sci_Trainer

class nn_solver(object):
  def __init__(self, head):
    self.head = head
    
  def sci_train(self, artery=None, first_order_trainer='rmsprop',  batch_size=128, first_order_epochs=10, 
                factr=10, m=50, maxls=50, maxiter=15000):

    if artery == None:
      x_train, y_train = self.head.create_dataset()
      trainer = sci_Trainer(self.head.pinn, x_train, y_train, first_order_trainer=first_order_trainer, batch_size=batch_size, 
                                 first_order_epochs=first_order_epochs, factr=factr, m=m, maxls=maxls, maxiter=maxiter)
      trainer.train()
      return self.head.R_network, self.head.q_network

    x_train, y_train = artery.create_dataset()
    trainer = sci_Trainer(artery.pinn, x_train, y_train, first_order_trainer=first_order_trainer, batch_size=batch_size, 
                                 first_order_epochs=first_order_epochs, factr=factr, m=m, maxls=maxls, maxiter=maxiter)
    trainer.train()
    return artery.R_network, artery.q_network
