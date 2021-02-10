from .cantorProject.network import Network
from .cantorProject.tfp_trainer import tfp_Trainer, set_weights
from .cantorProject.sci_trainer import sci_Trainer
from .utils import plot
import tensorflow as tf
import numpy as np
import math
from tensorflow.keras.layers import Lambda



class GradientLayer(tf.keras.layers.Layer):
    """
    Subclassed layer to compute general derivatives
    """
    def __init__(self, R_model,q_model, **kwargs):
        """
        Args:
            R_model: keras network model to simulate R
            q_model: keras network model to simulate q
        """
        self.R_model = R_model
        self.q_model = q_model
        super().__init__(**kwargs)

    def call(self, tx):
        """
        Computing 1st and 2nd derivatives of the neural net.
        Args:
            tx: (z,t)
        Returns:
            u: network output.
            du_dx: 1st derivative of x.
            d2u_dx2: 2nd derivative of x.
        Computing the first derivatives of the two neural networks
        Args:
          tx: (z,t)
        Returns:
          A : Area as computed from the output of R_model
          q : Output of q_model
          R : Output of R_model 
          dA_dt : First derivative of A w.r.t t
          dq_dt : First derivative of q w.r.t t
          dq_dz : First derivatice of q w.r.t z
        """
        #print(tx)
        #tx = tf.keras.layers.Concatenate(inputs)
        #z=inputs[0]
        #t=inputs[1]
        with tf.GradientTape() as g1:
            g1.watch(tx)
            R = self.R_model(tx)
            A = np.pi * (R**2)
        dA_dtx = g1.batch_jacobian(A,tx)
        dA_dt = dA_dtx[...,1]

        with tf.GradientTape() as g2:
            g2.watch(tx)
            q = self.q_model(tx)
        dq_dtx = g2.batch_jacobian(q,tx)
        dq_dz = dq_dtx[...,0]
        dq_dt = dq_dtx[...,1]

        return A,q,R,dA_dt,dq_dt,dq_dz
          
          
class PINN:
  def __init__(self,R_network,q_network):
    """
    Args : 
      R_network : Keras network model to compute R
      q_network : Keras network model to compute q
    """
    self.R_network = R_network
    self.q_network = q_network
    self.grad = GradientLayer(self.R_network,self.q_network)

  def build(self,delta_b,E,h,elasticity_func,R1,R2,CT,Ru,Rd,L,Reynolds_no,q_0):
    """
    Builds the actual model
    Args:
      
      
    """
    z=tf.keras.layers.Input(shape=(1,))
    t=tf.keras.layers.Input(shape=(1,))
    #print("PINN")
    #print(Ru)
    #print(Rd)
    concat_layer = tf.keras.layers.Concatenate()([z,t])
    A,q,R,dA_dt,dq_dt,dq_dz=self.grad(concat_layer)
    A_0,dl_dz = find_derivatives_l(self.R_network,self.q_network,Ru,Rd,L)((z,t)) 
    
    """
      We divide the partial differential equation into two parts, p1 and p2
      p1 -> du/dt + dq/dt = 0
      p2 -> dq/dz + dl/dt = S1
    """
    p1 = (dA_dt + dq_dz)**2

    r0_grad= find_derivatives_r0(self.R_network,Ru,Rd,L)
    dr0_dz,r0 = r0_grad(z)

    df_dr0 = find_derivatives_f0()(r0)

    t1 = Lambda(lambda ar: -(2*math.pi*ar[0]*ar[1])/(delta_b*Reynolds_no*ar[2]))((R,q,A))
    
    #print(df_dr0)
    #print("T2")
    #t2 = Lambda(lambda ar: math.sqrt(math.pi) * elasticity_func(relaxed_radius_func(ar[0],ar[3],int(ar[4]),int(ar[5]))) + tf.math.sqrt(ar[1]) * ar[2])((z,A_0,df_dr0,float(Ru),Rd,L))
    t2 = t2_class(Ru,Rd,L)((z,A_0,df_dr0))
    S1 = Lambda(lambda ar: ar[3] + (2*tf.math.sqrt(ar[0])*(ar[4])-ar[0]*ar[1])*ar[2])((A,df_dr0,dr0_dz,t1,t2))
    p2 = Lambda(lambda ar: tf.math.pow(ar[0] + ar[1] - ar[2],2))((dq_dt,dl_dz,S1))
    u_eqn = p1 + p2

    #For the inflow condition
    z_inflow = tf.keras.layers.Input(shape=(1,))
    t_inflow = tf.keras.layers.Input(shape = (1,))
    concat_inflow = tf.keras.layers.Concatenate()([z_inflow,t_inflow])
    q_bndry_inflow = self.q_network(concat_inflow)

    
    #For the outflow condition
    z_outflow = tf.keras.layers.Input(shape=(1,))
    t_outflow = tf.keras.layers.Input(shape = (1,))
    p_obj = p_class(self.R_network,self.q_network,Ru,Rd,L,E,h)
    dp_bo_dt,p,dq_bo_dt,q_bo = p_obj((z_outflow,t_outflow))
    u_bndry_outflow = dp_bo_dt - (R1 * dq_bo_dt - (p/(R2*CT)) + q_bo*(R1+R2)/(R2*CT) )

    
    #print(S1)
    #print(dq_dt)
    #print(dl_dz)
    #print(p2)
    return tf.keras.models.Model(
        inputs = [z,t,z_inflow,t_inflow,z_outflow,t_outflow],
        outputs = [u_eqn,q_bndry_inflow,u_bndry_outflow]
    )    
    
 
class t2_class(tf.keras.layers.Layer):
  def __init__(self,Ru,Rd,L,**kwargs):
    super().__init__(self,**kwargs)
    self.Ru = Ru
    self.Rd = Rd
    self.L = L
  def call(self,input):
    z = input[0]
    A_0 = input[1]
    df_dr0 = input[2]
    return math.sqrt(math.pi) * elasticity_func(relaxed_radius_func(z,self.Ru,self.Rd,self.L)) + tf.math.sqrt(A_0) * df_dr0



class find_derivatives_l(tf.keras.layers.Layer):
  """
  Keras layers subclass to compute the derivative of l w.r.t z
  """
  def __init__(self,R_network,q_network,Ru,Rd,L,**kwargs):
    super().__init__(self,**kwargs)
    #print("L")
    self.Ru = Ru
    self.Rd = Rd
    self.L = L
    self.grads = GradientLayer(R_network,q_network)
  def call(self,input):
    """
    Computes relaxed radius area and dl_dz
    Returns:
      A_0 : Relaxed radius area computed from pi*square(relaxed_radius)
      dl_dz: The derivative of l w.r.t z
    """
    z = input[0]
    t = input[1]
    #concat = tf.keras.layers.Concatenate()([z,t])
    #print(z)
    with tf.GradientTape() as g3:
      g3.watch(z)
      concat = tf.keras.layers.Concatenate()([z,t])
      A,q,_,_,_,_ = self.grads(concat)
      #print(tx[0])
      r0 = relaxed_radius_func(z,self.Ru,self.Rd,self.L)
      A_0 = math.pi * (r0**2)
      l=(q**2)/A + elasticity_func(r0)*tf.sqrt(A_0*A)
    dl_dtx = g3.batch_jacobian(l,z)
    dl_dz = dl_dtx[...,0]
    return A_0,dl_dz



class p_class(tf.keras.layers.Layer):
  """
    Keras layers to compute the pressure, and related values
  """
  def __init__(self,R_model,q_model,Ru,Rd,L,E,h,**kwargs):
    """
      Args:
        R_model : Keras network model simulating R
        q_model : Keras network model simulating q
      """
    super().__init__(self,**kwargs)
    self.R_model = R_model
    self.q_model = q_model
    self.Ru = Ru
    self.Rd = Rd
    self.L = L
    self.E = E
    self.h = h
    self.grad = GradientLayer(self.R_model,self.q_model)
  
  def call(self,input):
    """
      Calculated the pressure, its derivative and related values
      Returns:
        dq_bo_dt : Derivative of q w.r.t t for the outflow boundary condition
        p : Pressure calculated at the outflow boundary condition
        dp_bo_dt : Derivative of p w.r.t t for the outflow boundary condition
        q_bo : q calculated at the outflow boundary condition
    """
    #print("P")
    #print(type(self.Ru))
    #print(type(self.Rd))
    z_outflow = input[0]
    t_outflow = input[1]
    concat_layer = tf.keras.layers.Concatenate()([z_outflow,t_outflow])
    with tf.GradientTape() as g:
      #L,A_bndry_outfow,q_bndry_outflow,_,_,dq_bo_dt,_,_=self.grads(tx_bndry_outflow,elasticity_func)
      g.watch(concat_layer)
      A_bo,q_bo,R_bo,_,dq_bo_dt,_ = self.grad(concat_layer)

      #A_bo_0 = Lambda(lambda x: math.pi * (relaxed_radius_func(x[0],int(x[1]),int(x[2]),int(x[3]))**2))((z_outflow,self.Ru,self.Rd,self.L))
      A_bo_0 = math.pi * (relaxed_radius_func(z_outflow,self.Ru,self.Rd,self.L) ** 2)
      p = (4/3)*((self.E*self.h)/relaxed_radius_func(z_outflow,self.Ru,self.Rd,self.L)) * (1 - tf.sqrt(A_bo_0/A_bo))
      #p=1
    dp_dtx_bo = g.batch_jacobian(p,concat_layer)
    dp_bo_dt = dp_dtx_bo[...,1]
    return dp_bo_dt,p,dq_bo_dt,q_bo

    

class find_derivatives_r0(tf.keras.layers.Layer):
  def __init__(self,R_network,Ru,Rd,L,**kwargs):
    super().__init__(self,**kwargs)
    self.R_network = R_network
    self.Ru = Ru
    self.Rd = Rd
    self.L = L
  def call(self,z):
    with tf.GradientTape() as g:
      g.watch(z)
      r0 = relaxed_radius_func(z,self.Ru,self.Rd,self.L)
    dr0_dx = g.batch_jacobian(r0,z)[...,0]
    return dr0_dx,r0



class find_derivatives_f0(tf.keras.layers.Layer):
  def __init__(self,**kwargs):
    super().__init__(self,**kwargs)

  def call(self,input):
    with tf.GradientTape() as g:
      f0 = elasticity_func(input)
      #print(f0)
    df0_dr0 = g.batch_jacobian(f0,input)[...,0]
    return df0_dr0
    
    
class artery:
    def __init__(self, delta_b=2*math.pow(10,-3), Ru=0.37, Rd=0.37, L=20.8, Reynolds_no=4500, E=4.8, h=0.065, q_0=450,
                 length_domain=(0, 20.8), time_domain = (0,0.8), tow=.3, timeperiod=0.8, 
                 layers=[50] * 9, activation='tanh', num_train_samples=100000):
        self.delta_b = delta_b
        self.Ru = Ru
        self.Rd = Rd
        self.L = L
        self.length_domain = (0,L)
        self.time_domain = (0,timeperiod)
        self.tow = tow
        self.q_0 = q_0
        self.timeperiod = timeperiod
        self.layers = layers
        #self.bnd_cond = bnd_cond
        self.activation = activation
        self.num_train_samples = num_train_samples
        
        self.R_network = Network.build(num_inputs = 2,layers=self.layers, activation=self.activation)
        self.q_network = Network.build(num_inputs = 2,layers = self.layers, activation = self.activation)
        self.pinn = PINN(self.R_network, self.q_network).build(self.delta_b, E, h, elasticity_func, 253/100, 139/100, 1.3384, Ru, Rd, L, Reynolds_no, q_0)
        self.pinn.summary()
        
    def create_dataset(self):
        z = np.random.rand(self.num_train_samples, 1)*self.length_domain[1]
        t = np.random.rand(self.num_train_samples,1)*self.time_domain[1]
        z_inflow = np.zeros((self.num_train_samples,1))
        t_inflow = np.random.rand(self.num_train_samples,1)*self.time_domain[1]
        z_outflow = np.ones((self.num_train_samples, 1))*self.length_domain[1]
        t_outflow = np.random.rand(self.num_train_samples,1)*self.time_domain[1]
        #print(t_outflow)

        x_train = [z,t,z_inflow,t_inflow,z_outflow,t_outflow]
        #print(x_train.shape)
        
            
        u_zero = np.zeros((self.num_train_samples, 1))
        q_bndry_inflow = initial_q(t_outflow, self.timeperiod, self.tow,self.q_0)
        #print(type(q_bndry_inflow))
        #print(q_bndry_inflow.shape)
        #q_bndry_inflow = np.zeros((self.num_train_samples,1))
        u_bndry_outflow = np.zeros((self.num_train_samples,1))
        y_train = [u_zero,q_bndry_inflow,u_bndry_outflow]
        
        return x_train, y_train
    
    def sci_train(self, first_order_trainer='rmsprop',  batch_size=128, first_order_epochs=10, 
                  factr=10, m=50, maxls=50, maxiter=15000):
        x_train, y_train = self.create_dataset()
        trainer = sci_Trainer(self.pinn, x_train, y_train, first_order_trainer=first_order_trainer, batch_size=batch_size, 
                                 first_order_epochs=first_order_epochs, factr=factr, m=m, maxls=maxls, maxiter=maxiter)
        trainer.train()
        return self.R_network, self.q_network
    
    def tfp_trainer(self, first_order_trainer='rmsprop', batch_size=128, first_order_epochs=10,
                 factr=10, m=50, maxls=50, maxiter=15000):
        x_train, y_train = self.create_dataset()
        tfp_trainer = tfp_Trainer(self.pinn, x_train, y_train, first_order_trainer=first_order_trainer, batch_size=batch_size, 
                                     first_order_epochs=first_order_epochs, maxiter=maxiter)
        result = tfp_trainer.train()
        set_weights(tfp_trainer, self.pinn, result.position)
        return self.networking
    
    def plot_flow(self, num_test_samples=100):
        plot(self.R_network, (0, self.L), self.time_domain, 'flow', num_test_samples)
        
    def plot_radius(self, num_test_samples=100):
        plot(self.q_network, (0, self.L), self.time_domain, 'radii', num_test_samples)    
        
        

def initial_q(t,timeperiod,tow,q_0): 
  t=np.fmod(t,timeperiod)
  #print(t)
  t1 = np.exp(-np.power(t,2) / (2*(tow**2)))
  #print(t1)
  return ((q_0*t)/( (tow**2) * t1))/1000000

def relaxed_radius_func(z, Ru, Rd, L):
  #print(z)
  #print("Relrad")
  #print(type(Rd))
  #print(type(Ru))
  Ru = float(Ru)
  temp = tf.cast(tf.math.log(Rd/Ru),tf.float64,name=None)
  #print(temp)
  #print(type(temp))
  return Ru*tf.exp(temp*(z/L))

def elasticity_func(r0):
  return 2/3*r0
