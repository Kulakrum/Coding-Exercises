import sys

sys.argv[0]
sys.argv


def longest():
    
    n = len(sys.argv)

    if n == 2:
        print('The longest word is {}'.format(sys.argv[1]))
    else:
        longest = max (sys.argv[1], key=len)
        print('The longest word is {}'.format(longest))

  
longest()
