import sys
import math

sys.argv[0]
sys.argv[1]
sys.argv[2]
sys.argv[3]

def quadratic():
    # Solve the quadratic equation ax**2 + bx + c = 0

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    
    d = (b**2) - (4*a*c)
    if d < 0:
        print ('No solutions')
    else:
        root1 = (-b-math.sqrt(d))/(2*a)
        root2 = (-b+math.sqrt(d))/(2*a)

        print('The solutions are %.2f and %.2f' %(root2,root1))

quadratic()