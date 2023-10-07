#文字列型

fruit = 'apple'
print(fruit)
print(type(fruit))
print(fruit * 10) #10回繰り返す

#文字列同士の連結
new_fruit = fruit + 'banana'

#改行を含めた表現
fruits = """apple
banana
grape"""

print(fruits)

fruit = 'banana'
print(fruit[2])
print(fruit[-1]) #一番最後の文字を表示

# encodeとdecode
#encode
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

#decode
str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))


#count
msg = 'ABCDEABC'
print(msg.count('ABC'))
print(msg.count('ABCF'))


#startswith, endswith
print(msg.startswith('AB')) # True or Falseで返ってくる
print(msg.endswith('B'))


#空白の削除　strip(両端), rstrip(右端), lstrip(左端)
msg = ' ABC   '
print(msg.strip())
print(msg.rstrip())
print(msg.lstrip())


#特定の文字の削除
msg = 'ABCDEFABC'
print(msg.strip('C')) #Cだけ除去
print(msg.strip('CBA')) #ABC全部の文字を除去　→ DEFが残る
print(msg.rstrip('C')) #一番右のCだけ除去


# upeer, lower, swapcase, replace, capitalize
msg = 'abcABC'
msg_u = msg.upper()
msg_l = msg.lower()
msg_s = msg.swapcase()
print(msg_u, msg_l, msg_s)

msg = 'ABCDEABC'
msg_r = msg.replace('ABC','FFF',1) #一つ目まで変換
print(msg_r)
msg_r = msg.replace('ABC','FFF',-1) #全部変換
print(msg_r)

msg = 'hello World'
print(msg.capitalize()) #Hello worldになる。


#文字列の一部を取り出し、format、islower、isupper
msg = 'hello, my name is taro'
print(msg[:5])
print(msg[5:])
print(msg[1:5])
print(msg[1:10:2]) #第三引数での指定で2つ飛ばしで値を取得できる。

print('hello {}'.format('taro'))
name = 'Jiro'
print(f'hello {name}') #3.6以上
print(f'{name=}') #3.8以上

msg = 'apple'
print(msg.islower()) #全て小文字だった場合はTrue
print(msg.isupper()) #全て大文字だった場合はTrue


# find, index, rfind, rindex
msg = 'ABCDEABC'
print(msg.find('ABC')) #ABCがどこにあるかインデックスナンバーで返してくれる。
print(msg.rfind('ABC')) #右から検索してくれる。
print(msg.index('ABC')) #findと同じ
print(msg.rindex('ABC')) #rfindと同じ

#ただし、find と index では検索結果が無い時の挙動が違う
print(msg.find('ZZZ')) #検索結果無しの場合は：-1
print(msg.index('ZZZ')) #検索結果無しの場合は：エラー



