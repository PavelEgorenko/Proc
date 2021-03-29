class diagonal_matrix:
    OutputType = ["None", "line by line", "one dimensional array"]
    type = "Diag"
    size = 0
    mtx = ""
    key = 1


def InDiag(nm, matrices, line):
    mtx1 = line.split(" ")
    nm.size = len(mtx1)
    nm.key = mtx1.pop(0)

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
    if struct.key == "2":
        struct.mtx = struct.mtx.replace("\n", "")
    ofst.write("Output Type = " + struct.OutputType[int(struct.key)] + "\n")
    ofst.write("Size = " + str(struct.size) + "\n")
    ofst.write(struct.mtx + "\n")