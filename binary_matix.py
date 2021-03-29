class bin_matrix:
    OutputType = ["None", "line by line", "one dimensional array"]
    type = "Bin"
    size = 0
    mtx = ""
    sumelems = 0
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
    sum_of_elements(nm)
    matrices.append(nm)


def OutBin(struct, ofst):
    ofst.write("Common two-dimensional array:\n")
    if struct.key == "2":
        struct.mtx = struct.mtx.replace("\n", "")
    ofst.write("Output Type = " + struct.OutputType[int(struct.key)] + "\n")
    ofst.write("Size = " + str(struct.size) + "\n")
    ofst.write("Sum of elements = " + str(struct.sumelems) + "\n")
    ofst.write(struct.mtx + "\n")


def sum_of_elements(nm):
    lst = nm.mtx.replace("\n", "").split(" ")
    for i in lst:
        nm.sumelems += int(i)
