import tensorflow as tf

print("\n\n\n")

print(tf.__version__)


print("\n\n\n")


variable1 = tf.Variable(22,tf.int16)
tf.print(variable1)          # this will print the value of the variable
tf.print(variable1.numpy())  # this will print the value of the variable as a numpy array
print(tf.rank(variable1))         # this will print the rank of the variable
print(tf.shape(variable1) )         # this will print the shape of the variable

print("\n\n\n")

variable2 = tf.Variable([1,2,3,4],tf.int16)
tf.print(variable2)
tf.print(variable2.numpy())
print(tf.rank(variable2))
print(tf.shape(variable2))

print("\n\n\n")

variable3 = tf.Variable([["hei","hello","hola"],
                         ["hei","hello","hola"]],tf.string)
tf.print(variable3)
tf.print(variable3.numpy())
print(tf.rank(variable3))
print(tf.shape(variable3))


# when you say, tf.Variable(22,tf.int16), you're creating a scalar tensor
# when you say, tf.Variable([1,2,3,4],tf.int16), you're creating a vector tensor
# when you say, tf.Variable([["hei","hello","hola"],["hei","hello","hola"]],tf.string), you're creating a matrix tensor

# these tensors are mutable, i.e., you can change the values of these tensors
# these tensors are also called "variables" in tensorflow
# right now, we're just creating variables and hardcoding values
# but in reality, you'd be using these variables to store the weights and biases of a neural network
# and you'd be updating these variables using the backpropagation algorithm
# and you'd be using these variables to make predictions
# and you'd be using these variables to calculate the loss
# and you'd be using these variables to calculate the gradients

