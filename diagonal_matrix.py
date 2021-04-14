class diagonal_matrix:
    OutputType = ["None", "line by line", "one dimensional array"]
    type = "Diag"
    size = 0
    mtx = ""
    sumelems = 0
    key = 1


def InDiag(nm, matrices, line):
    mtx1 = line.split(" ")
    for i in mtx1:
        if not i.isdigit():
            print("В диагональной матрице содержаться не только числа, ошибка в", len(matrices) + 1, "строке")
            exit()
    nm.size = len(mtx1)
    nm.key = mtx1.pop(0)
    if nm.key != "1" and nm.key != "2":
        print("Неверно введен тип вывода данных в диагональной матрице, ошибка в", len(matrices) + 1, "строке")
        exit()

    for i in mtx1:
        mtx2 = ""
        for k in range(len(mtx1)):
            if i == mtx1[k]:
                mtx2 += (i + " ")
            else:
                mtx2 += ("0" + " ")
        nm.mtx += mtx2 + "\n"
    nm.mtx = nm.mtx[:-2]
    sum_of_elements(nm)
    matrices.append(nm)


def OutDiag(struct, ofst):
    ofst.write("Diagonal two-dimensional array:\n")
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
