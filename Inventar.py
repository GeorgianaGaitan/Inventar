

d = {
    "Mere":(2,50)

}
class Inventar:
    def __init__(self):
        self.produse ={}

    def adauga_produse(self, nume, pret, cantitate):
        # produs = [nume, pret, cantitate]
        self.produse[nume] = (pret, cantitate)

    def verifica_stoc(self, nume, cantitate):
        if self.produse["Mere"][1] >= cantitate:
            return True
        else:
            return False

    def scade_stoc(self, nume, cantitate):
        #"mere" = (2,50)
        pret_original = self.produse[nume]
        cantitate_originala = self.produse[nume][1]
        if cantitate_originala < cantitate:
            pass
        else:
            self.produse[nume] = (pret_original, cantitate_originala-cantitate)

    def afiseaza_produse(self):
        print("Inventar:")
        for prod in self.produse.keys():
            pret = self.produse[prod][0]
            stocul = self.produse[prod][1]
            print("Produs: {}, pret: {}, stoc: {}".format(prod, pret, stocul))

class Client:
    def __init__(self, nume: str= "Lipsa_Nume"):
        self.nume = nume
        self.cos = {}

    def adauga_in_cos(self, nume_produs, cantitate):
        self.cos[nume_produs] = cantitate
    def afiseaza_cos(self):
        print("Cosul clientului {}".format(self.nume))
        for prod in self.cos:
            print("Produsul: {}, cantitatea dorita; {}".format(prod, self.cos[prod]))


class MagazinDeCumparaturi:
    def __init__(self, inventar: Inventar):
        self.inventar = inventar
    def proceseaza_cumparaturi(self, client: Client):
        total = 0
        for produs in client.cos:
            if produs in self.inventar.produse:
                cantitate = client.cos[produs]
                if self.inventar.verifica_stoc(produs, cantitate):
                    pret_produs = self.inventar.produse[produs][0]
                    total = total + pret_produs * cantitate
                    self.inventar.scade_stoc(produs, cantitate)
            else:
                print("Nu avem acel produs in inventar: {}".format(produs))
        return total

    def afiseaza_stare_magazin(self):
        print("In magazin avem:")
        self.inventar.afiseaza_produse()




i = Inventar()
i.adauga_produse("Mere", 2, 50)
i.scade_stoc("Mere", 50)
i.afiseaza_produse()
c = Client("Vlad")
c.adauga_in_cos("Mere", 10)
c.adauga_in_cos("Caise",30)
c.afiseaza_cos()

magazin = MagazinDeCumparaturi(i)
total = magazin.proceseaza_cumparaturi(c)
print("Totalul clientului {} este {}".format(total, c.nume))
magazin.afiseaza_stare_magazin()