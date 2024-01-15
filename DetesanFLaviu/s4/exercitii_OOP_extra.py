"""
EXERCITII BONUS - OOP - EXTRA
"""
from abc import abstractmethod, ABC

"""
1. 
a. Defineste clasa User.
Clasa User va avea urmatoarele atribute:
username (public) - se seteaza in constructor
email (public) - se seteaza in constructor
password (privat) - Nu primim atribut pentru el in constructor,
ci il initializam noi cu None (self.__password == None).

b. Implementeaza proprietatea password care va incapsula atributul privat
password.
Va avea:
- getter:
In getter verificam daca parola a fost setata (daca are valoare).
Daca are valoare, atunci vom returna ***, unde numarul de * va fi egal
cu lungimea parolei.
Daca nu e setata, atunci afisam un mesaj ca parola nu e setata.
- setter:
In setter vom verifica, inainte sa setam parola, ca aceasta indeplineste
urmatoarele conditii:
    -- are minim 10 caractere
    -- are cel putin o litera mare
Daca aceste conditii se indeplinesc atunci setam parola.
Daca nu, afisam un mesaj corespunzator pentru fiecare situatie.

c. Metode:
- Metoda login: verificam ca user-ul are atat username, email si parola.
Daca are, atunci afisam mesajul "Conectat".
Daca nu, afisam mesajul "Lipsesc credentiale de conectare. Nu va putem conecta"

d. Asigura-te ca creezi cel putin doua obiecte din clasa User.
Afiseaza toate atributele/metodele/proprietatile.
"""

# class User:
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#         self.__password = None
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.getter
#     def password(self):
#         if self.__password is None:
#             print('Parola nu e setata.')
#         else:
#             rezultat = '*' * len(self.__password)
#             #print('*' * len(self.__password))
#             return rezultat
#
#     @password.setter
#     def password(self, new_password):
#         if new_password is not None and len(new_password) >= 10:
#             for char in new_password:
#                 if char.isupper():
#                     self.__password = new_password
#                     break
#             else:
#                 print('Nu avem majuscula')
#         else:
#             print('Parola noua nu are 10 caractere')
#
#     def login(self):
#         if self.username is not None and self.email is not None and self.__password is not None:
#             print('Conectat')
#         else:
#             print('Lipsesc credentiale de conectare. Nu va putem conecta')
#
#
#
#
# obiect1 = User('flaviu','email1@email')
# print(obiect1.email)
# print(obiect1.username)
# print(obiect1.password)
# obiect1.password = 'Q1234567AA89gg00'
# print(obiect1.password)
# obiect1.login()

"""
2.
a. Defineste clasa abstracta Person.
Metode abstracte: wake_up, sleep, eat.
Metoda: describe -> afiseaza mesajul "O persoana se trezeste, mananca si doarme."

b. Defineste clasa Student.
Clasa Student implementeaza clasa abstracta Person.
Atribute in constructor: name, university, grade.
Metode describe -> afiseaza SI mesajul:
Studentul x, studiaza la universitatea y si are nota generala z.

c. Defineste clasa Employee.
Clasa Employee implementeaza cls abstracta Person.
Atribute in constructor: name, experience, salary.
Salary este un atribut privat!
Metoda describe -> afiseaza SI mesajul:
Angajatul x lucreaza de y ani.

d. Creeaza proprietatea salary care sa incapsuleze atributul privat salary.
"""
from abc import abstractmethod, ABC


class Person(ABC):

    @abstractmethod
    def wake_up(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def descrie(self):
        print('O persoana se trezeste, mananca si doarme!')


class Student(Person):

    def __init__(self, name, university, grade):
        self.name = name
        self.university = university
        self.grade = grade

    def descrie(self):
        super().descrie()
        print(f'Studentul {self.name} studiaza la universitatea {self.university} si are nota generala {self.grade}.')

    def wake_up(self):
        print(f'Studentul {self.name} se trezeste la ora 7.')

    def sleep(self):
        print(f'Studentul {self.name} se pune la somn la ora 23.')

    def eat(self):
        print(f'Studentul {self.name} mananca 3 mese/zi')


class Employee(Person):

    def __init__(self, name, experience, salary):
        self.name = name
        self.experience = experience
        self.__salary = salary

    def descrie(self):
        super().descrie()
        print(f'Angajatul {self.name} lucreaza de {self.experience} ani.')

    def wake_up(self):
        print(f'Angajatul {self.name} se trezeste la ora 6.')

    def sleep(self):
        print(f'Angajatul {self.name} se pune la somn la ora 22.')

    def eat(self):
        print(f'Angajatul {self.name} mananca 4 mese/zi')

    @property
    def salary(self):
        return self.__salary

    @salary.getter
    def salary(self):
        print(f'Salariul angajatului {self.name} este {self.__salary}')
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print(f'Am marit salariul. Noul salariu este {new_salary}')
        else:
            self.__salary = new_salary
            print(f'Am micsorat salariul. Noul salariu este {new_salary}')


student1 = Student('Ion', 'UBB', 9)
student1.descrie()
student1.wake_up()
student1.eat()
student1.sleep()

angajat1 = Employee('Stefan', 4, 4500)
angajat1.descrie()
angajat1.wake_up()
angajat1.eat()
angajat1.sleep()

angajat1.salary
angajat1.salary = 5000
angajat1.salary
angajat1.salary = 2000
angajat1.salary
angajat1.salary = 8000
angajat1.salary

