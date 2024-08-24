import re

sonuc = dir(re)

string = "Regular Expression"
sonuc = re.findall("Regular",string) #R.E'nin amacı bişeyin içinde bişey aramadır.
sonuc = len(sonuc)
sonuc = re.split(" ",string) # Verdiğimiz değişkene kadar Bölmek için kulanılır 
sonuc = re.sub(" ","-",str) # Burda da istediğimiz şeyi değiştirebiliyoruz
sonuc = re.search("Regular",string) # Burada ise karakterin konumunu veriyor

sonuc = re.span() #konumu
sonuc = re.start() #başlangıç konumu
sonuc = re.end() #bitiş konumu
sonuc = re.string() #Nerede aradığını gösterir.

print(sonuc)
