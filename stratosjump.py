import pandas as pd
import math
import json
from scipy import constants
import matplotlib.pyplot as plt

radius = 0.4
mass = 70

data = pd.read_csv("pep.csv")

print(data['Velocity Time (s)'].values.tolist())
def getgravity(y):
	h = y + 6378100
	g = constants.G	*(5.972 * 10**24)/(h**2)
	return g


def getdensity(y):
	if(y>=25000):
		T = (0.00299*y)-131.21
		p = 2.488*((T+273.1)/216.6)**(-11.388)
	elif(11000<=y<25000):
		T = -56.46
		p = 22.65*math.exp(1.73-0.000157*y)
	elif(y<11000):
		T = 15.04 - 0.00649 * y 
		p =  101.29 *((T+273.1)/288.08)**5.256
	density = p/(0.2869*(T+273.1))

	return density

def y(t):
	deltat = 1;
	vknot = 0;
	yknot = 38969;
	for i in range(0,int(t/deltat)):
		v = vknot + (getgravity(yknot) - ((math.pi*getdensity(yknot)*(radius**2)*(vknot**2)*0.5)/mass)*deltat)
		#Trapezoidal rule to estimate integral 
		y = yknot -((v+vknot)*deltat/2)
		vknot = v
		yknot = y
	return yknot	


time = range(0,250)
position = [y(i) for i in time]
plt.plot(time,position)


#COMMENT EITHER ONE OF THESE OUT 
plt.plot(data['Alt Time (s)'],data['Altitude (m)'])
#plt.plot(data['Velocity Time (s)'],data['Velocity (m/s)'])



plt.show()

