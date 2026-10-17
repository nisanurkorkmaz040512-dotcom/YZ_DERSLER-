urunler = ["Kablosuz Kulaklık", "Mekanik Klavye", "Gaming Oyuncu Faresi", "Akıllı Saat"]

arama_sorgusu = "klavye"

bulunan_urunler = []

for urun in urunler:
    if arama_sorgusu.lower() in urun.lower():
        bulunan_urunler.append(urun)

print("Arama Sorgusu:", arama_sorgusu)
print("Bulunan Eşleşen Ürünler:", bulunan_urunler)

kelime1 = "gitar"
kelime2 = "gitarlar"

kume1 = set(kelime1)
kume2 = set(kelime2)

ortak_harfler = kume1.intersection(kume2)

tum_harfler = kume1.union(kume2)

benzerlik_skoru = len(ortak_harfler) / len(tum_harfler)

print("Kelime 1 Harfleri:", kume1)
print("Kelime 2 Harfleri:", kume2)
print("Ortak Harfler:", ortak_harfler)
print("Hesaplanan Benzerlik Skoru:". round(benzerlik_skoru, 2))
