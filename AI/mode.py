#Use the SciPy mode() method to find the number that appears the most:
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
result = stats.mode(speed)
print(result)