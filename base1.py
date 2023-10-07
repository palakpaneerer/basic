#input()関数
name = input('あなたの名前は何ですか？:')
print(name)


#format関数
age = 20
print('My name is {}, 年齢は {}'.format(name, age))


#複数の変数
a = b = 'hello'
print(a, b)


#変数、定数について
#定数：全て大文字で定義する。
KING_OF_ANIMAL = 'lion'


#定数化することで可読性があがる。
LEGAL_AGE = 20
if age < LEGAL_AGE:
    print('未成年')
else:
    print('成人')


#特殊なprint文(fstring文)
print(f'age = {age}')
print(f'{age=}')


#論理型
is_animal=False
if is_animal:
    print('動物です')
    
is_man = True
is_adult = True
#or文
if is_man or is_adult:
    print('男か大人です')


#and文
if is_man and is_adult:
    print('成人男性です')
    
