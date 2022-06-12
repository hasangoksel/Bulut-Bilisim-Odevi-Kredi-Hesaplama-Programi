import krediKontrol
import krediListele

nameSurname = input("Adınız, Soyadınız: ")
print(f"Sayın {nameSurname}, YBS Bank'a Hoşgeldiniz")

programDevam = 1

while programDevam == 1:
    miktar=int(input("İstediğiniz kredi tutarı: "))
    krediListele.Listele()
    krediTuru=int(input("Kredi türü seçiniz(1-6): "))
    vade=int(input("Vade süresi: "))
    krediNotu = float(input("Kredi notunuzu giriniz: "))
    hesapla=krediKontrol.krediKontrol(krediNotu,krediTuru,miktar,vade)
    if(krediTuru == 1):
        krediKontrol.krediKontrol.ihtiyacKredisi(hesapla)
    elif(krediTuru == 2):
        krediKontrol.krediKontrol.tasitKredisi(hesapla)
    elif(krediTuru == 3):
        krediKontrol.krediKontrol.konutKredisi(hesapla)
    elif(krediTuru == 4):
        krediKontrol.krediKontrol.dugunKredisi(hesapla)
    elif(krediTuru == 5):
        krediKontrol.krediKontrol.esnafKredisi(hesapla)
    elif(krediTuru == 6):
        krediKontrol.krediKontrol.ogrenciKredisi(hesapla)
    else:
        print("Geçerli bir kredi türü seçmediniz.")    
    programDevam=int(input("Başa dönmek istiyor musunuz [1(Evet)/2(Hayır)]: "))
    if (programDevam==2):
        break        
    