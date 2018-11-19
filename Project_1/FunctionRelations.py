import csv
import math

xValues = []
yValues = []

# Some code written to try but its doesn't work on every situation.

# def findLinear (x, y) :
#     if y > x :
#         if (y - x) > x :
#             print("It is multiplication")
#             quotient = int(y / x)
#             return (str(quotient) + "x + " + str(y % x))
#         else :
#             print("It is Addition Function")
#             return ("x + " + str(y - x))
#     else :
#         if (y - x) > x : 
#             print("It is Division")
#             quotient = int(x / y)
#             return (str(quotient) + "x + " + str(x % y))
#         else:
#             print("It is Substration Function")
#             return ("x - " + str(x - y))

def relation () :
    # tuple first value is coefficient numerator, second value is coefficient Denominator, 
    # third value for Constant 

    funcData = (1 , 1 , 0)

    xDiff = xValues[0] - xValues[1]
    yDiff = yValues[0] - yValues[1]
    
    xyFractionNum = int(funcData[0])
    xyFractionDeno = int(funcData[1])
    constant = int(funcData[2])

    if xDiff > yDiff :
        commonDivider = math.gcd(xDiff, yDiff)
        xDiff = int(xDiff/commonDivider)
        yDiff = int(yDiff/commonDivider)
        # print("xDiff is greater" + str(yDiff) + str(xDiff))
        xyFractionNum = int(yDiff/xDiff)
        constant =  int(yValues[0] - (xyFractionNum * xValues[0]) )
        # print("xDiff is greater" + str(xyFractionNum))
    else :
        # print("yDiff is greater")
        commonDivider = math.gcd(xDiff, yDiff)
        # print("GCD >>> " + str(commonDivider))
        xDiff = xDiff/commonDivider
        yDiff = yDiff/commonDivider
        xyFractionNum = int(yDiff)
        xyFractionDeno = int(xDiff)
        constant =  int(yValues[0] - ((xyFractionNum * xValues[0]) / xyFractionDeno) )

    funcData = (xyFractionNum, xyFractionDeno ,constant)
    return funcData

def fileReader () :
    with open('Dataset_f(x)=2x-10.txt') as csv_file:
    # with open('Dataset_f(x)=-x.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                x = int(row[0])
                y = int(row[1])
                xValues.append(x)
                yValues.append(y)
                print(f'\t x is {row[0]} and y is {row[1]}')
                line_count += 1
        print(f'Processed {line_count} lines.')
        

def printEachFunction () :
    t = relation()

    for x in range(len(xValues)):
        xInt = t[1]
        constant = t[2]
        constantStr = ""

        if constant != 0:
            constantStr = str(t[2])
        if xInt == 1: 
            print(str(t[0]) + "x" + constantStr)
        elif xInt == -1:
            print(str(t[0] * t[1]) + "x" + "+"+ constantStr)
        else:
            print("FUNCTION FOR Index : " + str(x) + " is " + str(t[0]) + str(t[1]) + "+" + constant)

        # print("X value is ,Index : " + str(x) + str(t[0]) + str(t[1]) + str(t[2]))
        # if (((xValues[x] * t[0]) / t[1]) + t[2]) - yValues[x]  == 0:
        #     print("function  right")
        # else : 
        #     print("Function is not correct")
        

fileReader()
printEachFunction()

 
