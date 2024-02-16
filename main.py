import random
def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim topa olasizmi?")
    tahminlar = 0
    while True:
        tahminlar += 1
        tahmin = int(input(">>>"))
        if tahmin < tasodifiy_son:
            print("Xato, Men oylagan son bundan kattaroq. Yana harakat qiling.")
        elif tahmin > tasodifiy_son:
            print("Xato, Men oylagan son bundan kichikroq. Yana harakat qiling.")
        else:
            break
    print(f"Tabriklayman siz {tahminlar} ta tahmin bilan topdingiz")
    return tahminlar

def sontop_pc(x=10):
    input(f"1 dan {x} gacha istalgan son o'ylang va istalgan tugmani bosing. Men topaman")
    quyi = 1
    yuqori = x
    tahminlar = 0
    while True:
        tahminlar +=1
        if quyi != yuqori:
            tahmin = random.randint(quyi, yuqori)
        else:
            tahmin = quyi
        javob = input(f"Siz o'ylagan son {tahmin} ga teng, to'g'ri(t)"
                      f"men o'ylagan son bundaan katta(+), yoki kichik (-)")
        if javob == "-":
            yuqori = tahmin-1
        elif javob == "+":
            quyi = tahmin+1
        else:
            break
    print(f"Men {tahminlar} ta tahmin bilan topdim")
    return tahminlar

def play(x=10):
    javob = True
    while javob:
        tahminlar_users = sontop(x)
        tahminlar_pc = sontop_pc(x)
        if tahminlar_users>tahminlar_pc:
            print(f"Men {tahminlar_pc} ta tahmin yutdim!")
        elif tahminlar_users < tahminlar_pc:
            print (f"Siz {tahminlar_users} ta tahmin bilan yutdingiz!")
        else:
            print("Durrang!")
        javob = int(input("Yana o'ynaysizmi?Ha(1)/Yoq(0)"))
print(play())
    