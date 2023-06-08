from Calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi

    # get / set methods
    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        if self.get_tecrube() < 24:  # 2 yıl
            zam_orani = self.__yipranma_payi * 10
        elif 24 <= self.get_tecrube() < 48:  # 2-4 yıl
            if self.get_maas() < 15000:
                zam_orani = (self.get_maas() % self.get_tecrube()) / 2 + self.__yipranma_payi * 10
            else:
                zam_orani = None
        elif self.get_tecrube() >= 48:  # 4 yıldan fazla
            if self.get_maas() < 25000:
                zam_orani = (self.get_maas() % self.get_tecrube()) / 3 + self.__yipranma_payi * 10
            else:
                zam_orani = None
        else:
            zam_orani = None

        if zam_orani is not None:
            self.set_maas(self.get_maas() + zam_orani)
        return zam_orani
