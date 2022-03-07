import sys

sys.argv[0]
sys.argv[1]


def mintosec():
    minutes = int(sys.argv[1])
    seconds = minutes * 60
    print(f"{seconds}")

mintosec()