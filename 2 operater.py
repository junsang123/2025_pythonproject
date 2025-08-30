x=10
y=15
z=x==y
print('x==y:',z)
z=x!=y
print('x!=y:',z)
z=x>y
print('x>y:',z)
z=x<y
print('x<=y:',z)
z=x+y
print('x+y:',z)
z=x-y
print('x-y:',z)
z=x*y
print('x*y:',z)
z=x/y
print('x/y:',z)
z=x//y
print('x//y : ' , z)
str_x='hello'
str_y='python'

str_z= str_x+str_y
print('str_x+str_y:',str_z)
str_z=str_x*2
print('str_x*2:',str_z)



array_x=[123,1123]
arry_y=[2312,1441]
arry_z=array_x+arry_y
print('array_x+arry_y:',arry_z)
array_z=array_x*2
print('array_x*2:',array_z)
report_card = {
    "국어": 1,
    "수학": 3,
    "영어": 3,
    "물리": 4,
    "화학": 2,
    "생명과학": 5,
}
can_apply=report_card['국어']<3 and report_card['영어']<3 and repot_cord['수학']<3
print('지원가능여부',can_apply)
total=report_card['국어']+report_card['수학']+report_card['영어']<6
a=report_card['물리']==1 or report_card['화학']==1 or report_card['생명과학']==1
print('가능',a)