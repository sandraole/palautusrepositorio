KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self._validoi_kapasiteetti(kapasiteetti)
        self._validoi_kasvatuskoko(kasvatuskoko)

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def _validoi_kapasiteetti(self, kapasiteetti):
        if not isinstance(kapasiteetti, int) or kapasiteetti <= 0:
            raise ValueError("Kapasiteetti pitää olla positiivinen kokonaisluku")

    def _validoi_kasvatuskoko(self, kasvatuskoko):
        if not isinstance(kasvatuskoko, int) or kasvatuskoko <= 0:
            raise ValueError("Kasvatuskoko pitää olla positiivinen kokonaisluku")

    def _luo_lista(self, koko):
        return [0] * koko

    def _laajenna_lista(self):
        uusi_koko = self.alkioiden_lkm + self.kasvatuskoko
        uusi_lista = self._luo_lista(uusi_koko)
        self._kopioi_lista(self.ljono, uusi_lista)
        self.ljono = uusi_lista

    def _kopioi_lista(self, vanha_lista, uusi_lista):
        for i in range(self.alkioiden_lkm):
            uusi_lista[i] = vanha_lista[i]

    def kuuluu(self, x):
        return x in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, x):
        if self.kuuluu(x):
            return False

        if self.alkioiden_lkm == len(self.ljono):
            self._laajenna_lista()

        self.ljono[self.alkioiden_lkm] = x
        self.alkioiden_lkm += 1
        return True

    def poista(self, x):
        if x not in self.ljono[:self.alkioiden_lkm]:
            return False

        for i in range(self.alkioiden_lkm):
            if self.ljono[i] == x:
                self._poista_alkio(i)
                break
        return True

    def _poista_alkio(self, index):
        for i in range(index, self.alkioiden_lkm - 1):
            self.ljono[i] = self.ljono[i + 1]
        self.ljono[self.alkioiden_lkm - 1] = 0
        self.alkioiden_lkm -= 1

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        uusi_joukko = IntJoukko()
        for alkio in a.to_int_list() + b.to_int_list():
            uusi_joukko.lisaa(alkio)
        return uusi_joukko

    @staticmethod
    def leikkaus(a, b):
        uusi_joukko = IntJoukko()
        a_alkiot = a.to_int_list()
        b_alkiot = b.to_int_list()

        for alkio in a_alkiot:
            if alkio in b_alkiot:
                uusi_joukko.lisaa(alkio)
        return uusi_joukko

    @staticmethod
    def erotus(a, b):
        uusi_joukko = IntJoukko()
        for alkio in a.to_int_list():
            uusi_joukko.lisaa(alkio)
        for alkio in b.to_int_list():
            uusi_joukko.poista(alkio)
        return uusi_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        alkiot = ", ".join(str(self.ljono[i]) for i in range(self.alkioiden_lkm))
        return f"{{{alkiot}}}"
