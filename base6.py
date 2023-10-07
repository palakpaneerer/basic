#複素数 実数と虚数を含む数
#ex. 3+2j は実数が3で虚数が2
#complex(3,2)でも同じ結果が得られる。

a = 1 + 3j
b = 3 + 5j
print(a, b)

#計算
print(a + b)
print(a * b)

#complex関数での表現
c = complex(1,3)
d = complex(3,5)
print(c,d)

#実数部分、虚数部分だけの抽出
print(a.real) #float型で返される
print(a.imag) #float型で返される


