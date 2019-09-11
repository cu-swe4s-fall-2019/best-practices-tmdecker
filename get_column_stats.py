import sys
import math
import math_lib


file_name = sys.argv[1]

col_num = int(sys.argv[2])

try:
    f = open(file_name, 'r')
except FileNotFoundError:
    print(file_name, 'not found!')
    sys.exit(2)

V = []

try:
    for l in f:
        A = [int(x) for x in l.split()]
        V.append(A[col_num])
except IndexError:
    print(file_name, 'has less than', col_num, 'columns!')
    sys.exit(2)

f.close()

if len(V) < 1:
    print('no data found in file')
else:
    mean = math_lib.mean(V)

    stdev = math_lib.stdev(V)

    print('mean:', mean)
    print('stdev:', stdev)
