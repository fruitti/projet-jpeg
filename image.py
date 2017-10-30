import math
from heapq import *




def createMatrix(x, y):
    matrix = [[0] * x for _ in range(y)]
    return matrix


def printMatrix(matrix):
    autre = ""
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            autre = autre + " " + str(matrix[i][j])
        print(autre)
        autre = ""


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
    return coefDCT


def quantification(coefDCT, coefQuant):
    for i in range(8):
        for j in range(8):
            coefQuant[i][j] = math.trunc((coefDCT[i][j]) / coefQuant[i][j])
    printMatrix(coefQuant)
    return coefQuant


def codageZigZag(xMax, yMax):
    x = 0
    y = 0
    croiss = 0
    tab = []
    matrice = [[139, 144, 149, 153, 155, 155, 155, 155],
               [144, 151, 153, 156, 159, 156, 156, 156],
               [150, 155, 160, 163, 158, 156, 156, 156],
               [159, 161, 162, 160, 160, 159, 159, 159],
               [159, 160, 161, 162, 162, 155, 155, 155],
               [161, 161, 161, 161, 160, 157, 157, 157],
               [162, 162, 161, 163, 162, 157, 157, 157],
               [162, 162, 161, 161, 163, 158, 158, 158]]

    while x <= xMax and y <= yMax:

        tab.append(matrice[x][y])
        if x == 0 or x == xMax:
            if y == yMax:
                y = y - 1
                x = x + 1

            else:
                y = y + 1
            tab.append(matrice[x][y])
        else:

            if y == 0 or y == yMax:
                if x == xMax:
                    x = x -1
                    y = y + 1

                else:
                    x = x + 1
                tab.append(matrice[x][y])

        if x == 0 or y == yMax:
            croiss = 0
        if y == 0 or x == xMax:
            croiss = 1

        if croiss == 1:
            x = x - 1
            y = y + 1
        else:
            x = x + 1
            y = y - 1
    print (tab)
    return tab

def rle(tab):
    compteur = 0
    list = []
    for i in range (0, len(tab)):
        if i == len(tab)-1:
            compteur = compteur +1
            tuple = (compteur, tab[i])
            list.append(tuple)
        else :
            if tab[i] == tab[i + 1]:
                compteur = compteur +1
            else :
                compteur = compteur + 1
                tuple = (compteur, tab[i])
                list.append(tuple)
                compteur = 0
    return list

def table_frequences(tab):
    table = {}
    for nombre in tab:
        if nombre in table:
            table[nombre] = table[nombre] +1
        else :
            table[nombre] = 1
    return table

def arbre_huffman(occurrences):
    # Construction d'un tas avec les lettres sous forme de feuilles
    tas = [(occ, lettre) for (lettre, occ) in occurrences.items()]
    heapify(tas)

    # Création de l'arbre
    while len(tas) >= 2:
        occ1, noeud1 = heappop(tas) # noeud de plus petit poids occ1
        occ2, noeud2 = heappop(tas) # noeud de deuxième plus petit poids occ2
        heappush(tas, (occ1 + occ2, {0: noeud1, 1: noeud2}))
        # ajoute au tas le noeud de poids occ1+occ2 et avec les fils noeud1 et noeud2

    return heappop(tas)[1]

matrice = [[139, 144, 149, 153, 155, 155, 155, 155],
           [144, 151, 153, 156, 159, 156, 156, 156],
           [150, 155, 160, 163, 158, 156, 156, 156],
           [159, 161, 162, 160, 160, 159, 159, 159],
           [159, 160, 161, 162, 162, 155, 155, 155],
           [161, 161, 161, 161, 160, 157, 157, 157],
           [162, 162, 161, 163, 162, 157, 157, 157],
           [162, 162, 161, 161, 163, 158, 158, 158]]

coefDCT = createMatrix(8, 8)
coefQuant = [[16, 11, 10, 16, 24, 40, 51, 61],
             [12, 12, 14, 19, 26, 58, 60, 55],
             [14, 13, 16, 24, 40, 57, 69, 56],
             [14, 17, 22, 29, 51, 87, 80, 62],
             [18, 22, 37, 56, 68, 109, 103, 77],
             [24, 35, 55, 64, 81, 104, 113, 92],
             [49, 64, 78, 87, 103, 121, 120, 101],
             [72, 92, 95, 98, 112, 100, 103, 99]]

print("dct = \n")
test = dct(matrice, coefDCT)
print("quant = \n")

print("zigzag = \n")
tab = codageZigZag(7, 7)
liste = rle(tab)
print("rle = \n", liste)
print("table frequence", table_frequences(tab))
print ("huffman : ", arbre_huffman(table_frequences(tab)))

