
print("시작")
weapon_level = 0
upgrade_rates = [
    {"up": 70, "keep": 30, "down": 0, "break": 0},
    {"up": 60, "keep": 25, "down": 10, "break": 5},
    {"up": 50, "keep": 30, "down": 15, "break": 5},
    {"up": 45, "keep": 30, "down": 20, "break": 5},
    {"up": 40, "keep": 30, "down": 20, "break": 10},
    {"up": 35, "keep": 30, "down": 25, "break": 10},
    {"up": 30, "keep": 30, "down": 30, "break": 10},
    {"up": 25, "keep": 30, "down": 30, "break": 15},
    {"up": 20, "keep": 30, "down": 30, "break": 20},
    {"up": 15, "keep": 30, "down": 30, "break": 25},
    {"up": 0, "keep": 100, "down": 0, "break": 0}
]
import random
while True:
    choice = input('숫자입력/0을 입력 종료/1무기강화: ')

    if choice == '0':
        break
    elif choice == '1':
        num = random.randint(1, 100)
        rate = upgrade_rates[weapon_level]
        print(weapon_level)
        print(num)
        print(rate)
        if rate['keep'] + rate['down'] + rate['break'] < num <= rate['up'] + rate['keep'] + rate['down'] + rate['break']:
            weapon_level = weapon_level + 1
            print("up")
        elif rate['down'] + rate['break'] < num <= rate['keep'] + rate['down'] + rate['break']:
            print("keep")
        elif rate['break'] < num <= +rate['break'] + rate['down']:
            print("down")
            weapon_level = weapon_level - 1
        elif num <= rate['break']:
            print('qudtls')
            weapon_level = 0
