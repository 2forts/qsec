from projectq.ops import X, CNOT, Toffoli

def subtractingX(eng, bb):
    #Step 1
    X | bb.cin
    X | bb.xj0
    X | bb.xj1
    X | bb.xj2

    #Step 2
    CNOT | (bb.xi0, bb.xj0)
    CNOT | (bb.xi1, bb.xj1)
    CNOT | (bb.xi2, bb.xj2)

    #Step 3
    CNOT | (bb.xi0, bb.cin)

    #Step 4
    CNOT | (bb.xi1, bb.xi0)

    #Step 5
    Toffoli | (bb.cin, bb.xj0, bb.xi0)
    CNOT | (bb.xi2, bb.xi1)

    #Step 6
    Toffoli | (bb.xi0, bb.xj1, bb.xi1)

    #Step 8
    X | bb.xj0
    X | bb.xj1
    CNOT | (bb.xi1, bb.xj2)

    #Step 9
    X | bb.xj1
    Toffoli | (bb.xi0, bb.xj1, bb.xi1)
    X | bb.xj1
    CNOT | (bb.xi0, bb.xj1)

    #Step 10
    X | bb.xj0
    Toffoli | (bb.cin, bb.xj0, bb.xi0)
    X | bb.xj0
    CNOT | (bb.cin, bb.xj0)
    X | bb.xj1
    CNOT | (bb.xi2, bb.xi1)

    #Step 12
    X | bb.xj0
    CNOT | (bb.xi1, bb.xi0)

    #Step 13
    CNOT | (bb.xi0, bb.cin)

    #Step 15
    CNOT | (bb.xi0, bb.xj0)
    CNOT | (bb.xi1, bb.xj1)
    CNOT | (bb.xi2, bb.xj2)
    X | bb.cin

def subtractingY(eng, bb):
    #Step 1
    X | bb.cin
    X | bb.yj0
    X | bb.yj1
    X | bb.yj2

    #Step 2
    CNOT | (bb.yi0, bb.yj0)
    CNOT | (bb.yi1, bb.yj1)
    CNOT | (bb.yi2, bb.yj2)

    #Step 3
    CNOT | (bb.yi0, bb.cin)

    #Step 4
    CNOT | (bb.yi1, bb.yi0)

    #Step 5
    Toffoli | (bb.cin, bb.yj0, bb.yi0)
    CNOT | (bb.yi2, bb.yi1)

    #Step 6
    Toffoli | (bb.yi0, bb.yj1, bb.yi1)

    #Step 8
    X | bb.yj0
    X | bb.yj1
    CNOT | (bb.yi1, bb.yj2)

    #Step 9
    X | bb.yj1
    Toffoli | (bb.yi0, bb.yj1, bb.yi1)
    X | bb.yj1
    CNOT | (bb.yi0, bb.yj1)

    #Step 10
    X | bb.yj0
    Toffoli | (bb.cin, bb.yj0, bb.yi0)
    X | bb.yj0
    CNOT | (bb.cin, bb.yj0)
    X | bb.yj1
    CNOT | (bb.yi2, bb.yi1)

    #Step 12
    X | bb.yj0
    CNOT | (bb.yi1, bb.yi0)

    #Step 13
    CNOT | (bb.yi0, bb.cin)

    #Step 15
    CNOT | (bb.yi0, bb.yj0)
    CNOT | (bb.yi1, bb.yj1)
    CNOT | (bb.yi2, bb.yj2)
    X | bb.cin

def squaringX(bb):
    #Step 1
    #X | ai0
    #X | ai3
    #X | ai4

    #Step 2
    Toffoli | (bb.xj0, bb.xj1, bb.ai2)

    #Step 3
    Toffoli | (bb.xj0, bb.xj2, bb.ai3)

    #Step 4
    Toffoli | (bb.xj1, bb.xj2, bb.ai4)

    #Step 5
    Toffoli | (bb.xj1, bb.ai2, bb.ai5)
    CNOT | (bb.xj1, bb.ai2)

    #Step 6
    #ControlledGate(X, 3) | (ai0, ai3, ai5, ai6)
    Toffoli | (bb.ai0, bb.ai3, bb.ai5)

    #Step 7
    #ControlledGate(X, 3) | (xj2, ai4, ai6, ai7)
    #Toffoli | (xj2, ai4, ai6)

def squaringY(bb):
    #Step 1
    #X | bi0
    #X | bi3
    #X | bi4

    #Step 2
    Toffoli | (bb.yj0, bb.yj1, bb.bi2)

    #Step 3
    Toffoli | (bb.yj0, bb.yj2, bb.bi3)

    #Step 4
    Toffoli | (bb.yj1, bb.yj2, bb.bi4)

    #Step 5
    Toffoli | (bb.yj1, bb.bi2, bb.bi5)
    CNOT | (bb.yj1, bb.bi2)

    #Step 6
    #ControlledGate(X, 3) | (bi0, bi3, bi5, bi6)
    Toffoli | (bb.bi0, bb.bi3, bb.bi5)

    #Step 7
    #ControlledGate(X, 3) | (yj2, bi4, bi6, bi7)
    #Toffoli | (yj2, bi4, bi6)

#outputs: a0->xj0, a1->ai1, a2->ai2, a3->ai5
#outputs: b0->yj0, b1->bi1, b2->bi2, b3->bi5
def addingNoCarryInput(bb):
    #Step 2
    CNOT | (bb.ai1, bb.bi1)
    CNOT | (bb.ai2, bb.bi2)
    CNOT | (bb.ai5, bb.bi5)

    #Step 3
    CNOT | (bb.ai5, bb.z)

    #Step 4
    CNOT | (bb.ai2, bb.ai5)

    #Step 5
    CNOT | (bb.ai1, bb.ai2)

    #Step 6
    Toffoli | (bb.yj0, bb.xj0, bb.ai1)

    #Step 7
    Toffoli | (bb.bi1, bb.ai1, bb.ai2)

    #Step 8
    Toffoli | (bb.bi2, bb.ai2, bb.ai5)

    #Step 9
    Toffoli | (bb.ai5, bb.bi5, bb.z)
    CNOT | (bb.ai5, bb.bi5)

    #Step 10
    Toffoli | (bb.ai2, bb.bi2, bb.ai5)
    CNOT | (bb.ai2, bb.bi2)

    #Step 11
    Toffoli | (bb.ai1, bb.bi1, bb.ai2)
    CNOT | (bb.ai1, bb.bi1)

    #Step 12
    Toffoli | (bb.xj0, bb.yj0, bb.ai1)
    CNOT | (bb.xj0, bb.yj0)

    #Step 13
    CNOT | (bb.ai1, bb.ai2)

    #Step 14
    CNOT | (bb.ai2, bb.bi5)

    #Step 15
    CNOT | (bb.ai1, bb.bi1)
    CNOT | (bb.ai2, bb.bi2)
    CNOT | (bb.ai5, bb.bi5)
