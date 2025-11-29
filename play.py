import random

a = random.randint(1, 100)
90

def down():
    while True:
        b = int(input("입력"))
        if b < a:
            print("s")
        else:
            if b > a:
                print("d")
            elif b == a:
                break
down()


