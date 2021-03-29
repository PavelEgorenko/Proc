from matrices import InMtx
from matrices import OutMtx
from diagonal_matrix import OutDiag
from binary_matix import OutBin
class container():
    matrices = []

def InData(matrices, file):
    for line in file:
        InMtx(matrices, line)


def OutData(matrices, ofst):
    ofst.write("Container contains " + str(len(matrices)) + " elements.\n")
    for i in range(len(matrices)):
        ofst.write(str(i + 1) + ": ")
        OutMtx(matrices[i], ofst)

def OutDataFiltr(matrices, ofst):
    ofst.write("Container contains " + str(len(matrices)) + " elements.\n")
    for i in range(len(matrices)):
        if matrices[i].type == "Bin":
            ofst.write(str(i + 1) + ": ")
            OutMtx(matrices[i], ofst)

def Clear(matrices):
    matrices.clear()
