import deepxde as dde
import numpy as np
import matplotlib.pyplot as plt
from deepxde.backend import tf

# Define the geometry
geom = dde.geometry.Rectangle(xmin=[0, 0], xmax=[1, 1])

# Define the PDE
def pde(x, u):
    du_xx = dde.grad.hessian(u, x, i=0, j=0)
    du_yy = dde.grad.hessian(u, x, i=1, j=1)
    # Using TensorFlow operations for the source term
    source_term = dde.backend.sin(np.pi * x[:, 0:1]) * dde.backend.sin(np.pi * x[:, 1:2])
    return du_xx + du_yy + source_term

# Define the boundary conditions
def boundary(x, on_boundary):
    return on_boundary

bc = dde.icbc.DirichletBC(geom, lambda x: 0, boundary)

# Define the data object
data = dde.data.PDE(
    geom,
    pde,
    bc,
    num_domain=4000,
    num_boundary=400,
    num_test=1000
)

# Define the neural network
layer_size = [2] + [32]*3 + [1]

activation = 'tanh'
initializer =  'Glorot uniform'
layers = []
for i, size in enumerate(layer_size):
  layers.append(Dense(size, activation=activation, kernel_initializer=initializer))

network = dde.maps.Sequential(layers)
model = dde.Model(data, network)
model.compile('adam', lr=0.0001)
losshistory, train_state = model.train(iterations=10000, display_every=1000)

# Predict the solution and plot it
x_data = np.linspace(0, 1, 2000)
t_data = np.linspace(0, 1, 2000)
test_x, test_t = np.meshgrid(x_data, t_data)
test_domain = np.vstack([test_x.ravel(), test_t.ravel()]).T
predicted_solution = model.predict(test_domain)
residual = model.predict(test_domain, operator=pde)
predicted_solution = predicted_solution.reshape(test_x.shape)
plt.contourf(test_x, test_t, predicted_solution)
plt.show()

