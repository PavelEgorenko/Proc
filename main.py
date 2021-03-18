from container import *

ifst = open("input.txt").read().split("\n")
ofst = open("output.txt", "w")

print("Start.")
matrices = []
InData(matrices, ifst)
ofst.write("Filled container.\n")
OutData(matrices, ofst)
Clear(matrices)
ofst.write("Empty container.\n")
OutData(matrices, ofst)
print("Stop")
ofst.close()