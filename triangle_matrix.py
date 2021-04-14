class triangle_matrix:
    OutputType = ["None", "line by line", "one dimensional array"]
    type = "Tri"
    size = 0
    mtx = ""
    sumelems = 0
    key = 1


def InTri(nm, matrices, line):
    mtx1 = line.split(" ")
    for i in mtx1:
        if not i.isdigit():
            print("В матрице содержаться не только числа, ошибка в", len(matrices) + 1, "строке")
            exit()
    nm.key = mtx1.pop(0)
    if nm.key != "1" and nm.key != "2":
        print("Неверно введен тип вывода данных в треугольной матрице, ошибка в", len(matrices) + 1, "строке")
        exit()
    itr = 0
    length = 0
    while length < len(mtx1):
        itr += 1
        length = 0
        for i in range(itr):
            length += i + 1
        if length > len(mtx1):
            print("Неверно введено количество элементов в треугольной матрице, ошибка в", len(matrices) + 1, "строке")
            exit()
    nm.size = itr

    for i in range(nm.size):
        for k in range(nm.size):
            if k <= i:
                nm.mtx += mtx1.pop(0) + " "
            else:
                nm.mtx += "0 "
        nm.mtx += "\n"
    nm.mtx = nm.mtx[:-2]
    sum_of_elements(nm)
    matrices.append(nm)


def OutTri(struct, ofst):
    ofst.write("Triangle two-dimensional array:\n")
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
