from matplotlib import pyplot as plt
import numpy as np

def ftAbs(n):
    if (n < 0):
        return -n
    return n

def ftSqrt(value):
    low = 0
    high = value
    mid = value
    oldMid = -1
    while (ftAbs(oldMid - mid) >= 0.0000001):
        oldMid = mid
        mid = (high + low) / 2
        if mid*mid > value:
            high = mid
        else:
            low = mid
    return mid

def convertDecimalToFraction(d):
    d *= 10000
    n = 10000
    if d == 0:
        return "0"
    dividende = d 
    diviseur = n
    if d < n:
        d, n = n, d
    r = d % n
    while r != 0:
        r = d % n
        if r == 0:
            break
        d, n = n, r
    if dividende/n >= 10000 or diviseur/n >= 10000:
        return(str(dividende/10000))
    if dividende / n < 0:
        if diviseur / n < 0:
            dividende = -dividende
            diviseur = -diviseur
    elif diviseur / n < 0:
        dividende = -dividende
        diviseur = -diviseur
    res = str(int(dividende/n)) + "/" + str(int(diviseur/n))
    return res
    
def printGraph(a, b, c):
    x = np.arange(-20,20,0.1)
    y = a*x**2+b*x+c
    plt.plot(x,y)
    plt.grid(True)
    plt.show()

def solve(a, b, c):
    if (a == 0):
        if (b == 0 and c == 0):
            print("Il y a une infinité de solutions")
        elif (b == 0 and c != 0):
            print("Il n'y a pas de solution")
        else:
            print("La solution est donc x = ", convertDecimalToFraction(round(-c/b, 4)))
    else :
        delta = b*b - 4*a*c
        if (delta > 0):
            x1 = (-b - ftSqrt(delta)) / (2*a)
            x2 = (-b + ftSqrt(delta)) / (2*a)
            print("Les solutions sont: x1 = {0} et x2 = {1}".format(
                convertDecimalToFraction(round(x1, 4)), convertDecimalToFraction(round(x2, 4))))
        elif (delta == 0):
            x = (-b) / (2 * a)
            print("La solution est: x = ", convertDecimalToFraction(round(x, 4)))
        else:
            print ("Les solutions sont: \n x1 = ({0}-i√{1})/{2} \n x2 = ({0}+i√{1})/{2}".format(-b, -delta, 2*a))

def solveVerbose(a, b, c) :
    if (a == 0):
        print("Le coefficient a est nul c'est donc une équation du premier degré")
        if (b == 0 and c == 0):
            print("Il y a une infinité de solutions")
        elif (b == 0 and c != 0):
            print("Il n'y a pas de solution")
        else:
            print("La solution sous forme de fraction irréductible est donc x = "
                , convertDecimalToFraction(round(-c/b, 4)))
            print("La solution sous forme décimale est x = ", round(-c/b, 4))
    else:
        delta = b*b - 4*a*c
        print("Δ = b^2 - 4*a*c")
        print("Δ = {1}^2 - 4*{0}*{2} = {3}".format(a, b, c, delta))
        if (delta > 0):
            print("Le discriminant {} est positif. Il y a donc deux solutions".format(delta))
            print("x1 = (-b - √Δ) / 2*a")
            print("x2 = (-b + √Δ) / 2*a")
            print("x1 = ({1} - √{2}) / 2*{0}".format(a, -b, delta))
            print("x2 = ({1} + √{2}) / 2*{0}".format(a, -b, delta))
            x1 = (-b - ftSqrt(delta)) / (2*a)
            x2 = (-b + ftSqrt(delta)) / (2*a)
            print("Les solutions sont sous forme de fraction irréductible: x1 = {0} et x2 = {1}"
                .format(convertDecimalToFraction(round(x1, 4)), convertDecimalToFraction(round(x2, 4))))
            print("Les solutions décimales sont: x1 = {0} et x2 = {1}".format(round(x1, 4), round(x2, 4)))
        elif (delta == 0):
            print("Le discriminant est nul, il n'y a donc qu'une seule solution")
            print("x1 = -b / (2 * a)")
            print("x1 = {1} / (2 * {0})".format(a, -b))
            x = (-b) / (2 * a)
            print("La solution en fraction irréductible est: x = ", convertDecimalToFraction(round(x, 4)))
            print("La solution décimale est: x = ", round(x, 4))
        else:
            print("Le discriminant {} est négatif. Les solutions sont donc complexes".format(delta))
            print ("Les solutions sont: \n x1 = ({0}-i√{1})/{2} \n x2 = ({0}+i√{1})/{2}".format(-b, -delta, 2*a))