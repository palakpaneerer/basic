# 数値型 (int, Float)

value = 9
print(value+1) #10が返される

print(value/3) #3.0とfloat型が返される。

print(value//4) #小数点切り捨てのint型で返される。


value += 3 #valueに3を加算して12になる。
print(value)

print(value **2) #べき乗

#float型
height = 175.5
print(type(height))
print(height + 10) # float型

#シフト演算
value = 8 #8は2進数だと1000
print(value >> 2) #1000が0010と右にシフトされる。なので、0010を10進数に直すと2。
print(value << 3) #1000が1000000と左にシフトされる。なので、10進数に直すと64。

#ビット計算（&,|） |はパイプと読む
print(12 & 21) #01100 and 10101 → 00100 → 4 論理和は値が一致したケタは1、異なる場合は0。
print(12 | 21) #                → 11011 → 29

#以下でも上記と同じ結果を表現できる。
value = 12
value &= 21
print(value)
