class Kitap:
    def __init__(self, ad, yazar, yil):
        self.ad = ad
        self.yazar = yazar
        self.yil = yil
        self.odunc = False

    def __str__(self):
        durum = "Ödünçte" if self.odunc else "Rafta"
        return f"{self.ad} - {self.yazar} ({self.yil}) [{durum}]"


class Uye:
    def __init__(self, ad, uye_id):
        self.ad = ad
        self.uye_id = uye_id
        self.alinan_kitaplar = []

    def __str__(self):
        kitap_isimleri = ", ".join([k.ad for k in self.alinan_kitaplar]) if self.alinan_kitaplar else "Yok"
        return f"Üye: {self.ad} (ID: {self.uye_id}) | Elindeki Kitaplar: {kitap_isimleri}"


class Kutuphane:
    def __init__(self):
        self.kitaplar = []
        self.uyeler = []  # Kütüphaneye kayıtlı üyeler

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"'{kitap.ad}' kütüphaneye eklendi.")

    def uye_ekle(self, uye):
        self.uyeler.append(uye)
        print(f"'{uye.ad}' isimli üye sisteme kayıt oldu.")

    def ara(self, kelime):
        sonuclar = [k for k in self.kitaplar 
                    if kelime.lower() in k.ad.lower() or kelime.lower() in k.yazar.lower()]
        return sonuclar
        
    def odunc_ver(self, kitap_adi, uye_id):
        aktif_uye = None
        for u in self.uyeler:
            if u.uye_id == uye_id:
                aktif_uye = u
                break
        
        if not aktif_uye:
            print(f"Hata: ID'si {uye_id} olan bir üye bulunamadı!")
            return
            
        for k in self.kitaplar:
            if k.ad.lower() == kitap_adi.lower():
                if k.odunc:
                    print("Bu kitap zaten ödünç verilmiş!")
                    return
                else:
                    k.odunc = True
                    aktif_uye.alinan_kitaplar.append(k)  # Kitabı üyenin listesine ekle
                    print(f"'{k.ad}' kitabı, {aktif_uye.ad} isimli üyeye ödünç verildi.")
                    return
        
        print("Kitap bulunamadı.")

    def iade_et(self, kitap_adi, uye_id):
        # Önce üyeyi bulalım
        aktif_uye = None
        for u in self.uyeler:
            if u.uye_id == uye_id:
                aktif_uye = u
                break

        if not aktif_uye:
            print(f"Hata: ID'si {uye_id} olan bir üye bulunamadı!")
            return

        for k in aktif_uye.alinan_kitaplar:
            if k.ad.lower() == kitap_adi.lower():
                k.odunc = False  # Kitabı tekrar rafa koyduk
                aktif_uye.alinan_kitaplar.remove(k)  # Üyenin elinden çıkardık
                print(f"'{k.ad}' kitabı {aktif_uye.ad} tarafından başarıyla iade edildi.")
                return

        print(f"Bu üyenin elinde '{kitap_adi}' isimli bir kitap görünmüyor.")

    def listele(self):
        print("\n--- Kütüphanedeki Kitaplar ---")
        if not self.kitaplar:
            print("Kütüphane henüz boş.")
        for k in self.kitaplar:
            print(k)

    def uyeleri_listele(self):
        print("\n--- Kayıtlı Üyeler ---")
        if not self.uyeler:
            print("Sisteme kayıtlı üye yok.")
        for u in self.uyeler:
            print(u)


lib = Kutuphane()
lib.kitap_ekle(Kitap("Dune", "Frank Herbert", 1965))
lib.kitap_ekle(Kitap("1984", "George Orwell", 1949))
lib.uye_ekle(Uye("Zeynep Akyel", 101))

while True:
    print("\n==============================")
    print("  KÜTÜPHANE YÖNETİM SİSTEMİ  ")
    print("==============================")
    print("1 - Kitap Ekle")
    print("2 - Üye Kaydet")
    print("3 - Kitap Ödünç Ver")
    print("4 - Kitap İade Et")
    print("5 - Kitapları Listele")
    print("6 - Üyeleri Listele")
    print("0 - Çıkış")
    
    secim = input("Lütfen yapmak istediğiniz işlemi seçin: ")

    if secim == "1":
        ad = input("Kitap Adı: ")
        yazar = input("Yazar Adı: ")
        yil = int(input("Yayın Yılı: "))
        lib.kitap_ekle(Kitap(ad, yazar, yil))
    
    elif secim == "2":
        ad = input("Üye Ad Soyad: ")
        uye_id = int(input("Üye ID (Sayı): "))
        lib.uye_ekle(Uye(ad, uye_id))
    
    elif secim == "3":
        kitap_adi = input("Ödünç verilecek kitap adı: ")
        uye_id = int(input("Ödünç alacak üyenin ID'si: "))
        lib.odunc_ver(kitap_adi, uye_id)
        
    elif secim == "4":
        kitap_adi = input("İade edilecek kitap adı: ")
        uye_id = int(input("İade eden üyenin ID'si: "))
        lib.iade_et(kitap_adi, uye_id)

    elif secim == "5":
        lib.listele()

    elif secim == "6":
        lib.uyeleri_listele()

    elif secim == "0":
        print("Sistemden çıkılıyor. İyi günler!")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
