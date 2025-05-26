import pytest
from Django_inventar.Inventar import Inventar, Client

@pytest.fixture
def Inventar():
    i = Inventar()
    return i
@pytest.fixture
def client():
    c = Client()
    return c

def test_inventar_verifica_stoc():
    i = Inventar()
    i.adauga_produse("Mere",2,50)
    assert i.verifica_stoc("Mere",60) == False

def test_adauga_produse():
    i = Inventar()
    i.adauga_produse("Mere",2,50)
    assert i.verifica_stoc("Mere",60) == True

def test_adauga_produs():
    nume = "Mere"
    pret = "5"
    cantitate = 100
    inventar.adauga_produse(nume,pret,cantitate)
    assert inventar.produse[nume] == [pret, cantitate]
def test_scade_stoc(inventar):
    nume = "Mere"
    pret = "5"
    cantitate = 100
    inventar.adauga_produse("Mere",2,50)
    inventar.scade_stoc("Mere",2,50)
    assert inventar.produse(nume) == [pret, cantitate]

def test_client_adauga_in_cos(client):
    nume_prod = "Mere"
    cantitate = 100
    client.adauga_in_cos(nume_prod,cantitate)
    assert client.produse(nume_prod) == 50

def test_proceseaza_cumparaturi(client, inventar):
    inventar().adauga_produse("Pere", 4, 500)
    inventar().adauga_produse("Mere",2,300)
    client.adauga_produse("Mere",30)
    client.adauga_produse("Pere", 50)
    assert magazin.proceseaza_cumparaturi(client) == 260
    client.adauga_produse("Mere",350)
    assert inventar.produse["Mere"]
    magazin.proceseaza_cumparaturi(client)
    assert inventar.produse["Mere"] == (2,300)



