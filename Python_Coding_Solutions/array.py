import sys
import numpy

sys.argv[0]
sys.argv[1]
sys.argv[2]
sys.argv[3]
sys.argv[4]

def array():
    
    a = numpy.array([sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]])
    sum = int(sys.argv[1])+int(sys.argv[2])+int(sys.argv[3])+int(sys.argv[4])

    print('%s'%type(a))
    print('%.0f'%sum)

array()