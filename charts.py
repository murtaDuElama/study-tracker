import matplotlib.pyplot as plt
import analysis

def ders_grafigi(result):
    dersler=analysis.ders_bazli_analiz(result)
    ders=[]
    sure=[]
    for anahtar,deger in dersler.items():
        ders.append(anahtar)
        sure.append(deger)

    plt.bar(ders,sure)
    plt.title("Günlük ders çalışma süresi")
    plt.xlabel("ders")
    plt.ylabel("süre(dk)")
    plt.show()

def gun_grafigi(result):
    gunler=analysis.gun_bazli_analiz(result)
    tarih=[]
    sure=[]
    for anahtar,deger in gunler.items():
        tarih.append(anahtar)
        sure.append(deger)

    plt.plot(tarih,sure)
    plt.title("Günlük")
    plt.xlabel("tarih")
    plt.ylabel("süre(dk)")
    plt.show()