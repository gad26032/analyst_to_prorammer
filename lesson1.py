print(2)
2
print('dsfsdfd')
dsfsdfd
print('Вы получили прибыль ' + 2)
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
TypeError: Can
't convert '
int
' object to str implicitly
print('Вы получили прибыль ' + str(2))
Вы
получили
прибыль
2
a = 2
print('Вы получили прибыль ' + a)
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
TypeError: Can
't convert '
int
' object to str implicitly
print('Вы получили прибыль ' + 'a')
Вы
получили
прибыль
a
print('Вы получили прибыль ' + str(a))
Вы
получили
прибыль
2
s = 'Привет всем'
s[0]
'П'
s[1]
'р'
s[-1]
'м'
s[0:6]
'Привет'
s[-4:]
'всем'
s[0:6] + 'вам ' + s[-4:]
'Приветвам всем'
s[0:6] + ' вам ' + s[-4:]
'Привет вам всем'
s[:]
'Привет всем'
'{} получил прибыль {}, ваши расходы {}'.format('Виталя', 100, 200)
'Виталя получил прибыль 100, ваши расходы 200'
3 / 2
1.5
3 + 3.5
6.5
s
'Привет всем'
s[0] = 'g'
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
TypeError: 'str'
object
does
not support
item
assignment
l = []
l
[]
l = list()
l = list(1)
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
TypeError: 'int'
object is not iterable
l = list(s)
l
['П', 'р', 'и', 'в', 'е', 'т', ' ', 'в', 'с', 'е', 'м']
l = [1, 'sdsssd', [1, 2, 3], {'s': 1}]
l = [1, 2, 3, 4, 5]
l
[1, 2, 3, 4, 5]
l[3] = 'sdkjfhsdkf'
l
[1, 2, 3, 'sdkjfhsdkf', 5]
l[2]
3
l[:2]
[1, 2]
s
'Привет всем'
'dctv' in s
False
'всем' in s
True
1 in l
True
l
[1, 2, 3, 'sdkjfhsdkf', 5]
8 > 'adaasdd'
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
TypeError: unorderable
types: int() > str()
8 > l
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
TypeError: unorderable
types: int() > list()
'asass' == 'asdasda'
False
l.append('asdsdasd')
l
[1, 2, 3, 'sdkjfhsdkf', 5, 'asdsdasd']
l.pop()
'asdsdasd'
l
[1, 2, 3, 'sdkjfhsdkf', 5]
l.insert(1, '3434')
l
[1, '3434', 2, 3, 'sdkjfhsdkf', 5]
l.index(2)
2
l
[1, '3434', 2, 3, 'sdkjfhsdkf', 5]
l.index(1)
0
l.index('asdasdasds')
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
ValueError: 'asdasdasds' is not in list
d = dict()
d
{}
type(d)
<

class 'dict'>


d['Name'] = 'Olga'
d
{'Name': 'Olga'}
d['Name']
'Olga'
d[1] = 'sddsd'
d
{1: 'sddsd', 'Name': 'Olga'}
d['1'] = 'sddsd'
d
{1: 'sddsd', '1': 'sddsd', 'Name': 'Olga'}
names = ['olga', 'Vasya', 'Petya']
names = ['olga', 'Vasya', 'Petya']
age = [22, 23, 24]
users = [
    {'name': "olga", 'age': 22}, {'name': "vasya", 'age': 23}, {'name': "petya", 'age': 24},
]
u
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
NameError: name
'u' is not defined
users
[{'age': 22, 'name': 'olga'}, {'age': 23, 'name': 'vasya'}, {'age': 24, 'name': 'petya'}]
for i in users:
    print(i['name'])
    print(i['age'])

olga
22
vasya
23
petya
24
for i in users:
    if i['age'] == 22:
        print(i['name'])

olga
d
{1: 'sddsd', '1': 'sddsd', 'Name': 'Olga'}
d[1] = '222'
d
{1: '222', '1': 'sddsd', 'Name': 'Olga'}
d[1] = 'erer'
d
{1: 'erer', '1': 'sddsd', 'Name': 'Olga'}
d[0]
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
KeyError: 0
d.keys()
dict_keys([1, '1', 'Name'])
2 == 2
True
True == []
False
False == []
False
se = set()
se
set()
se.update(1)
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
TypeError: 'int'
object is not iterable
se.update([1, 2])
se
{1, 2}
se.update([1, 2])
se
{1, 2}
se2 = {2, 3}
se & se2
{2}
se2 = {'2 ', '2'}
se2
{'2', '2 '}
se.update(['1', '2'])
se & se2
{'2'}
dict(1, 2)
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
TypeError: dict
expected
at
most
1
arguments, got
2
dict(1 = 2)
File
"<input>", line
1
SyntaxError: keyword
can
't be an expression
{1: 2} == {1: 2}
True
