import os                           #Terminal temizlemek için
os.system('cls||clear')

import time 
import requests
from bs4 import BeautifulSoup



def kur_ogren(kur_kodu):
    t=time.time()
    url = "https://www.ziraatbank.com.tr/tr/fiyatlar-ve-oranlar"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,  "lxml")
    kurlar = soup.find("div",{"data-module":"DovizKur"}).find("div",{"data-id":"rdBranchDoviz"}).tbody.find_all("tr")
    for kur in kurlar:
        #print(kur.td.text)
        if kur.td.text==kur_kodu:
            liste=[k.text for k in kur.find_all("td")]

    print(f'www.ziraatbank.com.tr sidesinden alınan {liste[1]} için gişe kur değerleri')
    print(f'{liste[1]} alış: {liste[2]},\t{liste[1]} satış: {liste[3]}\n')
    print(f'İşlem için geçen süre:{(time.time()-t):.2f} sn')


while True:
    print('Menü'.center(100,'_'))
    secim=input('Çıkış için ENTER\'a basın.\nÖğrenmek istediğiniz kur değerini giriniz (USD,EUR,GBP,CHF,JPY,DKK,SEK,NOK,CAD,AUD,SAR,RUB): ').upper()
    print(' ')
    if secim in ["USD","EUR","GBP","CHF","JPY","DKK","SEK","NOK","CAD","AUD","SAR","RUB"]:
        kur_ogren(secim)
        print('\n\n\n')
    else:
        print('Yanlış giriş veya çıkış yaptınız\n\n')
        break #Exit










