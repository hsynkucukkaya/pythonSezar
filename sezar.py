alfabe= ['a','b','c','ç','d','e','f','g','ğ','h','i','ı','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']
ekle = []
mesaj = input("Mesaj Giriniz :")
metin = ""

key = int(input("Ofset Giriniz :"))

for i in range(0,len(mesaj)):
    if(mesaj[i] in alfabe):
        uzunluk = alfabe.index(mesaj[i]) + key
        mod = uzunluk % 29
        ekle.append(alfabe[mod])
    else:
        ekle.append(" ")

for i in range(0,len(ekle)):
    if(ekle[i] in alfabe):
        metin = metin + ekle[i]
    else:
        metin = metin + " "

print(metin)