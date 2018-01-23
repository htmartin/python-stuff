import numpy as np 

my_house = [18.0, 20.0, 10.75, 9.50]
np.array(my_house)
your_house = [14.0, 24.0, 14.25, 9.0]
np.array(your_house)

height = [1.73, 1.68, 1.71, 1.89, 1.79] 
weight = [65.4, 59.2, 63.6, 88.4, 68.7] 
numpy_height=np.array(height)
numpy_weight=np.array(weight)

bmi=numpy_weight/numpy_height**2

To subset both regular Python lists and numpy arrays, you can use square brackets:

x = [4 , 9 , 6, 3, 1]
x[1]
import numpy as np
y = np.array(x)
y[1]
For numpy specifically, you can also use boolean numpy arrays:

high = y > 5
y[high]


# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array

light = bmi > 5
bmi[light]
# Print out light


# Print out BMIs of all baseball players whose BMI is below 21
bmi>21