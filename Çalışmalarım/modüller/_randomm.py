import random

sonuç = random.random()         #0 ile 1 arasında virgüllü değer çevirir.
sonuç = random.random() * 100   #0 ile 100 arasında virgüllü değer çevirir.
sonuç = random.uniform(1,10)    #Burada ise 1 10 arasında virgüllü değer verir.
sonuç = int(random.uniform(1,10))  #Burada ise 1 10 arasında tamsayı değer verir.



ad = ['Erkan','Yusuf', 'Hamza','Furkan']
sonuç = ad[random.randint(0,len(ad) - 1)]   #Burada ise değer göre random değer verir.

sonuç = random.choice(ad) #Yukarıda yaptımız şeklin daha sade hali choice özelliği ile daha basit şekilde yapabiliriz.

liste = list(range(10))
random.shuffle(liste)   #Burada yaptımız ise range methodu ile 0 dan 10 a kadar sayı verip random modülüyle rastgele yerleştirmemiz.
sonuç = liste


liste = range(100)
sonuç = random.sample(liste , 5) # sample methodu ile rastgele 5 tane sayı verdik.


print(sonuç)


listem = list(range(10))
random.shuffle(listem)
sonuc1 = listem
print(sonuc1)
