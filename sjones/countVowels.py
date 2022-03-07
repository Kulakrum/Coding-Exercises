import sys

sys.argv[0]
sys.argv[1]

def countVowels():
    
    letters = str(sys.argv[1]).lower()
    count = 0
    for char in letters:
        if char in 'aeiou':
            count = count + 1 
    print(count)

countVowels()