import sys

sys.argv[0]
sys.argv[1]


def temp():
    Celsius = float(sys.argv[1])
    Fahrenheit = (9/5*Celsius + 32)
    print ("The temperature is %.2f degrees Fahrenheit." %(Fahrenheit))

temp()