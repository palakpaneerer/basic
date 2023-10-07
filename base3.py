#論理型

#論理型はそのまま条件として使える。
is_animal = False

if is_animal:
    print('動物です')

    
is_man = True
is_adult = True

#or文 どっちかTrueなら実行される
if is_man or is_adult:
    print('男か大人です')


#and文　どっちもTrueなら実行される
if is_man and is_adult:
    print('成人男性です')
    
