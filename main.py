print('quadratic equation should be in form +-ax^2 +-bx + c')

from math import sqrt
import cmath

def quadratic(a, b, c):
    x = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    y = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
    return(x,y)


try:
    a = int(input('enter the cofficient of X^2: '))
    b = int(input('enter the cofficient of x:  '))
    c = int(input('enter the constant of the equation '))
    print(quadratic(a, b, c)) 

except Exception:
    print('invalid syntax')

    