from veritabani import   VeritabaniYoneticisi
from time import sleep as zmn
# veritabanı  nesnesi oluşturma:
db=VeritabaniYoneticisi()

def ana_menu():
    while True:
        print("\n--- KİŞİSEL BÜTÇE TAKİP SİSTEMİ ---")
        print("1. Gelir Ekle")
        print("2. Gider Ekle")
        print("3. Gelirleri Listele")
        print("4. Giderleri Listele")
        print("5. Bakiye Durumu Gör")
        print("6. Çıkış")

        secim=input("seiçiminiz (1-6):")

        if secim == "1":
            aciklama = input("Gelir açıklaması (örn: Maaş): ")
            tutar = float(input("Tutar: "))
            tarih = input("Tarih (GG.AA.YYYY): ")
            print(db.gelir_ekle(aciklama,tarih,tutar))

        elif secim =="2":
            aciklama = input("Gider açıklaması (örn: Market): ")
            tutar = float(input("Tutar: "))
            tarih = input("Tarih (GG.AA.YYYY): ")
            print(db.gider_ekle(aciklama,tarih,tutar))

        elif secim == "3":
            print("---GELİRLER---")
            gelirler = db.gelirleri_listele()
            for g in gelirler:
                print(f"ID: {g[0]} | Açıklama: {g[1]} | Tutar: {g[2]} TL | Tarih: {g[3]}")
        elif secim == "4":
            print("---GİDERLER---")
            giderler = db.giderleri_listele()
            for g in giderler:
                print(f"ID: {g[0]} | Açıklama: {g[1]} | Tutar: {g[2]} TL | Tarih: {g[3]}")

        elif secim == "5":
            t_gelir,t_gider,bakiye =db.bakiye_hesapla()
            print(f"\nToplam Gelir: {t_gelir} TL")
            print(f"Toplam Gider: {t_gider} TL")
            print(f"Net Bakiye: {bakiye} TL")

        elif secim == "6":
            print("programdan çıkılıyor.")
            zmn(2)
            break
        else:
            print("Geçersiz seçim! Lütfen 1-6 arasında bir değer girin.") 

if __name__ =="__main__":
    ana_menu()

        
