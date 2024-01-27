import math

def Sin(a):
    return math.sin(a)

def Cos(a):
    return math.cos(a)

def Tan(a):
    return Cos(a) / Sin(a)

def Sinh(a):
    return math.sinh(a)

def Cosh(a):
    return math.cosh(a)

def Tanh(a):
    return math.tanh(a)

def Hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def CathetusA(b, c):
    return math.sqrt(c ** 2 - b ** 2)

def CathetusB(a, c):
    return math.sqrt(c ** 2 - a ** 2)
