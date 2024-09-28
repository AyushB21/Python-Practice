import numpy
speed=[99,86,87,88,111,86,103,87]
x=numpy.mean(speed)
y=numpy.median(speed)

z=numpy.std(speed)  #Standard Deviation
v=numpy.var(speed)  #Variance

print(x,y,z,v,sep='\n')
