import sys

sys.argv[0]
sys.argv[1]
sys.argv[2]
sys.argv[3]
sys.argv[4]

def change():
    quarters= int(sys.argv[1]) * 0.25
    dimes=int(sys.argv[2]) * 0.1
    nickel=int(sys.argv[3]) * 0.05
    pennies=int(sys.argv[4]) * 0.01

    total_change = quarters+dimes+nickel+pennies

    print('The total value of your change is $%.2f' %(total_change))
    #return change()

change()

