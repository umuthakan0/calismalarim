class simple_mp3():
    def __init__(self):
        self.durum=True
    def çalıştır(self):
        self.menu()
        sec=self.seçim()
        if sec==1:
            self.cikarma()
        if sec ==2:
            self.toplam()
        if sec==3:
            self.çarpma()
        if sec==4:
            self.asal()
        if sec==5:
            self.kok()
        if sec==6:
            self.usalma()
        if sec ==7:
            self.bölme()
        if sec==8:
            self.çikis()
    def toplam(self):
        while True:
            try:
                a1 = int(input("sayı gır"))
                a2 = int(input("sayı gır"))
                print("işlemin sonucu= ", a2 + a1)
                break
            except ValueError:
                print("lutfen sayısal ifade girin")

    def çarpma(self):
        while True:
            try:
                a1 = int(input("sayı gır"))
                a2 = int(input("sayı gır"))
                if a1 > a2:
                    sonuc = a1 * a2
                    print(sonuc)
                else:
                    print("işlemin sonucu= ", a2 * a1)
                break
            except ValueError:
                print("lutfen sayısal ifade girin")


    def bölme(self):
        while True:
            try:
                a1 = int(input("sayı gır"))
                a2 = int(input("sayı gır"))
                print("kuçuk sayı buyuk olan sayıya bolunecektir")
                if a1 > a2:
                    sonuc = a1 / a2
                else:
                    print("işlemin sonucu= ", a2 / a1)
                break
            except ValueError:
                print("lutfen sayısal ifade girin")

    def cikarma(self):
        while True:
            try:
                a1 = int(input("sayı gır"))
                a2 = int(input("sayı gır"))
                if a1 > a2:
                    sonuc = a1 - a2
                    print(sonuc)
                else:
                    print("işlemin sonucu= ", a2 - a1)
                break
            except ValueError:
                print("lutfen sayısal ifade girin")

    def usalma(self):
        while True:
            try:
                a1 = int(input("sayı gır"))
                a2 = int(input("sayı gır"))
                print("BÜYÜK OLAN SAYININ ÜSSÜ ALINACAKTIR...")
                if a1 > a2:
                    sonuc = a1 ** a2
                    print("işlemin sonucu= ", sonuc)
                else:
                    print("işlemin sonucu= ", a2 ** a1)
                break
            except ValueError:
                print("lutfen sayısal ifade girin")

    def menu(self):
        print("""
        *******MENU*******
        1.çıkarma
        2.toplama
        3.carpma
        4.asal bulma
        5.kok alama
        6.uss alam
        7.bolme
        8.off mode""")
    def asal(self):
        while True:
            try:
                a1 = int(input("sayı gır"))
                for i in range(a1, 1, -1):
                    if a1 % i == 0:
                        k = k + 1

                if k <= 2:
                    print("sayı asaldır...")
                else:
                    print("sayı asal değildir...")
                break
            except ValueError:
                print("lutfen sayısal ifade girin")
    def kok(self):
        while True:
            try:
                a1 = int(input("sayı gır"))
                sonuc = a1 ** 0.5
                print("işlemin sonucu= ", sonuc)
                break
            except ValueError:
                print("lutfen sayısal ifade girin")

    def seçim(self):
        while True:
            try:
                secim = int(input("lutfen yapacagınız işlemi belirtin "))
                while secim < 1 or secim > 8:
                    secim = int(input("LUTFEN BELİRTİLEN ARALIKLARDA SEÇİM YAPINIZ... "))
                return secim
                break
            except ValueError:
                print("seçim hatalı tekrar deneyin")


    def çikis(self):
        self.durum=False

mp3=simple_mp3()
while mp3.durum:
    mp3.çalıştır()