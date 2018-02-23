from math import pi,pow

def coeff_sawtooth(n):
    return pow(-1, n+1)*(2/pi)*(1/n)

def coeff_triangle(n):
    return pow(-1,n)*1/((2*n+1)**2)*(8/(pi**2))

def coeff_square(n):
    return (4/pi)*(1/(2*n+1))
