print("新しいパスワードを入力して下さい。")

# input関数で与えられた文字列を取得し、passwordに格納
password = input()

#文字列の長さが6以上かを判定
if len(password) < 6:
    print("6文字より短いパスワードは無効です")
    exit()

numbers = "0123456789"
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

num = False
alpha = False

for i in password:
    if i in alphabet:
        alpha = True
    if i in numbers:
        num = True

if alpha == False or num == False:
    print("無効なパスワードです。数字と英字の両方が必要です。")
    exit()


# 連続しているか数えるための変数
cnt = 1

# 連続しているか数える文字を一時的に入れる変数
tmp = ""

# passwordを１文字ずつ先頭から順に見て、３つ以上連続しているか判定
for i in password:
    # 一致していたらカウントアップ
    if tmp == i:
        cnt += 1
        if cnt >= 3:
            print("３文字連続しているパスワードは無効です。")
            exit()
    else:
        cnt = 1
    tmp = i


# すべての条件を通ったら、有効を出力
print("有効なパスワードです。" + password + " で登録されました")
