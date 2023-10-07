#リスト

list_a = [1,2,3,4]
list_b = []

print(list_a)
print(list_a[0]) #1
print(list_a[-2]) #3

#リストの上書き
list_a = [1,[1,2,'apple'],3,'banana']

print(list_a)
print(list_a[1][2]) #apple

list_a[1][2] = 'lemon'
print(list_a[1][2]) #lemon


#リストのメソッド
#スライス（一部抽出）
list_a = [1,2,3,4,5]
list_b = list_a[:3]
print(list_b)
list_b = list_a[3:]
print(list_b)
list_b = list_a[1:4]
print(list_b)
list_b = list_a[:3:2] #第三引数はステップで1つ飛ばしした。
print(list_b)
list_b = list_a[1:4:2] #第三引数はステップで1つ飛ばしした。
print(list_b)

# append, extend, insert, clear
list_a.append('apple') #値をリストに追加
print(list_a)
list_a.extend(['banana', 'melon']) #リスト同士の連結
print(list_a)
list_a.insert(1, 'grape') #場所を指定した上でのリストへ値追加
print(list_a)
list_a.clear() #リスト内削除
print(list_a)

#remove, pop, count, index
list_a = [0,1,1,1,2,2,3,3,3,4]
list_a.remove(3) #一つ目の3を削除
print(list_a)

value = list_a.pop() #一番最後の値を取り出す
print(list_a, value)

print(list_a.count(0))
print(list_a.count(1))

print(list_a.index(1))


# copy
list_a = [1,2,3,4]
print(list_a)
list_b = list_a
list_b[0] = 'AAA' #参照渡しのため、list_bだけ変えたつもりでもlist_aも変えてしまっている。
print(list_a) 

#上記の問題をcopy()を使って解決できる。
list_a = [1,2,3,4]
print(list_a)
list_b = list_a.copy()
list_b[0] = 'AAA'
print(list_a) 


#sort, reverse
list_a = ['banana', 'apple', 'lemon', 'grape']
print(list_a)
list_a.sort()
list_a = sorted(list_a) #こっちでも同じ表現ができる。
print(list_a)

list_a.reverse()
print(list_a)