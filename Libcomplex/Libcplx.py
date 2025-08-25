import math

def sum(a, b):
    real = a[0] + b[0]
    imag = a[1] + b[1]
    return (real, imag)

def mul(a, b):
    real = (a[0] * b[0] - a[1] * b[1])
    imag = (a[0] * b[1] + a[1] * b[0])
    return (real, imag)

def rest(a, b):
    real = a[0] - b[0]
    imag = a[1] - b[1]
    return (real, imag)

def div(a, b):
    denom = b[0]**2 + b[1]**2
    real = (a[0]*b[0] + a[1]*b[1]) / denom
    imag = (a[1]*b[0] - a[0]*b[1]) / denom
    return (real, imag)

def conj(a):
    real = a[0]
    imag = -a[1]
    return (real, imag)

def mod(a):
    mod = math.sqrt(a[0]**2 + a[1]**2)
    return mod

def cart_polar(z):
    a = z[0]
    b = z[1]
    r = math.sqrt(a**2 + b**2)
    theta = math.atan2(b, a)
    return (r, theta)

def polar_cart(p):
    r = p[0]
    theta = p[1]
    a = r * math.cos(theta)
    b = r * math.sin(theta)
    return (a, b)

def phase(z):
    a = z[0]
    b = z[1]
    return math.atan2(b, a)

if __name__ == '__main__':
    print(sum((3,4), (-2.5,4)))



