import sys
import math
import math_lib

file_name = sys.argv[1]
col_num = int(sys.argv[2])

f = open(file_name, 'r')

V = []


for l in f:
    A = [int(x) for x in l.split()]
    V.append(A[col_num])

f.close()

if len(V) < 1:
    print('no data found in file')
else:
    mean = math_lib.mean(V)

    stdev = math_lib.stdev(V)

    print('mean:', mean)
    print('stdev:', stdev)
