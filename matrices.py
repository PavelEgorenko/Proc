from diagonal_matrix import *
from binary_matix import *


def InMtx(matrices, line):
    if line[0] == "1":
        line = line[2:]
        nm = diagonal_matrix()
        InDiag(nm, matrices, line)
    elif line[0] == "2":
        line = line[2:]
        nm = bin_matrix()
        InBin(nm, matrices, line)


def OutMtx(struct, ofst):
    if struct.type == "Diag":
        OutDiag(struct, ofst)
    elif struct.type == "Bin":
        OutBin(struct, ofst)