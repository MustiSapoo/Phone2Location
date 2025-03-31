import os
import sys
import time
import opencage
import folium
import phonenumbers

def figlet():
    os.system("clear")
    os.system("figlet Phone2Location") # Imza Gosteriyor
    print("""
              ##############################################
              ##                                          ##
              ##    Developed By MustiSaplar 2025-2026    ##
              ##                                          ##
              ##############################################""")
figlet()

print("")
numara = input("Hedefin Telefon Numarasını Yazınız: ")

def figlet():
    os.system("clear")
    os.system("figlet Phone2Location") # Imza Gosteriyor
    print("""
              ##############################################
              ##                                          ##
              ##    Developed By MustiSaplar 2025-2026    ##
              ##                                          ##
              ##############################################""") 
figlet()

print("")
def bekleme_animasyonu():
    # Bekleme animasyonunu yazdıran bir liste
    animation = ['|', '/', '-', '\\']
    
    # 10 saniye boyunca animasyon goster
    for _ in range(20):  # 20 kez donecek (yaklasık 10 saniye)
        for frame in animation:
            sys.stdout.write(f'\r{frame} Lütfen Bekleyin...\r')
            sys.stdout.flush()
            time.sleep(0.2)

# Animasyonu baslat
bekleme_animasyonu()

def figlet():
    os.system("clear")
    os.system("figlet Phone2Location") # Imza Gosteriyor
    print("""
              ##############################################
              ##                                          ##
              ##    Developed By MustiSaplar 2025-2026    ##
              ##                                          ##
              ##############################################""") 
figlet()
 
print("")
print("[+] Bulundu")
print("[*] Sorgulanan Numara:", numara)
print("")

from phonenumbers import geocoder # Numaranin Ulkesini Bulmak Icin
ülke = phonenumbers.parse(numara, "CH") # Numarayi Yazmak Icin
location = geocoder.description_for_number(ülke, "tr") # Ve Output Ulke Ortaya Cikacak
print("Ülke:", location)

from opencage.geocoder import OpenCageGeocode
anahtar = 'b8d1870ffad84d4998880b20ff7356dd'
geocoder = OpenCageGeocode(anahtar)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print("Latitude:", lat, "Longitude:", lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup = location).add_to((myMap))

myMap.save(numara,".html")

from phonenumbers import carrier
servis_numara = phonenumbers.parse(numara, "RO")
print("Internet Servis Sağlıyıcısı:", carrier.name_for_number(servis_numara, "tr"))
print("")
print("Hedefin Konumu Phone2Location Dosyasına Kaydedilmiştir")


