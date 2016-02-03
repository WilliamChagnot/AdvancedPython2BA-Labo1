# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016

def fact(n):
    m=1
    r=0
    if n == 0:
        r=1
    else:
        while m <= n:
            r *= m
            m += 1
    return r

def roots(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        result=()
    elif delta == 0:
        r=-b/(2*a)
        result=(r)
    else:
        r1=(-b-delta**(1/2))/(2*a)
        r2=(-b+delta**(1/2))/(2*a)
        result=(r1,r2)

def integrate(function, lower, upper):
    steps = 100
    h=(upper - lower)/steps
    x=lower

    integral=0
    i=0

    while i < steps:
        if i == 0 or i == steps:
            integral += eval(function, {}, {'x':x})
        elif i%2 == 0:
            integral += 2*eval(function, {}, {'x':x})
        else:
            integral += 4*eval(function, {}, {'x':x})

        x += h

    integral *= h/3

    return integral

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))
