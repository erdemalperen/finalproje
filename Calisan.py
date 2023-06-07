from Insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrübe = tecrube
        self.__maas = maas

    # get / set methods
    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrübe

    def set_tecrube(self, tecrube):
        self.__tecrübe = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def zam_hakki(self):
        return None  # Çalışan sınıfı için zam hakkı belirsizdir

    def get_yeni_maas(self):
        return self.__maas  # yeni maaş belirlenmediyse mevcut maaş döndürülür.

    def __str__(self):
        return f"Ad: {self.get_ad()} Soyad: {self.get_soyad()} Tecrübe: {self.get_tecrube()} Yeni Maaş: {self.get_yeni_maas()}"
