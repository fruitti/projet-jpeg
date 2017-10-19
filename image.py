import imageio
import matplotlib.pyplot as plt
import math
def createMatrix(x,y):
    matrix =  [[0] * x for _ in range(y)]
    return matrix
def printMatrix(matrix):
    autre = ""
    for i in range(0,len(matrix)):
        for j in range(0, len(matrix)):
            autre = autre+ " "+  str(matrix[i][j])
        print(autre)
        autre=""

def dct(matrice, coefDCT):
    Ci = 0
    Cj = 0
    for i in range(8):
        for j in range(8):
            for x in range(8):
                for y in range(8):
                    coefDCT[i][j] += matrice[x][y] * (
                    math.cos((math.pi * (2 * y + 1) * j) / 16) * math.cos((math.pi * (2 * x + 1) * i) / 16))
            if (j == 0):
                Cj = 1 / math.sqrt(2)
            else:
                Cj = 1
            if (i == 0):
                Ci = 1 / math.sqrt(2)
            else:
                Ci = 1
            coefDCT[i][j] = (coefDCT[i][j] * 0.25 * Cj * Ci)

    printMatrix(coefDCT)

def quantification(coefDCT,coefQuant):

    for i in range(8):
        for j in range(8):
            coefQuant[i][j] = math.trunc((coefDCT[i][j])/coefQuant[i][j])
    printMatrix(coefQuant)


matrice = [[139,144,149,153,155,155,155,155],
           [144,151,153,156,159,156,156,156],
           [150,155,160,163,158,156,156,156],
           [159,161,162,160,160,159,159,159],
           [159,160,161,162,162,155,155,155],
           [161,161,161,161,160,157,157,157],
           [162,162,161,163,162,157,157,157],
           [162,162,161,161,163,158,158,158]]

coefDCT = createMatrix(8,8)
coefQuant = [[16,11,10,16,24,40,51,61],
             [12,12,14,19,26,58,60,55],
             [14,13,16,24,40,57,69,56],
             [14,17,22,29,51,87,80,62],
             [18,22,37,56,68,109,103,77],
             [24,35,55,64,81,104,113,92],
             [49,64,78,87,103,121,120,101],
             [72,92,95,98,112,100,103,99]]


print("dct = \n")
dct(matrice, coefDCT)
print("quant = \n")
quantification(coefDCT,coefQuant)
