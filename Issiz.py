from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube_dict):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self._tecrube_dict = tecrube_dict
        self._statu = self.statu_bul()

    # getter and setter methods for tecrube_dict
    def get_tecrube_dict(self):
        return self._tecrube_dict

    def set_tecrube_dict(self, tecrube_dict):
        self._tecrube_dict = tecrube_dict

    def statu_bul(self):
        try:
            mavi_yaka_deger = self._tecrube_dict.get("mavi yaka", 0) * 0.20
            beyaz_yaka_deger = self._tecrube_dict.get("beyaz yaka", 0) * 0.35
            yonetici_deger = self._tecrube_dict.get("yonetici", 0) * 0.45
            max_deger = max(mavi_yaka_deger, beyaz_yaka_deger, yonetici_deger)
            if max_deger == mavi_yaka_deger:
                return "mavi yaka"
            elif max_deger == beyaz_yaka_deger:
                return "beyaz yaka"
            else:
                return "yonetici"
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            return None

    def __str__(self):
        return f"{super().__str__()}, En Uygun Statü: {self._statu}"

