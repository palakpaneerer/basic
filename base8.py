#数値型、文字列型の変換
#str(), int(), float()
#文字列(str)+文字列(str)で連結できる。

#int→strに変換
int_num = 12
str_num = str(int_num)
print(type(str_num))

#float→strに変換
float_num = -20.5
str_num = str(float_num)
print(type(str_num))

#str→int, floatに変換
msg = 12.5
int_msg = int(msg) #小数点以下は切り捨て
float_msg = float(msg)

print('value = {}, type = {}'.format(int_msg, type(int_msg)))
print('value = {}, type = {}'.format(float_msg, type(float_msg)))




