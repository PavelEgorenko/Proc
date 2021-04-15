from unittest import TestCase
from container import *
from matrices import *
from binary_matix import *
from diagonal_matrix import *
from triangle_matrix import *


class Test_triangle_matrix(TestCase):
    def test_in_tri(self):
        cont = []
        nm = triangle_matrix()
        line = "1 1 2 23"
        InTri(nm, cont, line)
        self.assertEqual(cont[0].mtx, "1 0 \n2 23")
        self.assertEqual(cont[0].key, "1")

    def test_out_tri(self):
        nm = triangle_matrix()
        nm.mtx = "233"
        nm.size = 2
        nm.key = 1
        nm.sumelems = 57
        ofsttest = open("testtriout.txt").read()
        ofst = open("tests.txt", "w")
        OutTri(nm, ofst)
        ofst.close()
        ofst1 = open("tests.txt").read()
        self.assertEqual(ofst1, ofsttest)

    def test_sum_elements(self):
        nm = triangle_matrix()
        nm.mtx = "23 0 \n111 13"
        self.assertEqual(sum_of_elements(nm), 147)


class Test_binar_matrix(TestCase):
    def test_in_bin(self):
        cont = []
        nm = bin_matrix()
        line = "1 1 2 23 32"
        InBin(nm, cont, line)
        self.assertEqual(cont[0].mtx, "1 2 \n23 32")
        self.assertEqual(cont[0].key, "1")

    def test_out_bin(self):
        nm = bin_matrix()
        nm.mtx = "233"
        nm.size = 2
        nm.key = 1
        nm.sumelems = 57
        ofsttest = open("testbinout.txt").read()
        ofst = open("tests.txt", "w")
        OutBin(nm, ofst)
        ofst.close()
        ofst1 = open("tests.txt").read()
        self.assertEqual(ofst1, ofsttest)

    def test_sum_elements(self):
        nm = triangle_matrix()
        nm.mtx = "23 2 \n111 13"
        self.assertEqual(sum_of_elements(nm), 149)


class Test_diag_matrix(TestCase):
    def test_in_diag(self):
        cont = []
        nm = diagonal_matrix()
        line = "1 1 32"
        InDiag(nm, cont, line)
        self.assertEqual(cont[0].mtx, "1 0 \n0 32")
        self.assertEqual(cont[0].key, "1")

    def test_out_diag(self):
        nm = diagonal_matrix()
        nm.mtx = "233"
        nm.size = 2
        nm.key = 1
        ofsttest = open("testdiagout.txt").read()
        ofst = open("tests.txt", "w")
        OutDiag(nm, ofst)
        ofst.close()
        ofst1 = open("tests.txt").read()
        self.assertEqual(ofst1, ofsttest)

    def test_sum_elements(self):
        nm = diagonal_matrix()
        nm.mtx = "23 0 \n0 13"
        self.assertEqual(sum_of_elements(nm), 36)


class Test_matrices(TestCase):
    def test_Inmtx(self):
        cont = []
        line = ["1 1 2 4 1", "2 3 1", "2 2 43 11 1 2"]
        for lin in line:
            InMtx(cont, lin)
        self.assertEqual(len(cont), 3)

    def test_OutMtx(self):
        nm1 = diagonal_matrix()
        nm1.type = "Diag"
        nm1.mtx = "1"
        nm1.key = "1"
        nm1.size = 1
        nm1.sumelems = 1

        nm2 = triangle_matrix()
        nm2.type = "Tri"
        nm2.mtx = "2"
        nm2.key = "2"
        nm2.size = 1
        nm2.sumelems = 2

        ofsttest = open("testoutmtx.txt").read()
        ofst = open("tests.txt", "w")
        OutMtx(nm1, ofst)
        OutMtx(nm2, ofst)
        ofst.close()
        ofst1 = open("tests.txt").read()
        self.assertEqual(ofst1, ofsttest)


class Test_container(TestCase):
    def test_Indata(self):
        cont = []
        file = ["1 1 2 4 1", "2 3 1", "2 2 43 11 1 2"]
        InData(cont, file)
        self.assertEqual(len(cont), 3)

    def test_OutData(self):
        cont = []
        nm1 = diagonal_matrix()
        nm1.type = "Diag"
        nm1.mtx = "1"
        nm1.key = "1"
        nm1.size = 1
        nm1.sumelems = 1

        nm2 = triangle_matrix()
        nm2.type = "Tri"
        nm2.mtx = "2"
        nm2.key = "2"
        nm2.size = 1
        nm2.sumelems = 2

        cont.append(nm1)
        cont.append(nm2)

        ofsttest = open("testoutdata.txt").read()
        ofst = open("tests.txt", "w")
        OutData(cont, ofst)
        ofst.close()
        ofst1 = open("tests.txt").read()
        self.assertEqual(ofst1, ofsttest)

    def test_OutDataFiltr(self):
        cont = []
        nm1 = diagonal_matrix()
        nm1.type = "Bin"
        nm1.mtx = "1"
        nm1.key = "1"
        nm1.size = 1
        nm1.sumelems = 1

        nm2 = triangle_matrix()
        nm2.type = "Tri"
        nm2.mtx = "2"
        nm2.key = "2"
        nm2.size = 1
        nm2.sumelems = 2

        cont.append(nm1)
        cont.append(nm2)

        ofsttest = open("testoutdatafiltr.txt").read()
        ofst = open("tests.txt", "w")
        OutDataFiltr(cont, ofst)
        ofst.close()
        ofst1 = open("tests.txt").read()
        self.assertEqual(ofst1, ofsttest)

    def test_Sort(self):
        c = []
        ctest = container
        nm1 = bin_matrix()
        nm1.mtx = "1"
        nm2 = triangle_matrix()
        nm2.mtx = "2"
        nm3 = triangle_matrix()
        nm3.mtx = "1"
        nm4 = bin_matrix()
        nm4.mtx = "1"
        c.append(nm1)
        c.append(nm2)
        c.append(nm3)
        c.append(nm4)
        Sort(c)
        ctest.matrices.append(nm1)
        ctest.matrices.append(nm3)
        ctest.matrices.append(nm4)
        ctest.matrices.append(nm2)
        self.assertEqual(c, ctest.matrices)

    def test_Clear(self):
        c = []
        nm1 = triangle_matrix()
        nm2 = bin_matrix()
        nm3 = diagonal_matrix()
        c.append(nm1)
        c.append(nm2)
        c.append(nm3)
        Clear(c)
        self.assertEqual(len(c), 0)
