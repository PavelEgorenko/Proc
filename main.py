from container import *

ifst = open("input.txt").read().split("\n")
ofst = open("output.txt", "w")
ofst2 = open("output2.txt", "w")


print("Start.")
c = container()
InData(c.matrices, ifst)
ofst.write("Filled container.\n")
Multimethods(c.matrices, ofst2)
Sort(c.matrices)
OutData(c.matrices, ofst)
Clear(c.matrices)
ofst.write("Empty container.\n")
OutData(c.matrices, ofst)
print("Stop")
ofst.close()