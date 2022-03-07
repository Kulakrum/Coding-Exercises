import sys

sys.argv[0]
sys.argv[1]

def capCount():
    
    letters = str(sys.argv[1])
    count = 0
    for i in letters:
        if i.isupper():
            count=count+1
    print(count)

capCount()