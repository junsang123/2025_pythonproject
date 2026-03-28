
print("시작")

weapon_level = 0
boss_name=['슬라임','고블린','오크','바보','멍청이','감세감','몬스터','크리쳐','무서운놈','조준상','ㄹㅇ짱짱쎈드레곤']
boss_level=0
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
def w(weapon_level,upgrade_rates):
    num = random.randint(1, 100)
    rate = upgrade_rates[0]
    print(weapon_level)

    if rate['keep'] + rate['down'] + rate['break'] < num <= rate['up'] + rate['keep'] + rate['down'] + rate['break']:
        weapon_level = weapon_level + 1
        print("up")
    elif rate['down'] + rate['break'] < num <= rate['keep'] + rate['down'] + rate['break']:
        print("keep")
    elif rate['break'] < num <= +rate['break'] + rate['down']:
        print("down")

    elif num <= rate['break']:
        print('qudtls')
        weapon_level = 0

    return weapon_level
def b(boss_level,boss_name):
    current_boss = boss_name[boss_level]
    print(current_boss)
    level_diff = weapon_level - boss_level
    if level_diff <= -3:
        winrate = 0
    elif level_diff == -2:
        winrate = 20
    elif level_diff == -1:
        winrate = 30
    elif level_diff == 0:
        winrate = 50
    elif level_diff == 1:
        winrate = 70
    elif level_diff == 2:
        winrate = 90
    elif level_diff == 3:
        winrate = 100
    c = random.randint(0, 99)
    if c < winrate:
        print("win")
        boss_level = boss_level + 1
    else:
        print("접어라")
    if boss_level == 11:
        print('i')
    return boss_level

while True:
    choice = input('숫자입력/0을 입력 종료/1무기강화/2보스: ')

    if choice == '0':
        break
    elif choice == '1':
        weapon_level = w(weapon_level, upgrade_rates)


    elif choice == '2':
        boss_level = b(boss_level, boss_name)
