#Fonksiyonlar 2
def ortalama(ders_sayisi):
    toplam = 0
    for i in range(ders_sayisi):
        print("Lutfen ders",i+1,"için not giriniz:")
        a=int(input())
        toplam = toplam + a
    sonuc = toplam / ders_sayisi
    return belge(sonuc)
    
def belge(ort):
    print("Ortalamaniz:",ort)
    if ort >= 70 and ort < 85:
        print("Tebrikler Tesekkür belgesi almaya hak kazandiniz.")
    elif ort >= 85:
        print("Tebrikler Takdir belgesi almaya hak kazandiniz.")
    else:
        print("Maalesef hicbir belge alma hakkiniz yoktur.")

ders_sayisi = int(input("Aldiginiz ders sayisini giriniz: "))
ortalama(ders_sayisi)
