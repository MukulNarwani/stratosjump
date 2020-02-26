import Math
import json


file = open("C:\\Users\\narwa\\Downloads\\cartodb-query.geojson","r")
text = file.read()
print (text)
file.close()

#TODO: code equations viscosity density figure deltat out
C=Math.pi() * density * (radius^2) * (velocity^2)/4;

B= 3* Math.pi()* viscosity*2*radius*velocity
'''
q = -(B^2) -4*(-mass*g)*C
mass = 70
deltat = 5
g = 10
def v(t):
	brac = Math.tanh(  (sqrt(-q)/(2*mass))  * (deltat))
	return (sqrt(-q)/(2*C))*(brac - (b/sqrt(-q)))


for 


def y(t):
	numerator = Math.cosh((deltat)*sqrt(-q)/(2*mass))
	denominator = Math.cosh(deltat*sqrt(-q)/(2*mass))
	brac = numerator/denominator
	return (mass/C)*Math.log(brac) - B*t/(2*C)

'''

def y(t):
	vknot = 0;
	yknot = 0
	for i in range(0,t):
		v = vknot + (gravity - ((Math.pi()*density*(radius^2)*(vknot^4)*0.25)/mass)deltat)
		y = yknot +(v+vknot)*deltat/2
		vknot = v
		yknot = y
	return y