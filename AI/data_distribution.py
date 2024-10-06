# To create big data sets for testing
import numpy
import matplotlib.pyplot as plt

# uniform()
# aktah data sets create korbe jeitar maje 0-5 main value dore 250 data item takhbe
x = numpy.random.uniform(0.0 , 5.0 , 250)

#histogram - show big data sets graphical representation
plt.hist(x, 5)
plt.show

# print(x)

