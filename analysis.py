def toplam_sure(result,tarih):
    sure=[]
    toplam=0
    for kayit in result:
        if kayit["tarih"] == tarih:
            sure.append(kayit["sure"])
    for num in range(len(sure)):
        toplam+=sure[num]
    return toplam

def gun_bazli_verim(result, tarih):
    toplamVerim = 0
    kayitSayisi = 0

    for kayit in result:
        if kayit["tarih"] == tarih:
            toplamVerim += kayit["verim"]
            kayitSayisi += 1

    if kayitSayisi > 0:
        ort = toplamVerim / kayitSayisi
        return ort
    else:
        return None

def en_cok_calisilan_ders(result,tarih):
    dictDers={}
    for kayit in result:
        if kayit["tarih"] == tarih:
            dictDers[kayit["ders"]]=kayit["sure"]
    return max(dictDers.keys())


def ders_bazli_analiz(result):
    dersler = {}

    for kayit in result:
        ders = kayit["ders"]

        if ders in dersler:
            dersler[ders] += kayit["sure"]
        else:
            dersler[ders] = kayit["sure"] 
    return dersler

def gun_bazli_analiz(result):
    gunler = {}

    for kayit in result:
        tarih = kayit["tarih"]

        if tarih in gunler:
            gunler[tarih] += kayit["sure"]
        else:
            gunler[tarih] = kayit["sure"]
    return gunler
def oneri_ver(result):
    if len(result) == 0:
        print("Henüz kayıt yok, öneri verilemiyor.")
        return

    # 1. Ortalama verim düşükse
    toplamVerim = 0
    for kayit in result:
        toplamVerim += kayit["verim"]
    ortVerim = toplamVerim / len(result)

    if ortVerim < 5:
        print("⚠️ Verimliliğin düşük görünüyor, daha kısa çalışma blokları deneyebilirsin.")

    # 2. Son 3 kayıtta verim düşüşü varsa
    if len(result) >= 3:
        sonUc = result[-3:]
        if sonUc[0]["verim"] > sonUc[1]["verim"] > sonUc[2]["verim"]:
            print("⚠️ Son günlerde performans düşüşü var, çalışma saatlerini yeniden planla.")

    # 3. Bir derse çok az zaman ayrıldıysa
    dersler = {}
    for kayit in result:
        ders = kayit["ders"]
        if ders in dersler:
            dersler[ders] += kayit["sure"]
        else:
            dersler[ders] = kayit["sure"]

    for ders, sure in dersler.items():
        if sure < 60:
            print(f"⚠️ {ders} dersine daha fazla zaman ayırman faydalı olabilir.")

    # 4. Bir günde çok fazla çalışıldıysa
    gunler = {}
    for kayit in result:
        tarih = kayit["tarih"]
        if tarih in gunler:
            gunler[tarih] += kayit["sure"]
        else:
            gunler[tarih] = kayit["sure"]

    for tarih, sure in gunler.items():
        if sure > 300:
            print(f"⚠️ {tarih} tarihinde çok uzun çalışmışsın, mola planlamayı unutma.")