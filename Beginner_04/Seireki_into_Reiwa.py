import random

for i in range(50):
    hit = random.randint(3,6)
    if hit < 6:
        print(str(hit) + "のダメージ")
    else: #クリティカルヒット
        print("クリティカルヒットで、20ダメージ！")



#他の文言バージョン

import random

for i in range(50):
    hit = random.randint(3,6)
    if hit < 6:
        print("スライムに" + str(hit) + "のダメージを与えた！")
    else: #クリティカルヒット
        print("クリティカルヒット！スライムに20ダメージ！")