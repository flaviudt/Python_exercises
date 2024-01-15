# OOP - advance
#
# Exerciții - studiu în workshopul de weekend
#
# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

from abc import abstractmethod, ABC


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am colturi')


# forma1 = FormaGeometrica  ## eroare
# forma1.descrie()


#
# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură
#
# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: Latura are valoarea: {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, new_latura):
        print(f'Setter: Noua valoare: {new_latura}')
        self.__latura = new_latura

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters valoarea')
        self.__latura = None

    def aria(self):
        aria = self.__latura * self.__latura
        print(f'Aria = {aria}')
        return aria


# obiect1 = Patrat(4)
# obiect1.descrie()
# print(obiect1.latura)
# obiect1.latura = 5
# obiect1.aria()
#
# del obiect1.latura
# print(obiect1.latura)

#
# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
#
#
class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza are valoarea: {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, new_raza):
        print(f'Setter: Noua valoare: {new_raza}')
        self.__raza = new_raza

    @raza.deleter
    def raza(self):
        print(f'Deleter: Am sters valoarea')
        self.__raza = None

    def aria(self):
        aria = self.PI * self.__raza ** 2
        print(f'Aria = {aria}')
        return aria

    def descrie(self):
        print('Eu nu am colturi')


obiect2 = Cerc(5)
obiect2.descrie()
print(obiect2.raza)
obiect2.raza = 6
del obiect2.raza
obiect2.raza = 10
obiect2.aria()

print(obiect2.PI)

# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
#
# Creează un obiect de tip Pătrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui
#
# 3. Actualizează proiectul pe github facand un push la noul cod
# În Folderul de teme ajunge să pui doar linkul cu proiectul tău public
#
# Sa avem github-ul instalat și să ne incarcam în acesta fișierele python lucrate în workshop-urile de weekend.
#
