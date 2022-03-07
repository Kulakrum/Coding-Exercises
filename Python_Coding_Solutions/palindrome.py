import sys

sys.argv[0]
sys.argv[1]


def palindrome():
    word = sys.argv[1].lower()

    is_palindrome = True

    for letter in word:
        if letter == word[-1]:
            word.pop(-1)
            print('It’s a palindrome!')
        else:
            is_palindrome = False
            print('It’s not a palindrome!')

            break

palindrome()