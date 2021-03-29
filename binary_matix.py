class bin_matrix:
    OutputType = ["None", "line by line", "one dimensional array"]
    type = "Bin"
    size = 0
    mtx = ""
    key = 1


def InBin(nm, matrices, line):
    mtx1 = line.split(" ")
    countlines = int(len(mtx1) ** 0.5)
    nm.size = countlines
    nm.key = mtx1.pop(0)

    for i in range(0, len(mtx1), countlines):
        mtx2 = ""
        for k in range(countlines):
            mtx2 += (mtx1[i + k]) + " "
        nm.mtx += mtx2 + "\n"
    nm.mtx = nm.mtx[:-2]
    matrices.append(nm)


def OutBin(struct, ofst):
    ofst.write("Common two-dimensional array:\n")
    if struct.key == "2":
        struct.mtx = struct.mtx.replace("\n", "")
    ofst.write("Output Type = " + struct.OutputType[int(struct.key)] + "\n")
    ofst.write("Size = " + str(struct.size) + "\n")
    ofst.write(struct.mtx + "\n")
