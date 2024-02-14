import random

def sontop(x=10):
    tasodifiy_son=random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi.")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin= int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato. Men o'ylagan son bundan katta. Yana harakat qiling:")
        elif taxmin>tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichik. Yana harakat qiling:")
        else:
            break
    print(f"Tabriklaymiz, {taxminlar} ta taxmin bilan to'gri topdingiz")
    return taxminlar
# print(sontop())
def  son_top_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar=0
    while True:
        taxminlar +=1
        if yuqori != quyi:
            taxmin= random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonni o'yladingiz: tog'ri(t),"
                      f"men oylagan son bundan kattaroq(+), yoki kichikroq(-)".lower())
        if javob == "+":
            quyi = taxmin+1
        elif javob == "-":
            yuqori=taxmin-1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan to'gri topdim ")
    return taxminlar

def play (x=10):
    while True:
            tahmin_user = sontop(x)
            tahmin_pc = son_top_pc(x)
            if tahmin_pc>tahmin_user:
                print("Siz yutdingiz")
            elif tahmin_pc<tahmin_user:
                print("Men yutdim")
            else:
                print("Durrang!")
            javob = int(input("YAana o'ynaysizmi? Ha(1)/Yoq(0)"))
            if javob == 0:
                break
            elif javob == 1:
                continue
print(play())    