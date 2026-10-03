# 💰 Kişisel Bütçe ve Harcama Takipçisi (CLI Alıştırma Projesi)

Python öğrenme ve pratik yapma sürecimde, modüler programlama, SQLite veritabanı yönetimi ve nesne yönelimli programlama (OOP) temellerini pekiştirmek için sıfırdan geliştirdiğim bir komut satırı (CLI) alıştırma uygulamasıdır.

## 🧠 Bu Projede Neler Pratik Edildi?
- **Modüler Mimari:** Sorumlulukların ayrılması prensibiyle veritabanı işlemlerinin (`veritabani.py`) arayüzden (`main.py`) ayrılması.
- **Veritabanı Tasarımı:** Performans ve veri düzeni için gelirler ve giderlerin iki ayrı tabloda tutulması.
- **Birim Testleri (Unit Testing):** `unittest` kütüphanesi ve geçici bellek veritabanı (`:memory:`) kullanılarak yazılan kapsamlı test senaryoları.
- **CRUD Operasyonları & SQL:** Veritabanına veri ekleme, listeleme ve dinamik `SUM()` sorgularıyla bakiye hesaplama.

## 📂 Proje Dosya Yapısı

```text
Butce-Harcama-Takip/
│
├── veritabani.py         # SQLite yöneticisi ve veritabanı operasyonları
├── main.py               # Kullanıcı arayüzü ve menü döngüsü
├── test_veritabani.py    # Otomatik test suite'i (unittest)
├── .gitignore            # Git takibinden harici tutulan dosyalar
└── README.md             # Proje dokümantasyonu