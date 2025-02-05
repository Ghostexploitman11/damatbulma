import random
import time
import sys


isim = input("İsminizi giriniz: ")


dosya_yolu = "/root/Desktop/damatbulma/isimler.txt"


with open(dosya_yolu, 'r', encoding='utf-8') as file:
    isimler = file.readlines()


isimler = [isim.strip() for isim in isimler]


rastgele_isim = random.choice(isimler)

print(isim + " " + "hanım için damat aranıyor", end="", flush=True)


for _ in range(30):
    print(".", end="", flush=True)
    time.sleep(1)  # 1 saniye bekle


print("\n" + isim + " " + "hanım için damat bulundu: " + rastgele_isim)
