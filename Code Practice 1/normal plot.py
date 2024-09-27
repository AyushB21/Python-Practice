import numpy
import matplotlib.pyplot as plt

x=numpy.random.normal(5.0,1.0,100000)   #100000 values with mean as 5 and standard deviation 1
#Meaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.
plt.hist(x,100)
plt.show()
