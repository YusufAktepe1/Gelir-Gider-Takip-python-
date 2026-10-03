import sqlite3

class VeritabaniYoneticisi:

    def __init__(self,db_adi="butce.db"):

        self.baglanti =sqlite3.connect(db_adi)
        self.cursor = self.baglanti.cursor()
        self.tablolari_olustur()

    def tablolari_olustur(self):
        # GELİRLER TABLOSU
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS gelirler(

                id  INTEGER  PRIMARY KEY AUTOINCREMENT,
                aciklama TEXT NOT NULL,
                tutar REAL NOT NULL,
                tarih TEXT      
            )
        """)

        #GİDERLER TABLOSU
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS giderler(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                aciklama TEXT NOT NULL,
                tutar REAL NOT NULL,
                tarih TEXT
            )
        """)
        self.baglanti.commit()

    def gelir_ekle(self,aciklama,tutar,tarih):

        self.cursor.execute("""
            INSERT INTO gelirler(aciklama,tutar,tarih)
            VALUES (?,?,?)

        """,(aciklama,tutar,tarih))
        self.baglanti.commit()
        return "Başarılı: Gelir eklendi."

    def gider_ekle(self,aciklama,tutar,tarih):
    
            self.cursor.execute("""
                INSERT INTO giderler(aciklama,tutar,tarih)
                VALUES (?,?,?)
    
            """,(aciklama,tutar,tarih))
            self.baglanti.commit()
            return "Başarılı: Gider kaydedildi."

    def bakiye_hesapla(self):
        #Toplam gelirler
        self.cursor.execute("SELECT SUM(tutar) FROM gelirler")
        toplam_gelir = self.cursor.fetchone()[0] or 0.0

        #Toplam giderler
        self.cursor.execute("SELECT SUM(tutar) FROM giderler")
        toplam_gider =self.cursor.fetchone()[0] or 0.0

        net_bakiye= toplam_gelir - toplam_gider
        return toplam_gelir,toplam_gider,net_bakiye

    def gelirleri_listele(self):
        self.cursor.execute("SELECT * FROM gelirler")
        return self.cursor.fetchall()
    def giderleri_listele(self):
        self.cursor.execute("SELECT * FROM giderler")
        return self.cursor.fetchall()
        


    
