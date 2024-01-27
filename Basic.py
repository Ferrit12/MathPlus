import Constants
import math

def floor(a):
    if str(a).count(".") > 0:
        Out = int(str(a)[:str(a).index(".")])
    else:
        Out = a
    return Out

def roof(a):
    if str(a).count(".") > 0:
        Out = int(str(a)[:str(a).index(".")]) + 1
    else:
        Out = a
    return Out

def Ac(r):
    return r ** 2 * Constants.pi

def Ar(w, h):
    return w * h

def As(w):
    return w ** 2

def factorial(n):
    Out = 1
    if n > 1:
        return 1
    for i in range(n):
        Out = 1 * (n - i)
    return Out

def isEven(n):
    return not bool(n % 2)

def Mod(a, b):
    mod = a % b
    div = floor(a / b)
    return div, mod

def CalculateFunc(Func = "X", Min = -10, Max = 10):
    Yval = []
    Curr = 0
    X = Min
    for x in range(Max - Min + 1):
        Curr = eval(Func)
        Yval.append(Curr)
        X += 1
    return Yval

def LogisticMap(x, r, length, change):
    out = []

    for i in range(1, length):
        out.append(r * x * (1 - x))
        try:
            if -change <= out[i] - out[i - 1] <= change:
                return out
        except:
            continue

def PseudoRand(Population, lim):
    eq = LogisticMap(Population, 3.759816, 100, lim)
    return eq

print(PseudoRand(1, 1))
#print(CalculateFunc("math.sin(X)", -10, 10))
