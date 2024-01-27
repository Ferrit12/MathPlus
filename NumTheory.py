import math

def exp(a, b):
    """
    Power function
    """
    return a ** b

def Log(a, Base):
    return math.log(a) / math.log(Base)

def S(a):
    """
    Successor function
    """
    return a + 1

def P(a):
    """
    Predecessor function
    """
    return a - 1

def R(a):
    """
    Ratio function
    """
    return 1 / a

def tet(a, b):
    """
    Tetration function
    """
    c = a
    for i in range(b):
        c = c ** a
    return c

def pent(a, b):
    """
    Pentation function
    """
    c = a
    for i in range(b):
        c = tet(c, a)
    return c

def hexa(a, b):
    """
    Hexation function
    """
    c = a
    for i in range(b):
        c = pent(c, a)
    return c
