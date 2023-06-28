# bankamatik


hesap1=5000
hesap2=5000

sifre="cicek"

#şifreyi bilip bilediğini kontrol ediyoruz
kontrol=0

menu=""" *** CİCEK BANK *** 
1- Bakiye sorma
2- Para çekme
3- Para yatırma
4- Hesaplar arası transfer
5- Çıkış
"""

# şifre kontrol döngüsü
for i in range(3):
    giris=input("Sifrenizi giriniz: ")

    if giris==sifre:
        print("Şifre doğru")
        kontrol=1
        break

#şifeyi bilemediyse programa girişi engelleniyor
if kontrol != 1:
    print("Şifreniz yanlış, kartınız bloke oldu")

# şifreyi bildiyse programa girişine izin veriliyor
else:
    #ana program döngüsü
    while True:
        print(menu)

        secim=input("Seçiminiz: ")

        if secim=="1":
            print(f"Hesap bakiyeniz. hesap1: {hesap1}  hesap2: {hesap2}")

        elif secim=="5":
            print("Program sona erdi")
            break

        elif secim=="2":
            miktar1=int(input("Ne kadar çekeceksiniz: "))
            hesapSec=input("Hangi hesaptan para çekeceksiniz: 1-hesap1, 2-hesap2")

            if hesapSec=="1":
                if miktar1>hesap1:
                    print("Hesap1 bakiyeniz yetersiz")
                else:
                    hesap1=hesap1-miktar1

            elif hesapSec=="2":
                if miktar1>hesap2:
                    print("Hesap2 bakiyeniz yetersiz")
                else:
                    hesap2=hesap2-miktar1

            else:
                print("Yanlış seçim yaptınız")

        elif secim=="3":
            miktar2=int(input("Ne kadar para yatıracaksınız: "))

            yatir=input("Hangi hesaba para yatıracaksınız: 1-hesap1, 2-hesap2")

            if yatir=="1":
                hesap1+=miktar2
            elif yatir=="2":
                hesap2+=miktar2
            else:
                print("Yanlış seçim yaptınız: ")

        elif secim=="4":
            hesapT=input("Hangi hesaptan transfer yapacaksınız: 1-hesap1, 2-hesap2 ")
            miktarT=int(input("Ne kadar transfer edeceksiniz: "))

            if hesapT=="1":

                if miktarT>hesap1:
                    print("Yetersiz bakiye")
                else:
                    hesap1=hesap1-miktarT
                    hesap2=hesap2+miktarT

            elif hesapT=="2":
                if miktarT>hesap2:
                    print("Yetersiz bakiye")
                else:
                    hesap2=hesap2-miktarT
                    hesap1=hesap1+miktarT


