import beylerXomg as bx # beylerXomg import edilip bx olarak kısaltılır
import random # random sınıfı import edilir
import time # time sınıfı import edilir

random_sayı = random.randint(1, 101) # 1-100 arasında random sayı alır
deneme_sayısı = 0 # her deneme için arttıracağımız deneme değişkeni

baslangic = time.time() # başlangıç süresini alıyoruz 

while True: # while döngüsü başlatılır 
    deneme_sayısı += 1 # her başa sarmada deneme +1 yapılır
    try: # hata olup olmadığını kontrol etmek için
        sayı_al = int(input("tahmininiz: ")) # kullanıcıdan (int) sayı alınır
    except: # eğer hata çıktıysa,örn kullanıcı string girdiyse tüm hataları içerir(bu haliyle)
        bx.oynat.kategori.milyoner.sesler.yanlıs_2() # ktüphanemizden yanlış_2 sesinşi çal
        print(">Lütfen sayı giriniz!") # uyarı mesajı
        continue # başa sar, yani hata verip uygulamayı kapatma 
    
    if sayı_al == random_sayı: # eğer girilen sayı , randoma eşitse(doğruysa)
        bitis = time.time() # bitiş zamanını al(sayacı durdur) 
        zaman = bitis - baslangic # bitiş den başlangıcı cıkar gecen sureyi bul 
        bx.oynat.kategori.milyoner.sesler.dogru_5() # doğru_5 sesini çal
        print(
            sayı_al, # girilen sayı
            f" tahmininiz doğru :)\n" # mesaj
            f"{deneme_sayısı}. denemede buldunuz\n" # deneme sayısı yazdırma (f"string") ile
            f"{zaman:.2f} saniyede buldunuz") # sureyi yazdırma formatlı(:.2f) virgülden sonra iki basamak
        break  # döngüden çık
    elif sayı_al < random_sayı: # eğer girilen doğrudan küçükse
        bx.oynat.kategori.milyoner.sesler.yanlıs_1() # sesi çal
        print("YANLIŞ - sayıyı büyült!")  # mesaj  

    elif sayı_al > random_sayı: # büyükse
        bx.oynat.kategori.milyoner.sesler.yanlıs_1() # sesi çal
        print("YANLIŞ - sayıyı küçült!") # mesaj









# yorumsuz

import beylerXomg as bx 
import random
import time

random_sayı = random.randint(1, 101)
deneme_sayısı = 0

baslangic = time.time()  

while True: 
    deneme_sayısı += 1
    try:
        sayı_al = int(input("tahmininiz: "))
    except:
        print(">Lütfen sayı giriniz!")
        continue  
    
    if sayı_al == random_sayı:
        bitis = time.time()  
        zaman = bitis - baslangic  
        bx.oynat.kategori.milyoner.sesler.dogru_5()
        print(
            sayı_al,
            f" tahmininiz doğru :)\n"
            f"{deneme_sayısı}. denemede buldunuz\n"
            f"{zaman:.2f} saniyede buldunuz")
        break  
    elif sayı_al < random_sayı:
        bx.oynat.kategori.milyoner.sesler.yanlıs_1()
        print("YANLIŞ - sayıyı büyült!")    

    elif sayı_al > random_sayı:
        bx.oynat.kategori.milyoner.sesler.yanlıs_1()

        print("YANLIŞ - sayıyı küçült!")
