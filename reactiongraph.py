from matplotlib import pyplot as plt
import numpy as np

def linear_plt(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals)

reaction_data = [
    (0.12E-3, 8.49E-6),
    (0.96E-3, 7.10E-6),
    (2.24E-3, 5.79E-6),
    (3.20E-3, 5.20E-6),
    (4.00E-3, 4.77E-6),
]

# Do an exponential regression on the data
# Approximate the rate with an average rate over a very small interval

fig = plt.figure()
# Plot reaction data
plt.plot(*zip(*reaction_data), "-o")
# Plot line from first to last
first_and_last = [reaction_data[0], reaction_data[-1]]
# Calculate the tangent line

plt.plot(*zip(*first_and_last))
fig.suptitle("Reaction Data")
plt.xlabel("Time (s)")
plt.ylabel("[ClO] (mol/L)")
plt.grid()
plt.show()