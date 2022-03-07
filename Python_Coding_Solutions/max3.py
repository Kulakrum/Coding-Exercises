import sys

sys.argv[0]
sys.argv[1]
sys.argv[2]
sys.argv[3]

def max3():
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    z = int(sys.argv[3])

    if x > y > z:
        print ('%.0f' % x)
        
    elif y > x > z:
        print ('%.0f' % y)
        
    elif z > y > x:
        print ('%.0f' % z)

max3()