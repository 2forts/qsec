#
#Comparator circuit. It only uses 1 ancilla input
#@version 1.0
#@author: Francisco Orts <francisco.orts@ual.es>
#

from projectq.ops import X, CNOT, Toffoli

def comparing(bb):
    #Step 1
    X | bb.yj0
    X | bb.bi1
    X | bb.bi2
    X | bb.bi5
    X | bb.z
    X | bb.bi6

    #Step 2
    CNOT | (bb.bi1, bb.xi1)
    CNOT | (bb.bi2, bb.xi2)
    CNOT | (bb.bi5, bb.yi0)
    CNOT | (bb.z, bb.yi1)
    CNOT | (bb.bi6, bb.yi2)

    #Step 3
    CNOT | (bb.bi6, bb.result)
    CNOT | (bb.z, bb.bi6)
    CNOT | (bb.bi5, bb.z)
    CNOT | (bb.bi2, bb.bi5)
    CNOT | (bb.bi1, bb.bi2)

    #Step 4
    Toffoli | (bb.xi0, bb.yj0, bb.bi1)
    Toffoli | (bb.xi1, bb.bi1, bb.bi2)
    Toffoli | (bb.xi2, bb.bi2, bb.bi5)
    Toffoli | (bb.yi0, bb.bi5, bb.z)
    Toffoli | (bb.yi1, bb.z, bb.bi6)
    Toffoli | (bb.yi2, bb.bi6, bb.result) #The result

    #UNCOMPUTE TO AVOID GABAGE OUTPUTS
    #Step 4
    Toffoli | (bb.yi1, bb.z, bb.bi6)
    Toffoli | (bb.yi0, bb.bi5, bb.z)
    Toffoli | (bb.xi2, bb.bi2, bb.bi5)
    Toffoli | (bb.xi1, bb.bi1, bb.bi2)
    Toffoli | (bb.xi0, bb.yj0, bb.bi1)

    #Step 3
    CNOT | (bb.bi1, bb.bi2)
    CNOT | (bb.bi2, bb.bi5)
    CNOT | (bb.bi5, bb.z)
    CNOT | (bb.z, bb.bi6)

    #Step 2
    CNOT | (bb.bi1, bb.xi1)
    CNOT | (bb.bi2, bb.xi2)
    CNOT | (bb.bi5, bb.yi0)
    CNOT | (bb.z, bb.yi1)
    CNOT | (bb.bi6, bb.yi2)

    #Step 1
    X | bb.yj0
    X | bb.bi1
    X | bb.bi2
    X | bb.bi5
    X | bb.z
    X | bb.bi6
