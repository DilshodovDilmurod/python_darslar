class Avto:
    """Avtolar classi"""
    def __init__(self, model, rang, korobka, narx, yil):
        self.model = model 
        self.rang = rang
        self.korobka = korobka
        self.narx = narx
        self.yil = yil
        self.kilometr = 0
    def get_info(self):
        return f"{self.korobka.title()} {self.rang} {self.model.title()} {self.yil}-yilda {self.narx}$ ga ishlab chiqarilgan"
    def update_km(self, km):
        self.kilometr = km
class Avto_Salon:
    def __init__(self, name, adres):
        self.name = name
        self.adres = adres
        self.avtolar = []
    def add_avto(self, avto):
        self.avtolar.append(avto)
    def get_avto(self):
        return [avto.get_info() for avto in self.avtolar]

avto1 = Avto("cobalt", "oq", "mexanik",40000, 2020)
salon = Avto_Salon("GM", "urganch")
salon.add_avto(avto1)
print(salon.get_avto())