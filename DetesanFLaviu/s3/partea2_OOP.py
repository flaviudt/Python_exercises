"""
PARTEA 2 - OOP: Clase & Obiecte
"""

"""
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria
diametru()
circumferinta()
"""
# import math
# class Cerc:
#     # constructor
#     def __init__(self, raza, culoare):
#         # atribute
#         self.raza = raza
#         self.culoare = culoare
#     # metode
#
#     def descrie_cerc(self):
#         print(f'Raza: {self.raza}')
#         print(f'Culoarea cercului: {self.culoare}')
#
#     def aria_cerc(self):
#         aria = math.pi * self.raza ** 2
#         print(f'Aria este: {aria}')
#         return aria
#
#     def diametru_cerc(self):
#         diametru = 2 * self.raza
#         print(f'Diametrul cercului:{diametru}')
#         return diametru
#
#     def circumferinta_cerc(self):
#         circumferinta = math.pi * 2 * self.raza
#         print(f'Circumferinta cercului: {circumferinta}')
#         return circumferinta
#
#
# cerc1 = Cerc(3, 'albastru')
#
# cerc1.descrie_cerc()
# cerc1.aria_cerc()
# cerc1.diametru_cerc()
# cerc1.circumferinta_cerc()

"""
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().
"""

# class Dreptunghi:
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie_dreptunghi(self):
#         print(f'Lungime: {self.lungime}')
#         print(f'Latime: {self.latime}')
#         print(f'Culoare: {self.culoare}')
#
#     def aria_dreptunghi(self):
#         aria = self.lungime * self.latime
#         print(f'Aria dreptunghiului este:{aria}')
#         return aria
#
#     def perimetru_dreptunghi(self):
#         perimetru = 2 * (self.lungime + self.latime)
#         print(f'Perimetrul dreptunghiului este: {perimetru}')
#         return perimetru
#
#     def schimba_culoarea(self, noua_culoare):
#         self.culoare = noua_culoare
#         print(f'Noua culoare este: {noua_culoare}')
#
#
# dreptunghi1 = Dreptunghi(5, 7, 'verde')
# dreptunghi1.descrie_dreptunghi()
# dreptunghi1.aria_dreptunghi()
# dreptunghi1.perimetru_dreptunghi()
# dreptunghi1.schimba_culoarea('albastru')

"""
3. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
"""

# class Angajat:
#     # constructor
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     #metode
#     def descrie_angajat(self):
#         print(f'Numele si prenumele angajatului: {self.nume} {self.prenume}')
#         print(f'Salariul: {self.salariu}')
#
#     def nume_complet(self):
#         print(f'Numele si prenumele angajatului: {self.nume} {self.prenume}')
#
#     def salariu_lunar(self):


"""
4. Clasa Cont
   Atribute: iban, titular_cont, sold
   Constructor pentru toate atributele
   Metode:
afisare_sold() - Titularul x are în contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
"""

# class Cont:
#     # constructor
#     def __init__(self ,iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#     # metode
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} $')
#
#     def debitare_cont(self, suma):
#         self.sold = self.sold - suma
#         print(f'{self.titular_cont} a cheltuit {suma} $ si mai are suma de {self.sold} $')
#
#     def creditare_cont(self, suma):
#         self.sold = self.sold + suma
#         print(f'{self.titular_cont} a adaugat {suma} $ si are acum suma de {self.sold} $')
#
#
# cont1 = Cont('ROBT01','Popescu Maria',1000)
# cont1.afisare_sold()
# cont1.debitare_cont(500)
# cont1.creditare_cont(5000)
#
# cont2 = Cont('ROBT02','Popescu Ion',100)
# cont2.afisare_sold()
# cont2.debitare_cont(5)
# cont2.creditare_cont(30_000)


"""
5. Clasa Factură
     Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
     Constructor: toate atributele, fără serie
     Metode:
schimbă_cantitatea(cantitate)
schimbă_prețul(pret)
schimbă_nume_produs(nume)
generează_factura() - va printa tabelar dacă reușiți

Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total
Telefon |      7       |       700       | 49000

Indiciu pentru dată: https://www.geeksforgeeks.org/get-current-date-using-python/
"""

# Import date class from datetime module
from datetime import date
from tabulate import tabulate


class Factura:
    seria = 'PYTHON'

    # constructor
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    # metode
    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate = cantitate_noua
        print(f'Cantitare: {self.cantitate}')

    def schimba_pretul(self, pret_nou):
        self.pret_buc = pret_nou
        print(f'Noul pret: {self.pret_buc}')

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        print(f'Noul nume al produsului: {self.nume_produs}')

    def genereaza_factura_tabel(self):
        print(f'Factura seria {self.seria} numar {self.numar}')
        print(f'Data: {date.today()}')
        table = [['Produs', 'Cantitate', 'Pret bucata', 'Total'],
                 [self.nume_produs, self.cantitate, self.pret_buc, self.pret_buc * self.cantitate]]
        print(tabulate(table) + '\n')

    def genereaza_factura(self):
        print(f'Factura seria {self.seria} numar {self.numar}')
        print(f'Data: {date.today()}')
        table = [['Produs', 'Cantitate', 'Pret bucata', 'Total'],
                 [self.nume_produs, self.cantitate, self.pret_buc, self.pret_buc * self.cantitate]]
        for row in table:
            print('|{:^15}|{:^15}|{:^15}|{:^15}|'.format(*row))
        print('\n')
###  : stanga-dreapta
###  ^ centered
###  > right-aligned
###  < left-aligned
###  https://learnpython.com/blog/print-table-in-python/


factura1 = Factura(1234, 'Tricou', 44, 100)

# factura1.schimba_cantitatea(200)
# factura1.schimba_pretul(150)
# factura1.schimba_nume_produs('Tricou rosu')

factura1.genereaza_factura()
factura1.genereaza_factura_tabel()

factura2 = Factura(500342, 'Bomboane', 100_000, 0.3)
factura2.genereaza_factura()
factura2.genereaza_factura_tabel()

