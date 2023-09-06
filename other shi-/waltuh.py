import random
u = "+-/*!&$#?=_@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

print("GOOGLE GÜÇLÜ ŞİFRE OLUŞTURUCU 9000")
le = int(input("ŞİFRE KAÇ KARAKTERLİ OLSUN????(EN AZ 10)"))
while le < 10:
    print("EN AZ 10 DEDİK KARDEŞ")
    le = int(input("ŞİFRE KAÇ KARAKTERLİ OLSUN????(EN AZ 10)"))
p = ""

for i in range(le):
    p += random.choice(u)
print("ULTRA SÜPER MEGA HİPER ÇOK ÇOK ÇOK AŞIRI ÇOK FENA FENA GÜVENLİ ŞİFRENİZ HAZIR.")
print("ŞİFREN:", p)
