class krediKontrol(object):
    def __init__(self,krediNotu,krediTuru,miktar,vade ):
        self.krediNotu = krediNotu
        self.krediTuru = krediTuru
        self.miktar = miktar
        self.vade = vade
    
    def ihtiyacKredisi(self):
        faizOrani = 1.89
        if(self.krediNotu >= 1.2 and self.krediNotu <= 10):
            if(self.vade >= 1 and self.vade <= 36):
                if(self.miktar >= 1000 and self.miktar <= 50000):
                    bankaKazanci= self.miktar * (faizOrani/100) * self.vade
                    toplamGeriOdeme= self.miktar + bankaKazanci
                    aylikOdeme = toplamGeriOdeme / self.vade
                    print(f"Kredi Tutarı: {self.miktar}\nVade: {self.vade}\nAylık Ödeme: {aylikOdeme} ₺\nToplam Geri Ödeme: {toplamGeriOdeme} ₺\n")
                else:
                    print("İhtiyaç Kredisi Kredi Tutarı Minimum 1000₺ - Maksimum 50.000₺")
            else:
                print("İhtiyaç Kredisi Vade Süresi Minimum 1 Ay - Maksimum 36 Ay")
        else:
            print("İhtiyaç Kredisi Gerekli Puan Minimum 1.2 !")
    
    def tasitKredisi (self):
        faizOrani = 1.72
        if(self.krediNotu >= 2 and self.krediNotu <= 10):
            if(self.vade >= 24 and self.vade <= 60):
                if(self.miktar >= 40000 and self.miktar <= 124000):
                    bankaKazanci= self.miktar * (faizOrani/100) * self.vade
                    toplamGeriOdeme= self.miktar + bankaKazanci
                    aylikOdeme = toplamGeriOdeme / self.vade
                    print(f"Kredi Tutarı: {self.miktar}\nVade: {self.vade}\nAylık Ödeme: {aylikOdeme} ₺\nToplam Geri Ödeme: {toplamGeriOdeme} ₺\n")
                else:
                    print("Taşıt Kredisi Kredi Tutarı Minimum 40.000₺ - Maksimum 124.000₺")
            else:
                print("Taşıt Kredisi Vade Süresi Minimum 24 Ay - Maksimum 60 Ay")
        else:
            print("Taşıt Kredisi Gerekli Puan Minimum 2 !")
            
    def konutKredisi (self):
        faizOrani = 1.24
        if(self.krediNotu >= 3 and self.krediNotu <= 10):
            if(self.vade >= 36 and self.vade <= 120):
                if(self.miktar >= 100000 and self.miktar <= 350000):
                    bankaKazanci= self.miktar * (faizOrani/100) * self.vade
                    toplamGeriOdeme= self.miktar + bankaKazanci
                    aylikOdeme = toplamGeriOdeme / self.vade
                    print(f"Kredi Tutarı: {self.miktar}\nVade: {self.vade}\nAylık Ödeme: {aylikOdeme} ₺\nToplam Geri Ödeme: {toplamGeriOdeme} ₺\n")
                else:
                    print("Konut Kredisi Kredi Tutarı Minimum 100.000₺ - Maksimum 350.000₺")
            else:
                print("Konut Kredisi Vade Süresi Minimum 36 Ay - Maksimum 120 Ay")
        else:
            print("Konut Kredisi Gerekli Puan Minimum 3 !")
            
    def dugunKredisi (self):
        faizOrani = 1.78
        if(self.krediNotu >= 1.8 and self.krediNotu <= 10):
            if(self.vade >= 12 and self.vade <= 60):
                if(self.miktar >= 50000 and self.miktar <= 350000):
                    bankaKazanci= self.miktar * (faizOrani/100) * self.vade
                    toplamGeriOdeme= self.miktar + bankaKazanci
                    aylikOdeme = toplamGeriOdeme / self.vade
                    print(f"Kredi Tutarı: {self.miktar}\nVade: {self.vade}\nAylık Ödeme: {aylikOdeme} ₺\nToplam Geri Ödeme: {toplamGeriOdeme} ₺\n")
                else:
                    print("Düğün Kredisi Kredi Tutarı Minimum 50.000₺ - Maksimum 350.000₺")
            else:
                print("Düğün Kredisi Vade Süresi Minimum 12 Ay - Maksimum 60 Ay")
        else:
            print("Düğün Kredisi Gerekli Puan Minimum 1.8 !")
                        
    def esnafKredisi (self):
        faizOrani = 1.95
        if(self.krediNotu >= 2 and self.krediNotu <= 10):
            if(self.vade >= 12 and self.vade <= 60):
                if(self.miktar >= 50000 and self.miktar <= 350000):
                    bankaKazanci= self.miktar * (faizOrani/100) * self.vade
                    toplamGeriOdeme= self.miktar + bankaKazanci
                    aylikOdeme = toplamGeriOdeme / self.vade
                    print(f"Kredi Tutarı: {self.miktar}\nVade: {self.vade}\nAylık Ödeme: {aylikOdeme} ₺\nToplam Geri Ödeme: {toplamGeriOdeme} ₺\n")
                else:
                    print("Esnaf Kredisi Kredi Tutarı Minimum 50.000₺ - Maksimum 350.000₺")
            else:
                print("Esnaf Kredisi Vade Süresi Minimum 12 Ay - Maksimum 60 Ay")
        else:
            print("Esnaf Kredisi Gerekli Puan Minimum 2 !")
    
    def ogrenciKredisi (self):
        faizOrani = 1.15
        if(self.krediNotu >= 1.6 and self.krediNotu <= 10):
            if(self.vade >= 1 and self.vade <= 12):
                if(self.miktar >= 1000 and self.miktar <= 5000):
                    bankaKazanci= self.miktar * (faizOrani/100) * self.vade
                    toplamGeriOdeme= self.miktar + bankaKazanci
                    aylikOdeme = toplamGeriOdeme / self.vade
                    print(f"Kredi Tutarı: {self.miktar}\nVade: {self.vade}\nAylık Ödeme: {aylikOdeme} ₺\nToplam Geri Ödeme: {toplamGeriOdeme} ₺\n")
                else:
                    print("Öğrenci Kredisi Kredi Tutarı Minimum 1000₺ - Maksimum 5000₺")
            else:
                print("Öğrenci Kredisi Vade Süresi Minimum 1 Ay - Maksimum 12 Ay")
        else:
            print("Öğrenci Kredisi Gerekli Puan Minimum 1.6 !")
                           
        
        