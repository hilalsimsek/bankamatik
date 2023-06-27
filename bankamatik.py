#bankamatik

class BankaHesabi:
    def __init__(self, isim, bakiye):
        self.isim = isim
        self.bakiye = bakiye

    def para_cek(self, miktar):
        if self.bakiye >= miktar:
            self.bakiye -= miktar
            print(f"{miktar} TL para çekildi. Yeni bakiye: {self.bakiye} TL")
        else:
            print("Yetersiz bakiye.")

    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f"{miktar} TL para yatırıldı. Yeni bakiye: {self.bakiye} TL")

    def transfer(self, diger_hesap, miktar):
        if self.bakiye >= miktar:
            self.para_cek(miktar)
            diger_hesap.para_yatir(miktar)
        else:
            print("Yetersiz bakiye.")

    def __str__(self):
        return f"{self.isim}: {self.bakiye} TL"


class ATM:
    def __init__(self):
        self.hesaplar = {"1234": BankaHesabi("Hesap 1", 1000),
                         "5678": BankaHesabi("Hesap 2", 2000)}

    def calistir(self):
        sifre = input("Lütfen şifrenizi girin: ")
        if sifre != "1234":
            print("Hatalı şifre.")
            return

        while True:
            print("1- Bakiye sorgulama")
            print("2- Para çekme")
            print("3- Para yatırma")
            print("4- Hesaplar arası transfer")
            print("5- Çıkış")

            secim = input("Lütfen bir seçenek girin: ")
            if secim == "1":
                for hesap in self.hesaplar.values():
                    print(hesap)
            elif secim == "2":
                hesap_numarasi = input("Hangi hesaptan para çekmek istiyorsunuz? (1 veya 2): ")
                miktar = int(input("Ne kadar para çekmek istiyorsunuz? "))
                hesap = self.hesaplar[hesap_numarasi]
                hesap.para_cek(miktar)
            elif secim == "3":
                hesap_numarasi = input("Hangi hesaba para yatırmak istiyorsunuz? (1 veya 2): ")
                miktar = int(input("Ne kadar para yatırmak istiyorsunuz? "))
                hesap = self.hesaplar[hesap_numarasi]
                hesap.para_yatir(miktar)
            elif secim == "4":
                gonderen_hesap_numarasi = input("Hangi hesaptan para transferi yapmak istiyorsunuz? (1 veya 2): ")
                alan_hesap_numarasi = input("Hangi hesaba para transferi yapmak istiyorsunuz? (1 veya 2): ")
                miktar = int(input("Ne kadar para transferi yapmak istiyorsunuz? "))
                gonderen_hesap = self.hesaplar[gonderen_hesap_numarasi]
                alan_hesap = self.hesaplar[alan_hesap_numarasi]
                gonderen_hesap.transfer(alan_hesap, miktar)
            elif secim == "5":
                break
            else:
                print("Geçersiz seçenek.")

