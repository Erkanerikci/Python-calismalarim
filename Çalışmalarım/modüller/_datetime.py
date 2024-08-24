from datetime import datetime 

simdi = datetime.now() # Burada yapmış olduğumuz şeyin mantığı ise çalıştırdığımız zamanki tarihi göstermesi

sonuc = simdi.year 
print(sonuc)

sonuc = simdi.month 
print(sonuc)

sonuc = simdi.day 
print(sonuc)

sonuc = simdi.minute
print(sonuc)

sonuc = simdi.hour
print(sonuc)

sonuc = simdi.second
print(sonuc)

sonuc = datetime.ctime(simdi)
print(sonuc)

sonuc = datetime.strftime(simdi,'%Y') #Burada kısaltma vererek çağırıyoruz mesela Y verdik yani Year a karşılık
sonuc = datetime.strftime(simdi,'%M')
sonuc = datetime.fromtimestamp(0) #Bilgisayarın milad bilgisi
print(sonuc)