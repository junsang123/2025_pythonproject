
x=3
print(x)

x=3==5
print(x)

x=[1,2,3,4,5]#list
print(x)
print(x[0])
x=x*2
print('x*2:',x)
print(x[2:4])
x.append(7)
print(x)
x.insert(1,4)
print(x)
x.remove(1)
print(x)
x[0]=3
print(x)
print(len(x))
print(len(x)-1)
x={'a':1,'b':2}#dictionary
print(x['a'])
example = {
    'python': [True, False, True, True, True, True, True, False, False, True],
}
print(example)
print(example['python'][2])

python_description = [
    {
        'answer': 1,
        'description': 'python에 대한 설명은 1번이 맞습니다.'
    },
    {
        'answer': "list",
        'description': 'python의 열거형 데이터 타입은 list입니다.'
    },
    {
        'answer': True,
        'description': 'python의 LIST 안에 Dictionary를 사용할 수 있습니다.'
    },
]

list_example = [1, "+", 2, "="]
print(python_description[0])
