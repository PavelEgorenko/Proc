from matrices import InMtx
from matrices import OutMtx
from diagonal_matrix import OutDiag, diagonal_matrix
from binary_matix import OutBin, bin_matrix


class container:
    matrices = []


def InData(matrices, file):
    for line in file:
        InMtx(matrices, line)


def OutData(matrices, ofst):
    ofst.write("Container contains " + str(len(matrices)) + " elements.\n")
    for i in range(len(matrices)):
        ofst.write(str(i + 1) + ": ")
        OutMtx(matrices[i], ofst)


def Sort(matrices):
    for i in range(len(matrices) - 1):
        for k in range(len(matrices) - 1):
            if matrices[k].size > matrices[k + 1].size:
                matrices[k], matrices[k + 1] = matrices[k + 1], matrices[k]


def Clear(matrices):
    matrices.clear()


def Multimethods(matrices, ofst):
    ofst.write("Multimethod\n")
    for i in range(len(matrices) - 1):
        for j in range(i, len(matrices)):
            if isinstance(matrices[i], diagonal_matrix):
                ofst.write("Diagonal ")
                if isinstance(matrices[j], diagonal_matrix):
                    ofst.write(" and diagonal matrix\n")
                if isinstance(matrices[j], bin_matrix):
                    ofst.write(" and common matrix\n")
            if isinstance(matrices[i], bin_matrix):
                ofst.write("Common ")
                if isinstance(matrices[j], diagonal_matrix):
                    ofst.write(" and diagonal matrix\n")
                if isinstance(matrices[j], bin_matrix):
                    ofst.write(" and common matrix\n")
            OutMtx(matrices[i], ofst)
            OutMtx(matrices[j], ofst)
