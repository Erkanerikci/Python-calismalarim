import os
sonuc = dir(os)
sonuc = os.name #işletim sistemi adı

# os.chdir('C:\\') # Burada ise hangi dizine uygulamak istersek onu yazıyoruz
sonuc = os.getcwd() #Projenin hangi klasörde olduğunu çıktı olarak gösterir
#os.mkdir("Yeni Klasör") # Klasör oluşturma
sonuc = os.listdir() #Bulunduğu dizindeki dosya ve klasörleri gösterir
print(sonuc)

# os.makedirs("Yeni Klasör/yeni klasör")

#listeleme
sonuc = os.listdir()
# sonuc = os.listdir('C:\\')
for dosya in os.listdir():
    if dosya.endswith('.py'):
        print(dosya)
print(sonuc)

#path
sonuc = os.path.abspath("_os.py") #Burdan dosyanın tam konumu buluyoruz
sonuc = os.path.dirname("D:\Okul Dersleri\Python\Çalışmalarım\_os.py") #dizin ismi
sonuc = os.path.dirname(os.path.abspath("_os.py"))
sonuc = os.path.exists("D:\Okul Dersleri\Python\Çalışmalarım\_os.py") #dosya var yada yok olduğunu gösterir
sonuc = os.path.isdir("D:\Okul Dersleri\Python\Çalışmalarım") #klasörün var yada yok olduğunu gösterir
sonuc = os.path.join("C:\\","deneme") # bağlamak için
sonuc = os.path.split("C:\\deneme") # bölmek için
sonuc = os.path.splitext("_os.py") #uzantısı ile ismini bölüyor

print(sonuc)