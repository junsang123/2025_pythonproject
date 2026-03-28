

score=int(input('입력'))

if score > 100 or score <0:
    print("ㄴㄴ")
else:
    if score >= 80:
            print('ㅇ')
    elif score >= 60:
            print("re")
    else:
            print('ㄴ')
#while True:
    #user_input("입력")
    #if user_input.lower()=="z":
       # break

input_number= int(input("입력"))
index=2
while index < input_number:
    print(index)
    index=index+2
