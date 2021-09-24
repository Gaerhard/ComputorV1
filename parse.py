import re
import sys

def printHelp():
    print("This is a quadratic Equation solver")
    print("     Usage: python|python3 computor.py [equation] [options]")
    print("     Options:")
    print("         -h  :  Help")
    print("         -v  :  Verbose")
    print("         -g  :  Graph")
    exit()

def parseEquation(args):
    equ = args[1].replace(" ", "").replace("+", " + ").replace("-", " - ")
    splittedeq = equ.split("=")
    if (len(splittedeq) != 2):
        print("Invalid entry")
        exit()
    return splittedeq

def parseArgs(args):
    verbose = False
    graph = False
    if (len(args) < 3):
        return verbose, graph
    else:
        for arg in args:
            if arg == "-h":
                printHelp()
                exit()
            elif arg == "-v":
                verbose = True
            elif arg == "-g":
                graph = True
        return verbose, graph

def findPow2Values(str, reg, reversed, res):
    listOfPow2Values = re.findall(reg, str)
    for (sign, extraData, coefficient, extraDataBis) in listOfPow2Values:
        if coefficient == "":
            coefficient = 1
        coefficient = float(coefficient)
        if sign == '-':
            coefficient *= -1
        res = res + coefficient * reversed
    return res

def findPow1Values(str, reg, reversed, res):
    listOfPow1Values = re.findall(reg, str)
    for (sign, extraData, coefficient, extraDataBis, extraDataTer, extraDataQuad) in listOfPow1Values:
        if coefficient == "":
            coefficient = 1
        coefficient = float(coefficient)
        if sign == '-':
            coefficient *= -1
        res = res + coefficient * reversed
    return res

def findPow0Values(str, reg, reversed, res):
    listOfPow0Values = re.findall(reg, str)
    for (sign, extraData, coefficient, extraDataBis, extraDataTer, extraDataQuad) in listOfPow0Values:
        if coefficient == "":
            if extraDataTer == "" or extraDataTer == " ":
                coefficient = 0
            else:
                coefficient = 1
        coefficient = float(coefficient)
        if sign == '-':
            coefficient *= -1
        res = res + coefficient * reversed
    return res

def parseInvalidValues(splittedeq, reg):
    listOfInvalidPow = re.findall(reg, splittedeq[0])
    ret = ""
    i = 0
    if listOfInvalidPow :
        for invalidEntries in listOfInvalidPow:
            if i == 0:
                ret = ret + invalidEntries[0]
            else:
                ret = ret + " et " + invalidEntries[0]
            i += 1
    listOfInvalidPow = re.findall(reg, splittedeq[1])
    if listOfInvalidPow :
        for invalidEntries in listOfInvalidPow:
            if i == 0:
                ret = ret + invalidEntries[0]
            else:
                ret = ret + " et " + invalidEntries[0]
            i += 1
    listOfInvalidPow = re.findall(reg, ret)
    if len(listOfInvalidPow) > 1:
        print(ret, "ne sont pas des entrées valides")
        exit()
    elif len(listOfInvalidPow) > 0:
        print(ret, "n'est pas une entrée valide")
        exit()