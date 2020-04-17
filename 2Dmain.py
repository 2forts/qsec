#
#A quantum circuit for Squared Euclidean Distance comparison
#@version 1.0
#@author: Francisco Orts <francisco.orts@ual.es>
#

from projectq import MainEngine  # import the main compiler engine
from projectq.ops import X, Measure  # import the operations we want to perform (X and measurement)

from qmath import subtractingX, subtractingY, squaringX, squaringY, addingNoCarryInput, UNCOMPUTEaddingNoCarryInput, UNCOMPUTEsquaring, UNCOMPUTEsubtracting
from qint import comparing
from Breadboard import *

import sys

if len(sys.argv) != 6:
        sys.exit("This program needs two coordinates from two particles and the distance^2 as input parameters.")

#Obtaining the coordinates
sCoordinatesxA = str(sys.argv[1])
sCoordinatesxB = str(sys.argv[2])
sCoordinatesyA = str(sys.argv[3])
sCoordinatesyB = str(sys.argv[4])
sDeltaSqr = str(sys.argv[5])

eng = MainEngine()  # create a default compiler (the back-end is a simulator)
bb = Breadboard(eng)

#Coordinates x of i
if sCoordinatesxA[2] == "1":
    #print("Negating xi0...")
    X | bb.xi0
if sCoordinatesxA[1] == "1":
    #print("Negating xi1...")
    X | bb.xi1
if sCoordinatesxA[0] == "1":
    #print("Negating xi2...")
    X | bb.xi2

#Coordinates x of j
if sCoordinatesxB[2] == "1":
    #print("Negating xj0...")
    X | bb.xj0
if sCoordinatesxB[1] == "1":
    #print("Negating xj1...")
    X | bb.xj1
if sCoordinatesxB[0] == "1":
    #print("Negating xj2...")
    X | bb.xj2

#Coordinates y of i
if sCoordinatesyA[2] == "1":
    #print("Negating yi0...")
    X | bb.yi0
if sCoordinatesyA[1] == "1":
    #print("Negating yi1...")
    X | bb.yi1
if sCoordinatesyA[0] == "1":
    #print("Negating yi2...")
    X | bb.yi2

#Coordinates y of j
if sCoordinatesyB[2] == "1":
    #print("Negating yj0...")
    X | bb.yj0
if sCoordinatesyB[1] == "1":
    #print("Negating yj1...")
    X | bb.yj1
if sCoordinatesyB[0] == "1":
    #print("Negating yj2...")
    X | bb.yj2

#Difference between coordinates
subtractingX(eng, bb) #outputs: xj2, xj1, xj0
subtractingY(eng, bb) #outputs: yj2, yj1, yj0

#Squaring the differences
X | bb.ai0
X | bb.bi0
squaringX(bb) #outputs: xj0, ai1, ai2, ai5, ai6
squaringY(bb) #outputs: yj0, bi1, bi2, bi5, bi6

#Adding the squares
addingNoCarryInput(bb) #outputs: yj0, bi1, bi2, bi5, z

#Reverting xi and yi to use these qubits
if sCoordinatesxA[2] == "1":
    X | bb.xi0
if sCoordinatesxA[1] == "1":
    X | bb.xi1
if sCoordinatesxA[0] == "1":
    X | bb.xi2
if sCoordinatesyA[2] == "1":
    X | bb.yi0
if sCoordinatesyA[1] == "1":
    X | bb.yi1
if sCoordinatesyA[0] == "1":
    X | bb.yi2

#Distance^2
if sDeltaSqr[5] == "1":
    X | bb.xi0
if sDeltaSqr[4] == "1":
    X | bb.xi1
if sDeltaSqr[3] == "1":
    X | bb.xi2
if sDeltaSqr[2] == "1":
    X | bb.yi0
if sDeltaSqr[1] == "1":
    X | bb.yi1
if sDeltaSqr[0] == "1":
    X | bb.yi2

#Final comparison (and its uncomputation)
comparing(bb)

#
#UNCOMPUTATION
#
#Reverting Distance^2
if sDeltaSqr[5] == "1":
    X | bb.xi0
if sDeltaSqr[4] == "1":
    X | bb.xi1
if sDeltaSqr[3] == "1":
    X | bb.xi2
if sDeltaSqr[2] == "1":
    X | bb.yi0
if sDeltaSqr[1] == "1":
    X | bb.yi1
if sDeltaSqr[0] == "1":
    X | bb.yi2
#Uncomptuing xi and yi
if sCoordinatesxA[2] == "1":
    X | bb.xi0
if sCoordinatesxA[1] == "1":
    X | bb.xi1
if sCoordinatesxA[0] == "1":
    X | bb.xi2
if sCoordinatesyA[2] == "1":
    X | bb.yi0
if sCoordinatesyA[1] == "1":
    X | bb.yi1
if sCoordinatesyA[0] == "1":
    X | bb.yi2

UNCOMPUTEaddingNoCarryInput(bb)
UNCOMPUTEsquaring(bb)
X | bb.ai0
X | bb.bi0
UNCOMPUTEsubtracting(bb)

#Coordinates x of i
if sCoordinatesxA[2] == "1":
    #print("Negating xi0...")
    X | bb.xi0
if sCoordinatesxA[1] == "1":
    #print("Negating xi1...")
    X | bb.xi1
if sCoordinatesxA[0] == "1":
    #print("Negating xi2...")
    X | bb.xi2

#Coordinates x of j
if sCoordinatesxB[2] == "1":
    #print("Negating xj0...")
    X | bb.xj0
if sCoordinatesxB[1] == "1":
    #print("Negating xj1...")
    X | bb.xj1
if sCoordinatesxB[0] == "1":
    #print("Negating xj2...")
    X | bb.xj2

#Coordinates y of i
if sCoordinatesyA[2] == "1":
    #print("Negating yi0...")
    X | bb.yi0
if sCoordinatesyA[1] == "1":
    #print("Negating yi1...")
    X | bb.yi1
if sCoordinatesyA[0] == "1":
    #print("Negating yi2...")
    X | bb.yi2

#Coordinates y of j
if sCoordinatesyB[2] == "1":
    #print("Negating yj0...")
    X | bb.yj0
if sCoordinatesyB[1] == "1":
    #print("Negating yj1...")
    X | bb.yj1
if sCoordinatesyB[0] == "1":
    #print("Negating yj2...")
    X | bb.yj2

X | bb.result #Change to invert the result if necessary

Measure | bb.result

eng.flush()  # flush all gates (and execute measurements)
print("Measured:"+format(int(bb.result)))
