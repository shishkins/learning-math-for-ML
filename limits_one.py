import numpy as np
from math import factorial
import plotly.graph_objects as go
'''TASK 1'''
def func_one(x):
    return (1**x)/x

example_one = np.arange(1,100)
# print(func_one(example_one))

example_one_fig = go.Figure()
example_one_fig.add_trace(go.Scatter(x = example_one,
                                     y = func_one(example_one)))

# example_one_fig.show()  #предел = 0
''' TASK 2'''
def func_two(x):
    return (x)/(x**2 + 1)

example_two = np.arange(1,1000)
# print(func_two(example_two))

example_two_fig = go.Figure()
example_two_fig.add_trace(go.Scatter(x = example_two,
                                     y = func_two(example_two)))
# example_two_fig.show()  # предел = 0


''' TASK 3'''
example_three = np.arange(1,100)
# print(func_two(example_three))
y_factorial = []
for x in example_three:
    y_factorial.append(factorial(x))
y_factorial = np.array(y_factorial)

example_three = np.apply_along_axis(lambda x: x**3,
                                    0,
                                    example_three)
example_three_y = example_three/y_factorial

example_three_fig = go.Figure()
example_three_fig.add_trace(go.Scatter(x = example_three,
                                     y = example_three_y))
# example_three_fig.show()  # предел = 0

''' TASK 4'''
def example_four_next(x):
    return 0.5*(x + 5/x)

init_x = [1]
n = 100
for i in range(1,n):
    init_x.append(example_four_next(init_x[i-1]))

example_four = np.arange(1,n)

example_four_fig = go.Figure()
example_four_fig.add_trace(go.Scatter(x = example_four,
                                     y = init_x))
example_four_fig.show()  # предел = 2.23

