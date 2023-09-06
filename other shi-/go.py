import random
q1 = int(input("kendi şifrenizi girmek mi(1) yoksa güçlü şifre oluşturmak mı?"))
u = "+-/*!&$#?=_@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
if q1 == 1:
    pwd = input("şifreni gir.")
    q = int(input("şifreden emin misiniz? (1=evet 2=hayır)"))
    while q == 2:
        pwd = input("yeni şifre:")
        q = int(input("şifreden emin misiniz? (1=evet 2=hayır)"))
    print("şifre kaydedildi.")
else:
    pwd = ""
    for i in range(10):
        ch = random.choice(u)
        pwd += ch
    print("Şifreniz:", pwd)