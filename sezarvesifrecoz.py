sayac = int(0)
alfabe= ['a','b','c','ç','d','e','f','g','ğ','h','i','ı','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']
ekle = []
mesaj = input("Mesaj Giriniz :")
sifre = input("Şifre Giriniz :")
metin = ""
saydırma = 0
yazdir = ". Ofset"
while sayac<=len(alfabe):
    for i in range(0,len(mesaj)):
        sifremod = i % len(sifre)
        sifrebul = alfabe.index(sifre[sifremod])
        if(mesaj[i] in alfabe):
            bul = alfabe.index(mesaj[i])
            sorgula = bul - sayac - sifrebul
            if(sorgula<0):
                topla = len(alfabe) + bul
                uzunluk = topla - sayac - sifrebul
                mod = uzunluk % 29
                ekle.append(alfabe[mod])
            else:
                uzunluk = alfabe.index(mesaj[i]) - sayac - sifrebul
                mod = uzunluk % 29
                ekle.append(alfabe[mod])
        else:
            ekle.append(" ")
    sayac+=1



for i in range(0,len(ekle)):
    if(ekle[i] in alfabe):
        metin = metin + ekle[i]
    else:
        metin = metin + " "

for i in range(0,len(metin),len(mesaj)):
    print(metin[i:i+len(mesaj)] , saydırma, yazdir)
    saydırma+=1
    

