from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    # get / set methods
    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
        eski_maas = self.get_maas()
        if self.get_tecrube() < 24:  # 2 yıl
            yeni_maas = self.__tesvik_primi
        elif 24 <= self.get_tecrube() < 48:  # 2-4 yıl
            if self.get_maas() < 15000:
                yeni_maas = ((self.get_maas() % self.get_tecrube()) * 5) + self.__tesvik_primi
            else:
                yeni_maas = None
        elif self.get_tecrube() >= 48:  # 4 yıldan fazla
            if self.get_maas() < 25000:
                yeni_maas = ((self.get_maas() % self.get_tecrube()) * 4) + self.__tesvik_primi
            else:
                yeni_maas = None
        else:
            yeni_maas = None

        if yeni_maas is not None:
            self.set_maas(yeni_maas)
        return yeni_maas
