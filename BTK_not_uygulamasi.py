import os                           #Terminal temizlemek için
os.system('cls||clear')

def not_hesapla(satir):
    satir_list=satir[:-1].split(':')
    isim=satir_list[0]
    notlar=satir_list[1].split(',')
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    ort=(not1+not2+not3)/3

    if ort>=90:
        harf='AA'
    elif ort>=70 and ort<90:
        harf='FF'
    else:
        harf='FF'

    return isim+" isimli öğrenci ortalaması "+str(ort)+"\'dır. Harf notu= "+harf+"\n"

    print(f'{isim} {ort}')

def ortalamalari_oku():
    with open("sinav_notlari.txt",'r',encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad=input('Öğrenci adı: ')
    soyad=input('Öğrenci soyadı: ')
    not1=input('not 1: ')
    not2=input('not 2: ')
    not3=input('not 3: ')

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+' '+soyad+':'+not1+','+not2+','+not3+'\n')

def notlari_kaydet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file1:
        liste=[not_hesapla(i) for i in file1]

    with open("sonuclar.txt","w",encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)

while True:
    print('*'.center(50,'*'))
    islem=input(' 1- Notları oku \n 2- Not gir \n 3- Notları kaydet \n 4- Çıkış \n')

    if islem=='1':
        ortalamalari_oku()
    elif islem=='2':
        not_gir()
    elif islem=='3':
        notlari_kaydet()
    else:
        print('Çıkış yapıldı')
        break













