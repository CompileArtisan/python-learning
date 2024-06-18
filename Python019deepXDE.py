import numpy as np
import scipy as sp
from deepxde.backend import tf
import deepxde as dde
import time

import matplotlib.pyplot as plt

def pde(x, y):
    dy_t = dde.grad.jacobian(y, x, j=1)                     ####
    dy_xx = dde.grad.hessian(y, x, j=0)                     ####
    return (dy_t - dy_xx*0.3)                               #### THIS IS THE ONLY PART WE GOTTA CHANGE ACCORDING TO OUR EQUATION
                                                            ####

def func(x):                                                ####
    return np.sin(np.pi * x[:, 0:1]) * np.exp(-x[:, 1:])    ####

geom = dde.geometry.Interval(-1,1)                          ####
timedomain = dde.geometry.TimeDomain(0, 1)                  ####
geomtime = dde.geometry.GeometryXTime(geom, timedomain)

bc = dde.icbc.DirichletBC(geomtime, func, lambda _, on_boundary: on_boundary)
ic = dde.icbc.IC(geomtime, func, lambda _, on_initial: on_initial)

data = dde.data.TimePDE(geomtime, pde, [bc, ic],
                        num_domain=8000,
                        num_boundary=2000,
                        num_initial=3000,
                        solution=func,
                        num_test=1000
                        )

layer_size = [2] + [32]*3 + [1]                             #### ALSO THIS

activation = 'tanh'
initializer = 'Glorot uniform'

net = dde.maps.FNN(layer_size, activation, initializer)
model = dde.Model(data, net)
model.compile('adam', lr=0.0001)

losshistory, train_state = model.train(epochs=10000)

x_data = np.linspace(-1,1, num=100)
t_data = np.linspace(0,1, num=100)
test_x, test_t = np.meshgrid(x_data, t_data)
test_domain = np.vstack([test_x.ravel(), test_t.ravel()]).T
predicted_solution = model.predict(test_domain)
residual = model.predict(test_domain, operator=pde)

predicted_solution = predicted_solution.reshape(test_x.shape)
plt.contourf(test_x, test_t, predicted_solution)
plt.show()

residual = residual.reshape(test_x.shape)
plt.contourf(test_x, test_t, residual)
plt.show()
