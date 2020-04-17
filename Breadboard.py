#
#Breadboard of the circuit. It includes the declaration of the necessary qubits.
#@version 1.0
#@author: Francisco Orts <francisco.orts@ual.es>
#

from projectq.ops import X

class Breadboard:
    def __init__(self, eng):
        #Coordinates of point i
        self.xi0 = eng.allocate_qubit()
        self.xi1 = eng.allocate_qubit()
        self.xi2 = eng.allocate_qubit()
        self.yi0 = eng.allocate_qubit()
        self.yi1 = eng.allocate_qubit()
        self.yi2 = eng.allocate_qubit()

        #Coordinates of point j
        self.xj0 = eng.allocate_qubit()
        self.xj1 = eng.allocate_qubit()
        self.xj2 = eng.allocate_qubit()
        self.yj0 = eng.allocate_qubit()
        self.yj1 = eng.allocate_qubit()
        self.yj2 = eng.allocate_qubit()

        #ancilla inputs
        self.ai0 = eng.allocate_qubit()
        self.ai1 = eng.allocate_qubit()
        self.ai2 = eng.allocate_qubit()
        self.ai3 = eng.allocate_qubit()
        self.ai4 = eng.allocate_qubit()
        self.ai5 = eng.allocate_qubit()
        
        self.bi0 = eng.allocate_qubit()
        self.bi1 = eng.allocate_qubit()
        self.bi2 = eng.allocate_qubit()
        self.bi3 = eng.allocate_qubit()
        self.bi4 = eng.allocate_qubit()
        self.bi5 = eng.allocate_qubit()
        self.bi6 = eng.allocate_qubit()

        #Auxiliar qubit for the subtraction. Please, refer to
        #qmath.py for more info
        self.cin = eng.allocate_qubit()

        self.z = eng.allocate_qubit()

        #output of the circuit
        self.result = eng.allocate_qubit()
