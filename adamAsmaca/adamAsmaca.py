import random
soruListesi=["BAŞARI","ZAMAN YÖNETİMİ","PYTHON PROGRAMLAMA DİLİ"]

def soruÜret():
    s=random.choice(soruListesi)
    return s

def soruyuDönüştür(soru):
    soruDönüştürülecek=list(soru)
    for i in range(len(soru)):
        if soruDönüştürülecek[i] != " ":
            soruDönüştürülecek[i] = "-"
    return soruDönüştürülecek

def listeyiYazdır(liste):
    print()
    for i in range(len(liste)):
        print(liste[i],end="")
    print()

def tahminDoğruMu(soru):
    tahmin=input("Tahminizi giriniz :")
    listTahmin=list(tahmin)
    if "i" in tahmin:
        for x in range(len(tahmin)):
            if listTahmin[x]=="i":
                listTahmin[x]="İ"
            listTahmin[x]=listTahmin[x].upper()
        listeyiYazdır(listTahmin)
        return listTahmin==list(soru)
    else:
        tahmin=tahmin.upper()
        return tahmin==soru

def girileniKontrolEt(giriş,soru,dönüştürülmüşSoru):
    if giriş in soru:
        for i in range(len(soru)):
            if giriş==soru[i]:
                dönüştürülmüşSoru[i]=giriş
        if list(soru) == dönüştürülmüşSoru:
            print(soru, "\nTebrikler cevabı buldunuz")


    else:
        print("Bu harf soruda bulunmamaktadır")
        global hak
        hak -= 1
        print(hak,"adet hakkınız kalmıştır")

def adminGirişi():
    def soruEkle():
        yeniSoru=input("Eklemek istediğiniz soruyu yazınız.. ")
        soruListesi.append(yeniSoru)
    def soruSil():
        for i in range(len(soruListesi)):
            print(i,soruListesi[i])
        indis=int(input("Silmek istediğiniz sorunun numarasını giriniz.. "))
        del soruListesi[indis]
    while True:
        print(soruListesi)
        print("""
        1- Yeni Soru Ekle
        2- Soru Sil
        3- Çıkış
        Yapmak istediğiniz işlemi seçiniz...  
        """)
        seçim=input()
        if seçim=="1":
            soruEkle()
        elif seçim=="2":
            soruSil()
        elif seçim=="3":
            break
        else:
            print("Hatalı Giriş Yaptınız")

def açılışMesajı():
    print("""
    |-----------------------------------------------------------|
    | Adam Asmaca Oyunumuza Hoşgeldiniz !!                      |
    | Oyundan çıkmak için harf yerine 0 tuşuna basabilirsiniz.  |
    | Oyun esnasında tahmin etmek için 1 tuşuna basabilirsiniz. |
    |      ****  İYİ EĞLENCELER   ****                          |
    |-----------------------------------------------------------|
    """)



def gövde():
    soru=soruÜret()
    dönüştürülmüşSoru=soruyuDönüştür(soru)
    print(soru)
    global hak
    hak=5
    açılışMesajı()
    while list(soru) != dönüştürülmüşSoru:
        if hak==0:
            print("Hakkınız kalmadı")
            print("CEVAP : ",soru)
            break
        listeyiYazdır(dönüştürülmüşSoru)
        giriş=input("Lütfen bir harf giriniz: ")
        if giriş=="gizlişifre":
            adminGirişi()
            continue
        if giriş=="0":
            print("Oyundan çıktınız :( ")
            break
        if giriş=="1":
            if tahminDoğruMu(soru):
                print("Tebrikler, doğru tahmin")
                break
            else:
                print("Yanlış tahmin!")
                hak -= 1
                print(hak,"adet hakkınız kalmıştır")
        else:
            if giriş=="i":
                giriş="İ"
            giriş=giriş.upper()
            girileniKontrolEt(giriş,soru,dönüştürülmüşSoru)
    

while True:
    gövde()
    cevap=input("Tekrar oynamak için herhangi bir tuşa basınız. \nOyundan çıkmak için H tuşuna basınız.")
    if cevap=="h" or cevap=="H":
        break

