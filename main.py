import pandas as pd
import numpy as np
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka


def main():
    people = [Insan('11111111111', 'Ali', 'Veli', 30, 'M', 'TR'),
              Insan('22222222222', 'Ayşe', 'Fatma', 25, 'F', 'TR'),
              Issiz('33333333333', 'Ahmet', 'Mehmet', 40, 'M', 'TR', {'Mavi Yaka': 2, 'Beyaz Yaka': 5, 'Yönetici': 1}),
              Issiz('44444444444', 'Elif', 'Merve', 35, 'F', 'TR', {'Mavi Yaka': 1, 'Beyaz Yaka': 3, 'Yönetici': 8}),
              Issiz('55555555555', 'Osman', 'Can', 33, 'M', 'TR', {'Mavi Yaka': 6, 'Beyaz Yaka': 4, 'Yönetici': 3}),
              Calisan('66666666666', 'Esra', 'Betül', 37, 'F', 'TR', 'Teknoloji', 36, 20000),
              Calisan('77777777777', 'Eren', 'Batu', 28, 'M', 'TR', 'Muhasebe', 24, 12000),
              Calisan('88888888888', 'Yusuf', 'Kadir', 42, 'M', 'TR', 'İnşaat', 60, 30000),
              MaviYaka('99999999999', 'Zeynep', 'Gamze', 39, 'F', 'TR', 'Diğer', 48, 15000, 0.3),
              MaviYaka('12345678901', 'Kerem', 'Barış', 31, 'M', 'TR', 'Teknoloji', 36, 16000, 0.4),
              MaviYaka('10987654321', 'Selin', 'Ceren', 29, 'F', 'TR', 'Muhasebe', 18, 13000, 0.2),
              BeyazYaka('23456789012', 'Bora', 'Cem', 45, 'M', 'TR', 'İnşaat', 72, 40000, 1000),
              BeyazYaka('34567890123', 'Deniz', 'Ege', 38, 'F', 'TR', 'Diğer', 36, 22000, 1500),
              BeyazYaka('45678901234', 'Ece', 'Derya', 41, 'F', 'TR', 'Teknoloji', 60, 28000, 2000)]

    for person in people:
        print(person)

    data = [person for person in people if isinstance(person, (Calisan, MaviYaka, BeyazYaka))]

    df = pd.DataFrame({
        "Sınıf": [type(person).__name__ for person in data],
        "TC No": [person.get_tc_no() for person in data],
        "Ad": [person.get_ad() for person in data],
        "Soyad": [person.get_soyad() for person in data],
        "Yaş": [person.get_yas() for person in data],
        "Cinsiyet": [person.get_cinsiyet() for person in data],
        "Uyruk": [person.get_uyruk() for person in data],
        "Sektör": [person.get_sektor() if isinstance(person, Calisan) else 'N/A' for person in data],
        "Tecrübe": [person.get_tecrube() if isinstance(person, Calisan) else 'N/A' for person in data],
        "Maaş": [person.get_maas() if isinstance(person, Calisan) else 'N/A' for person in data],
        "Yıpranma Payı": [person.get_yipranma_payi() if isinstance(person, MaviYaka) else 'N/A' for person in data],
        "Teşvik Primi": [person.get_tesvik_primi() if isinstance(person, BeyazYaka) else 'N/A' for person in data],
        "Yeni Maaş": [person.get_yeni_maas() if isinstance(person, (MaviYaka, BeyazYaka)) else 'N/A' for person in data]
    })

    df.replace('N/A', np.nan, inplace=True)

    print(df.groupby('Sınıf')[['Tecrübe', 'Yeni Maaş']].mean())

    print(df[df['Maaş'] > 15000].shape[0])

    df.sort_values('Yeni Maaş', inplace=True)
    print(df)

    print(df[(df['Sınıf'] == 'BeyazYaka') & (df['Tecrübe'] > 3)])

    print(df[(df['Yeni Maaş'] > 10000) & (df.index >= 2) & (df.index <= 5)][['TC No', 'Yeni Maaş']])

    new_df = df[['Ad', 'Soyad', 'Sektör', 'Yeni Maaş']]
    print(new_df)


if __name__ == '__main__':
    main()
