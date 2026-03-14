import utils

while True:
    print("""
          1-)Çalışma kaydı ekle\n
          2-)Kayıtları listele\n
          3-)Analiz yap\n
          4-)Grafik göster\n
          5-)Öneri ver\n
          6-)Çıkış\n
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
        pass
    elif secim==4:
        pass
    elif secim==5:
        pass
    elif secim==6:
        print("Programdan çıktınız.")
        break
    else:
        print("Doğru sayı giriniz.")