from container import *

ifst = open("input.txt").read().split("\n")
ofst = open("output.txt", "w")
ofst_filtr = open("output1.txt", "w")

print("Start.")
c = container()
InData(c.matrices, ifst)
ofst.write("Filled container.\n")
Sort(c.matrices)
OutData(c.matrices, ofst)
OutDataFiltr(c.matrices, ofst_filtr)
Clear(c.matrices)
ofst.write("Empty container.\n")
OutData(c.matrices, ofst)
print("Stop")
ofst.close()