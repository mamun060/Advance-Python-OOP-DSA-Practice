# Mean value is the average value
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Now calculate the average value of 13 car speed 
# Basically mathmatically =>  list / 13 = result

# But in AI
avg_speed = numpy.mean(speed)
print(avg_speed)