import utils
import analysis
import charts

result= utils.verileri_oku()

while True:
    print("""
          1-)Çalışma kaydı ekle
          2-)Kayıtları listele
          3-)Analiz yap
          4-)Gün bazlı grafik göster
          5-)Ders bazlı grafik göster
          6-)Öneri ver
          7-)Çıkış
          """)
    try:
        secim = int(input("Seçim yapınız:"))
    except ValueError:
        print("Lütfen bir sayı giriniz.")
        continue  # döngünün başına dön
    if secim==1:
        utils.kayit_ekle()
    elif secim==2:
        utils.verileri_listele()
    elif secim==3:
        analysis.gun_bazli_analiz(result)
        analysis.ders_bazli_analiz(result)
    elif secim==4:
        charts.ders_grafigi(result)
        charts.gun_grafigi(result)
    elif secim==5:
        pass
    elif secim==6:
        pass
    elif secim==7:
        print("Programdan çıktınız.")
        break
    else:
        print("Doğru sayı giriniz.")