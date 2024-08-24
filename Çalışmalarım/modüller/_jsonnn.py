class Kullanici:
    def __init__(self,AdSoyad,Sifre,Mail):
        self.AdSoyad = AdSoyad
        self.Sifre = Sifre
        self.Mail = Mail 


class KullaniciDeposu:
    def __init__(self):
        self.kullanıcı =[]

    def kayıt(self):
        pass
    def giris(self):
        pass
    def dosyakayıt(self):
        pass

while True:
    print("Menü".center(50,"*"))
    secim = input("1- Kayıt\n2- Giris\n3- Çıkış Yap\n4- Kimlik Bilgisi\n5- Uygulamadan Çık\nSeçiniz: ")
    if secim == "5":
        break
    else:
        if secim == "1":
            pass #Kayıt
        elif secim == "2":
            pass #Giris
        elif secim == "3":
            pass #Çıkış Yap
        elif secim == "4":
            pass#Kimlik
        else:
            print("Yanlış Karakter girdiniz.")