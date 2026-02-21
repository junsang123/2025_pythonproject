print("시작")
weapon_level = 0
upgrade_rates = [{"up": 70, "keep": 30, "down": 0, "break": 0},
                 {"up": 65, "keep": 45, "down": 0, "break": 0}]

while True:
    choice = input('숫자입력/0을 입력 종료/1무기강화: ')
    if choice == '0':
        break
    elif choice == '1':
        import random
        num = random.randint(1, 100)
        rate = upgrade_rates[weapon_level]



