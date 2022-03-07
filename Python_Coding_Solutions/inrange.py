import sys

sys.argv[0]
sys.argv[1]

def inrange():
    x = int(sys.argv[1])
    
    for i in range(5000,8000):
        if i % x == 0:
            if i % (x+4) == 0:
                #print ("[i]")
                print (*[f"{i}"],sep=',')

inrange()   