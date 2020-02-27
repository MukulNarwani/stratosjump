import pandas as pd
import math
import json
from scipy import constants
import matplotlib.pyplot as plt
radius = 0.5
mass = 70


data = pd.read_excel("C:\\Users\\narwa\\Downloads\\Book.xlsx")

#print(data['Altitude'][18])
'''file = open("C:\\Users\\narwa\\Downloads\\cartodb-query.geojson","r")
text = file.read()
print (text)
file.close()


#TODO: code equations viscosity density figure deltat out
C=math.pi() * density * (radius^2) * (velocity^2)/4;

B= 3* math.pi()* viscosity*2*radius*velocity

q = -(B^2) -4*(-mass*g)*C
mass = 70
deltat = 5
g = 10
def v(t):
	brac = math.tanh(  (sqrt(-q)/(2*mass))  * (deltat))
	return (sqrt(-q)/(2*C))*(brac - (b/sqrt(-q)))


for 


def y(t):
	numerator = math.cosh((deltat)*sqrt(-q)/(2*mass))
	denominator = math.cosh(deltat*sqrt(-q)/(2*mass))
	brac = numerator/denominator
	return (mass/C)*math.log(brac) - B*t/(2*C)

'''


def getgravity(y):
	h = y + 6378100
	g = constants.G	*(5.972 * 10**24)/(h**2)
	return 9.81


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

#'''


'''def getviscosity(y):
return
'''

def y(t):
	deltat = 1;
	vknot = 0;
	yknot = 38969;
	for i in range(0,int(t/deltat)):
		v = vknot + (getgravity(yknot) - ((3.14*getdensity(yknot)*(radius**2)*(vknot**2)*0.5)/mass)*deltat)
		y = yknot -((v+vknot)*deltat/2)
		vknot = v
		yknot = y
	return yknot	


time = range(0,250)
position = [y(i) for i in time]
plt.plot(time,position)
plt.show()