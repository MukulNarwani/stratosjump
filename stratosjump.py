import Math
import json


file = open("C:\\Users\\narwa\\Downloads\\cartodb-query.geojson","r")
text = file.read()
print (text)
file.close()

#TODO: code equations c(y),b(y),y(t),q and v(t), figure out a way to import data.
C=Math.pi() * density * (radius^2) * (velocity^2)/4;

B= 3* Math.pi()* viscosity*2*radius*velocity

q = -(B^2) -4*(-mass*g)*C


def v(t):
	brac = Math.tanh(  (sqrt(-q)/(2*mass))  * (t-tstar))
	return (sqrt(-q)/(2*C))*(brac - (b/sqrt(-q)))

def y(t):
	numerator = Math.cosh((t - tstar)*sqrt(-q)/(2*m))
	denominator = Math.cosh(tstar*sqrt(-q)/(2*m))
	brac = numerator/denominator
	return (mass/C)*Math.log(brac) - B*t/(2*C)

