import plotly.graph_objects as go 
import numpy as np 
import plotly

plotly.offline.init_notebook_mode()

def plot(network, z, t, type_plot, num_test_samples=1000):
  print('NOTE: The x axis represents the z value, the y axis, the t value and finally the z axis the predicted value of flow/radii.')
  z_flat = np.linspace(z[0], z[1], num_test_samples)
  t_flat = np.linspace(t[0], t[1], num_test_samples)
  u = network.predict([x_flat, t_flat], batch_size=num_test_samples)
  fig = go.Figure(data=[go.Surface(x=z_flat, y=t_flat, z=u)])
  print('NOTE: The x-axis represents the location along the artery,\n the y-axis, the time of evaluation and the z-axis the \n predicted value of {}'.format(type_plot)) 
  fig.update_layout(title='Plot of {}'.format(type_plot))
  fig.show() 
