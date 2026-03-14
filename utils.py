from datetime import datetime
import json
def kayit_ekle():
    kayit={}
    while True:
        try:
            ders_adi=input("Ders adı giriniz:")
            if len(ders_adi.strip()) > 0:
                break
        except:
            print("Geçerli bir ders adı giriniz!!!")
    while True:
        try:
            sure=int(input("Ders çalışma sürenizi giriniz(0-120dk):"))
            if sure>0 and sure<=120:
                break
        except ValueError:
            print("Geçerli bir süre giriniz!!!")
    while True:
        try:
            verim=int(input("Verim puanı giriniz(0-10):"))
            if verim>0 and verim<=10:
                break
        except ValueError:
            print("Geçerli bir verim puanı giriniz!!!")
    while True:
        try:
            tarih_str = input("Tarih giriniz (GG-AA-YYYY): ")
            tarih = datetime.strptime(tarih_str, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Tarihi yanlış formatta girdiniz!")

    kayit = {
    "ders": ders_adi,
    "sure": sure,
    "verim": verim,
    "tarih": str(tarih)
    }
    kayit_ekle_ve_kaydet(kayit)
    
def verileri_oku():
    with open("study_data.json", "r", encoding="utf-8") as f:
        result = json.load(f)
        return result
        
def verileri_listele():
        result=verileri_oku()
        for kayit in result:
            print(f"Ders adı: {kayit['ders']}")
            print(f"Çalışma süresi: {kayit['sure']}")
            print(f"Verim: {kayit['verim']}")
            print(f"Tarih: {kayit['tarih']}")
            print("---")

def verileri_kaydet(veriler):
    with open("study_data.json", "w", encoding="utf-8") as f:
        json.dump(veriler, f, indent=4, ensure_ascii=False)

def kayit_ekle_ve_kaydet(yeni_kayit):
    veriler = verileri_oku()      # mevcut kayıtları al
    veriler.append(yeni_kayit)    # yeni kaydı ekle
    verileri_kaydet(veriler)      # dosyaya yaz