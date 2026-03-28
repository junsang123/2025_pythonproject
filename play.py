import random

a = random.randint(1, 100)

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
import time

def t():
    while True:
        s = time.time()
        input()
        e=time.time()
        a = e - s
        if 9.7<=a<=10.3:
            print("성공")
            break
        else:
            print("실패")

print("택1or2")
while True:



