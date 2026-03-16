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
def oneri_ver(veriler):
    pass
