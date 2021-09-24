import sys
import parse
import maths

if len(sys.argv) < 2:
    parse.printHelp()

splittedeq = parse.parseEquation(sys.argv)
verbose, graph = parse.parseArgs(sys.argv)

def printEquation(a, b , c):
    reducedEquation = ""
    if a != 0:
        reducedEquation = "{0}x^2".format(a)
    if b < 0:
        reducedEquation = reducedEquation + "{0}x".format(b)
    elif b > 0:
        if a != 0:
            reducedEquation = reducedEquation + "+{0}x".format(b)
        else:
            reducedEquation = reducedEquation + "{0}x".format(b)
    if c < 0:
        reducedEquation = reducedEquation + "{0}".format(c)
    elif c > 0:
        if (a != 0 or b != 0):
            reducedEquation = reducedEquation + "+{0}".format(c)
        else:
            reducedEquation = reducedEquation + "{0}".format(c)
    if (a == 0 and b == 0 and c == 0):
        reducedEquation = "0"
    print("L'équation réduite est: " + reducedEquation + "=0")
    return reducedEquation

parse.parseInvalidValues(splittedeq, "((^|\+|-)(\s|^)([0-9]*(\.[0-9]+)?)\*?[X|x]\^([0-9]{2,}|[3-9]|\D|$))")
a = parse.findPow2Values(splittedeq[0], "(\+|-|^)(\s|^)([0-9]*(\.[0-9]+)?)\*?[X|x]\^2", 1, 0)
a = parse.findPow2Values(splittedeq[1], "(\+|-|^)(\s|^)([0-9]*(\.[0-9]+)?)\*?[X|x]\^2", -1, a)

b = parse.findPow1Values(splittedeq[0], "(\+|-|^)(\s|^)([0-9]*(\.[0-9]+)?)\*?[X|x]((\^1)|\s|$)", 1, 0)
b = parse.findPow1Values(splittedeq[1], "(\+|-|^)(\s|^)([0-9]*(\.[0-9]+)?)\*?[X|x]((\^1)|\s|$)", -1, b)

c = parse.findPow0Values(splittedeq[0], "(\+|-|^)(\s|^)([0-9]*(\.[0-9]+)?)\*?(([X|x]\^0)|$|\s)", 1, 0)
c = parse.findPow0Values(splittedeq[1], "(\+|-|^)(\s|^)([0-9]*(\.[0-9]+)?)\*?(([X|x]\^0)|$|\s)", -1, c)

reducedEquation = printEquation(a, b, c)

if verbose == True:
    maths.solveVerbose(a, b, c)
else:
    maths.solve(a, b, c)
if graph == True:
    maths.printGraph(a, b, c)