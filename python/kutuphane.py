class Kutuphane:
    def __init__(self):
        self.dosya_adi = "kitaplar.txt"
        self.dosya = open(self.dosya_adi, "a+")

    def __del__(self):
        self.dosya.close()

    def kitaplari_listele(self):
        with open(self.dosya_adi, "r") as dosya:
            kitaplar = dosya.readlines()
            if not kitaplar:
                print("Mevcut bir kitap bulunmamaktadir.")
            else:
                print("Kitap Listesi : ")
                for kitap in kitaplar:
                    kitap_bilgisi = kitap.strip().split(',')
                    print(f"Baslik : {kitap_bilgisi[0]}, Yazar : {kitap_bilgisi[1]}")

    def kitap_ekle(self):
        baslik = input("Kitabin basligini giriniz : ")
        yazar = input("Kitabin yazarini giriniz : ")
        yayin_yili = input("Kitabin yayin yilini giriniz : ") 
        sayfa_sayisi = input("Kitabin sayfa sayisini giriniz : ")

        kitap_bilgisi = [baslik, yazar, yayin_yili, sayfa_sayisi]

        with open(self.dosya_adi, "a") as dosya:
            dosya.write(','.join(kitap_bilgisi) + '\n')

        print("Kitap basariyla eklenmistir.")

    def kitap_sil(self):
        silinecek_baslik = input("Silmek istediğiniz kitabin basliğini giriniz : ")

        with open(self.dosya_adi, "r") as dosya:
            kitaplar = dosya.readlines()

        guncellenmis_kitaplar = []
        silindi = False

        for kitap in kitaplar: 
            kitap_bilgisi = kitap.strip().split(',')
            if kitap_bilgisi[0] == silinecek_baslik:
                silindi = True
            else:
                guncellenmis_kitaplar.append(kitap)

        with open(self.dosya_adi, "w") as dosya:
            for kitap in guncellenmis_kitaplar:
                dosya.write(kitap)
        
        if silindi:
            print(f"'{silinecek_baslik}' baslikli kitap silinmiştir.")
        else:
            print(f"'{silinecek_baslik}' baslikli kitap bulunamamistir")

lib = Kutuphane()

while True:
    print("***** MENU *****")
    print("1-) Kitaplari listele")
    print("2-) Kitap Ekle")
    print("3-) Kitap Sil")
    print("Q-) Cikis")
    menu = input("Yapilacak islemin numarasini giriniz : ")

    if menu == "1":
        lib.kitaplari_listele()
    elif menu == "2":
        lib.kitap_ekle()
    elif menu == "3":
        lib.kitap_sil()
    elif menu.upper() == "Q":
        print("Program kapatiliyor...")
        break
    else:
        print("Lütfen geçerli bir karakter giriniz.")







                                               




                                      

       







