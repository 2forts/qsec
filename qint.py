from projectq.ops import X, CNOT, Toffoli

#A5->yi2, A4->yi1, A3->yi0, A2->xi2, A1->xi1, A0->xi0
#ai7->bi6, ai6->z, ai5->bi5, ai2->bi2, ai1->bi1, x0->yj0
def comparing(bb):
    #Step 1
    X | bb.xi0
    X | bb.xi1
    X | bb.xi2
    X | bb.yi0
    X | bb.yi1
    X | bb.yi2

    #Step 2
    CNOT | (bb.xi0, bb.yj0)
    CNOT | (bb.xi1, bb.bi1)
    CNOT | (bb.xi2, bb.bi2)
    CNOT | (bb.yi0, bb.bi5)
    CNOT | (bb.yi1, bb.z)
    CNOT | (bb.yi2, bb.bi6)

    #Step 3
    CNOT | (bb.xi0, bb.cin2)

    #Step 4
    CNOT | (bb.xi1, bb.xi0)

    #Step 5
    Toffoli | (bb.yj0, bb.cin2, bb.xi0)
    CNOT | (bb.xi2, bb.xi1)

    #Step 6
    Toffoli | (bb.bi1, bb.xi0, bb.xi1)
    CNOT | (bb.yi0, bb.xi2)

    #Step 7
    Toffoli | (bb.bi2, bb.xi1, bb.xi2)
    CNOT | (bb.yi1, bb.yi0)

    #Step 8
    Toffoli | (bb.bi5, bb.xi2, bb.yi0)
    CNOT | (bb.yi2, bb.yi1)

    #Step 9
    Toffoli | (bb.z, bb.yi0, bb.yi1)

    #Step 10
    CNOT | (bb.yi1, bb.bi6)

    #Step 11
    CNOT | (bb.bi6, bb.result)
