def toplam_sure(result):
    sure=[]
    toplam=0
    for kayit in result:
        sure.append(kayit["sure"])
    for num in range(len(sure)):
        toplam+=sure[num]

    print(f"Toplam çalışma süresi:{toplam}")
    return toplam

def ortalama_verim(result):
    verim=[]
    toplamVerim=0
    ortVerim=0
    for kayit in result:
        verim.append(kayit["verim"])
    for num in range(len(verim)):
        toplamVerim+=verim[num]
    ortVerim=toplamVerim/len(verim)

    print(f"Ortalama verim:{ortVerim}")
    return ortVerim

def en_cok_calisilan_ders(result):
    dictDers={}
    for kayit in result:
        dictDers[kayit["ders"]]=kayit["sure"]
    print(max(dictDers.keys()))


def ders_bazli_analiz(result):
    dersler = {}

    for kayit in result:
        ders = kayit["ders"]

        if ders in dersler:
            dersler[ders] += kayit["sure"]
        else:
            dersler[ders] = kayit["sure"] 

    for ders, sure in dersler.items():
        print(f"{ders} : {sure} dk")

def gun_bazli_analiz(result):
    gunler = {}

    for kayit in result:
        tarih = kayit["tarih"]

        if tarih in gunler:
            gunler[tarih] += kayit["sure"]
        else:
            gunler[tarih] = kayit["sure"] 

    for tarih, sure in gunler.items():
        print(f"{tarih} : {sure} dk")

def oneri_ver(veriler):
    pass
