import sys

sys.argv[0]
sys.argv[1]
sys.argv[2]

def username():

    first_name = sys.argv[1]
    first_char = first_name[0]
    last_name = sys.argv[2]
    last_char = last_name[-7:]
    total_char = str(len(first_name)+ len(last_name))
    print('Your username is %s' %first_char.lower()+last_char.lower()+total_char)

username()