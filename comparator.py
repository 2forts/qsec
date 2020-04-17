#
#A quantum circuit for Squared Euclidean Distance comparison
#@version 1.0
#@author: Francisco Orts <francisco.orts@ual.es>
#

from projectq import MainEngine  # import the main compiler engine
from projectq.ops import X, Measure, CNOT, Toffoli  # import the operations we want to perform (X and measurement)

import sys

if len(sys.argv) != 3:
        sys.exit("This program needs two 6-bit numbers.")

eng = MainEngine()

a0 = eng.allocate_qubit()
a1 = eng.allocate_qubit()
a2 = eng.allocate_qubit()
a3 = eng.allocate_qubit()
a4 = eng.allocate_qubit()
a5 = eng.allocate_qubit()
b0 = eng.allocate_qubit()
b1 = eng.allocate_qubit()
b2 = eng.allocate_qubit()
b3 = eng.allocate_qubit()
b4 = eng.allocate_qubit()
b5 = eng.allocate_qubit()

sol = eng.allocate_qubit()

#Obtaining the coordinates
sCoordinatesA = str(sys.argv[1])
sCoordinatesB = str(sys.argv[2])

eng = MainEngine()  # create a default compiler (the back-end is a simulator)

if sCoordinatesA[5] == "1":
    X | a0
if sCoordinatesA[4] == "1":
    X | a1
if sCoordinatesA[3] == "1":
    X | a2
if sCoordinatesA[2] == "1":
    X | a3
if sCoordinatesA[1] == "1":
    X | a4
if sCoordinatesA[0] == "1":
    X | a5

if sCoordinatesB[5] == "1":
    X | b0
if sCoordinatesB[4] == "1":
    X | b1
if sCoordinatesB[3] == "1":
    X | b2
if sCoordinatesB[2] == "1":
    X | b3
if sCoordinatesB[1] == "1":
    X | b4
if sCoordinatesB[0] == "1":
    X | b5

#Step 1
X | a0
X | a1
X | a2
X | a3
X | a4
X | a5

#Step 2
CNOT | (a1, b1)
CNOT | (a2, b2)
CNOT | (a3, b3)
CNOT | (a4, b4)
CNOT | (a5, b5)

#Step 3
CNOT | (a5, sol)
CNOT | (a4, a5)
CNOT | (a3, a4)
CNOT | (a2, a3)
CNOT | (a1, a2)

#Step 4
Toffoli | (b0, a0, a1)
Toffoli | (b1, a1, a2)
Toffoli | (b2, a2, a3)
Toffoli | (b3, a3, a4)
Toffoli | (b4, a4, a5)
Toffoli | (b5, a5, sol)

#UNCOMPUTE TO AVOID GABAGE OUTPUTS
#Step 4
Toffoli | (b4, a4, a5)
Toffoli | (b3, a3, a4)
Toffoli | (b2, a2, a3)
Toffoli | (b1, a1, a2)
Toffoli | (b0, a0, a1)

#Step 3
CNOT | (a1, a2)
CNOT | (a2, a3)
CNOT | (a3, a4)
CNOT | (a4, a5)

#Step 2
CNOT | (a1, b1)
CNOT | (a2, b2)
CNOT | (a3, b3)
CNOT | (a4, b4)
CNOT | (a5, b5)

#Step 1
X | a0
X | a1
X | a2
X | a3
X | a4
X | a5

Measure | sol

eng.flush()  # flush all gates (and execute measurements)
print("Measured:"+format(int(sol)))
