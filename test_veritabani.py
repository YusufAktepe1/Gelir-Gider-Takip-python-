import unittest
from veritabani import VeritabaniYoneticisi

class TestVeritabaniYoneticisi(unittest.TestCase):
    
    def setUp(self):
        """Her test fonksiyonu çalışmadan önce RAM üzerinde geçici bir DB oluşturur."""
        self.db = VeritabaniYoneticisi(":memory:")

    def tearDown(self):
        """Test bittikten sonra veritabanı bağlantısını güvenli bir şekilde kapatır."""
        self.db.baglanti.close()

    def test_tablolar_basariyla_olustu_mu(self):
        # Tabloların var olup olmadığını cursor ile sorgulayarak test ediyoruz.
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='gelirler'")
        gelir_tablosu = self.db.cursor.fetchone()
        
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='giderler'")
        gider_tablosu = self.db.cursor.fetchone()
        
        self.assertIsNotNone(gelir_tablosu, "Gelirler tablosu oluşturulamadı!")
        self.assertIsNotNone(gider_tablosu, "Giderler tablosu oluşturulamadı!")

    def test_gelir_ekle_ve_listele(self):
        # Gelir ekleme fonksiyonunu test ediyoruz
        mesaj = self.db.gelir_ekle("Maaş", 20000.0, "01.10.2026")
        self.assertEqual(mesaj, "Başarılı: Gelir eklendi.")

        # Listeleme ile eklenen verinin doğruluğunu kontrol ediyoruz
        gelirler = self.db.gelirleri_listele()
        self.assertEqual(len(gelirler), 1)
        self.assertEqual(gelirler[0][1], "Maaş")
        self.assertEqual(gelirler[0][2], 20000.0)
        self.assertEqual(gelirler[0][3], "01.10.2026")

    def test_gider_ekle_ve_listele(self):
        # Gider ekleme fonksiyonunu test ediyoruz
        mesaj = self.db.gider_ekle("Market", 1500.50, "02.10.2026")
        self.assertEqual(mesaj, "Başarılı: Gider kaydedildi.")

        # Listeleme ile eklenen verinin doğruluğunu kontrol ediyoruz
        giderler = self.db.giderleri_listele()
        self.assertEqual(len(giderler), 1)
        self.assertEqual(giderler[0][1], "Market")
        self.assertEqual(giderler[0][2], 1500.50)
        self.assertEqual(giderler[0][3], "02.10.2026")

    def test_bakiye_hesapla_bos_durum(self):
        # Hiç veri yokken bakiye 0 olmalı
        t_gelir, t_gider, bakiye = self.db.bakiye_hesapla()
        self.assertEqual(t_gelir, 0.0)
        self.assertEqual(t_gider, 0.0)
        self.assertEqual(bakiye, 0.0)

    def test_bakiye_hesapla_matematigi(self):
        # Birden fazla gelir ve gider ekleyip net bakiyeyi test ediyoruz
        self.db.gelir_ekle("Ek Gelir", 5000.0, "01.10.2026")
        self.db.gelir_ekle("Burs", 2000.0, "03.10.2026") # Toplam Gelir: 7000
        
        self.db.gider_ekle("Kira", 3000.0, "05.10.2026")
        self.db.gider_ekle("Fatura", 1000.0, "10.10.2026") # Toplam Gider: 4000

        t_gelir, t_gider, bakiye = self.db.bakiye_hesapla()
        
        self.assertEqual(t_gelir, 7000.0)
        self.assertEqual(t_gider, 4000.0)
        self.assertEqual(bakiye, 3000.0) # 7000 - 4000 = 3000

if __name__ == "__main__":
    unittest.main()