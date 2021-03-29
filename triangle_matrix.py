class triangle_matrix():
    type = "Tri"
    size = 0
    mtx = ""

def InTri(nm, matrices, line):
    mtx1 = line.split(" ")
    itr = 0
    length = 0
    while length < len(mtx1):
        itr += 1
        length = 0
        for i in range(itr):
            length += i + 1
    nm.size = itr

    for i in range(nm.size):
        for k in range(nm.size):
            if k <= i:
                nm.mtx += mtx1.pop(0) + " "
            else:
                nm.mtx += "0 "
        nm.mtx += "\n"
    nm.mtx = nm.mtx[:-2]
    matrices.append(nm)

def OutTri(struct, ofst):
    ofst.write("Triangle two-dimensional array:\n")
    ofst.write("Size = " + str(struct.size) + "\n")
    ofst.write(struct.mtx + "\n")