#!/usr/bin/env python

import matplotlib.pyplot as plt 

year =[1950, 1970, 1990, 2010]

pop = [2.519, 3.692, 5.263, 6.791]

plt.plot(year, pop)

>>> line_graph=plt.plot(year, pop)
>>> line_graph
[<matplotlib.lines.Line2D object at 0x10b495278>]
>>> plt.show(line_graph)


scatter_plot=plt.scatter(year, pop)
plt.show(scatter_plot)


# Print the last item from year and pop

year =[1950, 1970, 1990, 2010]

pop = [2.519, 3.692, 5.263, 6.791]

print(year[-1])
print(pop[-1])

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
line_graph=plt.plot(year,pop)

# Display the plot with plt.show()
plt.show(line_graph)