#Simpson's rule application
import math

startVal = 4.0
totalValue = 0.0
for x in range(7):
	if((startVal%1.0) == 0.5):
		val = startVal
		val = val ** (-0.5)
		val = (val/2.0)
		val = (val + 1.0) ** 2.0
		val = val + 1.0
		print(4 * math.sqrt(val))
		totalValue = totalValue + val
		startVal = startVal + 0.5
	elif (startVal == 4.0 or startVal == 7.0):
		val = startVal
		val = val ** (-0.5)
		val = (val/2.0)
		val = (val + 1.0) ** 2.0
		val = val + 1.0
		print(math.sqrt(val))
		totalValue = totalValue + val
		startVal = startVal + 0.5
	else: 
		val = startVal
		val = val ** (-0.5)
		val = (val/2.0)
		val = (val + 1.0) ** 2.0
		val = val + 1.0
		print(2 * math.sqrt(val))
		totalValue = totalValue + val
		startVal = startVal + 0.5

print(totalValue)

'''
def simpsonsRule(botBound, topBound, funct, n):
	changeX = (topBound - botBound) / n
	constant = changeX / 3
	tempVal = botBound
	for x in range(n):
'''



