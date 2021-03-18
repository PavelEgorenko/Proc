class diagonal_matrix:
    type = "Diag"
    size = 0
    mtx = ""


def InDiag(nm, matrices, line):
    mtx1 = line.split(" ")
    nm.size = len(mtx1)

    for i in mtx1:
        mtx2 = ""
        for k in range(len(mtx1)):
            if i == mtx1[k]:
                mtx2 += (i + " ")
            else:
                mtx2 += ("0" + " ")
        nm.mtx += mtx2 + "\n"
    nm.mtx = nm.mtx[:-2]
    matrices.append(nm)

def OutDiag(struct, ofst):
    ofst.write("Diagonal two-dimensional array:\n")
    ofst.write("Size = " + str(struct.size) + "\n")
    ofst.write(struct.mtx + "\n")