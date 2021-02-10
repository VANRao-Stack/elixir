import plotly.graph_objects as go 
import numpy as np 
import plotly

plotly.offline.init_notebook_mode()

def plot(network, z, t, plot_type, num_test_samples=1000):
  # Creating dataset 
  x = np.linspace(0, 20.8, 100)
  y = np.linspace(0, 0.8, 100)
  z = []
  for i in range(100):
    temp = []
    for j in range(100):
      temp.append(network.predict(np.asarray([[x[i], y[j]]])))
    z.append(temp) 
  for i in range(len(z)):
    z[i] = np.asarray(z[i])
  z = np.asarray(z)
  z = z.reshape((100, 100))
  fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])
  fig.update_layout(title='Plot of {}'.format(plot_type))
  fig.show() 
