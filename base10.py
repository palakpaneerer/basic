#辞書型　｛キー：バリュー｝

car = {'brand':'Toyota', 'model': 'Prius', 'year':2015}

print(car['brand'])
# print(car['bran']) #キーに存在しなかったらエラーが返される。つまり以後の処理は実行されない。
print(car.get('bran','does not exist')) #キーに存在しなかったら第二引数が返される。
print(car.get(1)) #第二引数を設定していなかったらNoneが返される。

#辞書型内の値の抽出
print(car.keys()) #キー一覧
print(car.values()) #バリュー一覧
print(car.items()) #キー+バリュー一覧

#よく使う構文
#キーとバリューを夫々取り出す文
for k, v in car.items():
    print('key={}, value={}'.format(k,v))

#辞書のキーに'brand'があれば、以下のコードを実行
if 'brand' in car:
    print('carのブランドは{}'.format(car['brand']))

