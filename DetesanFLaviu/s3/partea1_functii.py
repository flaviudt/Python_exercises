"""
PARTEA 1 - FUNCTII

Exerciții - studiu în workshopul de weekend

Pentru toate exercițiile: Apelați funcția de cel puțin 2 ori cu valori diferite pentru a testa.
Dacă funcția are return, printează răspunsul.
"""

"""
1. Funcție care să calculeze și să returneze suma a două numere.
"""

# def suma_Nr(x, y):
#     return x + y
#
# x = int(input('Introduceti x: '))
# y = int(input('Introduceti y: '))
# print(suma_Nr(x,y))
"""
2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar.
"""
# def verificare_nr(numar):
#     if numar % 2 == 0:
#         return True
#     else:
#         return False
#
# #x = int(input('Introduceti nr: '))
# print(verificare_nr(24))


"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""

# def numar_caractere(nume, prenume, prenume2=''):
#     return len(nume + prenume + prenume2)
#
# # x = str(input('Numele: '))
# # y = str(input('Prenumele: '))
# # z = str(input('Prenume2: '))
#
# print(numar_caractere('detesan','flaviu','andrei'))
#

"""
4. Funcție care returnează aria dreptunghiului.
"""

# def aria_dreptunghi(lungime, latime):
#     return lungime * latime
#
# l = int(input('Introduceti lumgimea: '))
# L = int(input('Introduceti latimea: '))
# print(aria_dreptunghi(l,L))


"""
5. Funcție care returnează aria cercului.
"""

# def aria_cercului(raza):
#     import math
#     return math.pi * raza * raza
#
# r = int(input('raza = '))
# print(aria_cercului(r))


"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
"""

# def cauta_caracter(cuvant):
#     if x in cuvant:
#         return True
#     return False
#
# x = str(input('Introduceti un caracter: '))
# print(cauta_caracter('masina'))


"""
7. Funcție fără return, primește un string și printează pe ecran:
Numărul de caractere lower case este x.
Numărul de caractere upper case exte y.
"""

# def count_case(string):
#     lowercase_count = 0
#     uppercase_count = 0
#
#     for char in string:
#         if char.islower():
#             lowercase_count += 1
#         elif char.isupper():
#             uppercase_count += 1
#
#     print(f"Lowercase characters: {lowercase_count}")
#     print(f"Uppercase characters: {uppercase_count}")
#
# # Exemplu
# input_string = "AlaBaLa PortoCalA"
# print(len(input_string))
# count_case(input_string)

"""
8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.
"""

# lista1=[-3,4,-6,13,8,-20,-17,29,20]
# lista2=[]
# def nr_pozitive(lista):
#     for nr in lista:
#         if nr > 0:
#             print(nr)
#             lista2.append(nr)
#     return lista2
#
#
# nr_pozitive(lista1)
# print(lista2)

"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ:
Primul număr x este mai mare decat al doilea număr y.
Al doilea număr y este mai mare decat primul număr x.
Numerele sunt egale.
"""

# def mare_mic(x,y):
#     if x > y:
#         print(f'Primul număr {x} este mai mare decat al doilea număr {y}')
#     elif y > x :
#         print(f'Al doilea numar {y} este mai mare decat primul numar {x}')
#     else:
#         print('Numerele sunt egale')
#
# x = int(input('Introduceti x: '))
# y = int(input('Introduceti y: '))
# mare_mic(x,y)

"""
10. Funcție care primește un număr și un set de numere.
Printează ‘am adaugat numărul nou în set’ + returnează True
Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
"""

# def add_nr_to_set(nr,set_nr):
#     if nr in set_nr:
#         print('Nu am adaugat nr in set.Exista deja')
#         return False
#     print('Am adaugat nr nou in set')
#     set_nr.add(nr)
#     return True
#
# print(add_nr_to_set(3,{1,2,4}))
# print(add_nr_to_set(3,{1,2,3,4}))


"""
11. Funcție care primește o lună din an și returnează câte zile are acea lună.
"""

# from calendar import monthrange
#
# def luna_anului(luna):
#     rezultat = monthrange(2023, luna)
#     print(rezultat)
#     return rezultat[1]
#
# print(luna_anului(3))

# def nr_zile(luna):
#     months = {
#         'IANUARIE': 31,
#         'FEBRUARIE': 28,
#         'MARTIE': 31,
#         'APRILIE': 30,
#         'MAI': 31,
#         'IUNIE': 30,
#         'IULIE': 31,
#         'AUGUST': 31,
#         'SEPTEMBRIE': 30,
#         'OCTOMBRIE': 31,
#         'DECEMBRIE': 30
#     }
#     for key, value in months.items():
#         if luna == key:
#             print(value)
#             return value
# nr_zile('MAI')
#
#
# ## alte variante
# def count_days(month):
#     if month in (1, 3, 5, 7, 8, 10, 12):
#         return 31
#     elif month in (4, 6, 9, 11):
#         return 30
#     elif month == 2:
#         return 28  # 29 daca este an bisect
#     return 0
#
#
# print(count_days(1))
# print(count_days(4))
# print(count_days(2))
#
# def count_days2(month):
#     if month in ('ianuarie', 'martie', 'mai', 'iulie', 'august', 'octombrie', 'decembrie'):
#         return 31
#     elif month in ('aprilie','iunie', 'septembrie', 'noiembrie'):
#         return 30
#     elif month == 'februarie':
#         return 28  # 29 daca este an bisect
#     return 0
#
# print(count_days2('ianuarie'))
# print(count_days2('iunie'))

"""
12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.

În final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""

# def calculator(x,y):
#     a = x+y
#     b = x-y
#     c = x*y
#     d = x/y
#     print(f'Suma: {a}')
#     print(f'Diferenta: {b}')
#     print(f'Inmultirea: {c}')
#     print(f'Impartirea: {d}')
#
# x = int(input('Introduceti x: '))
# y = int(input('Introduceti y: '))
# calculator(x, y)


"""
13. Funcție care primește o listă de cifre (adică doar 0-9).
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""

# lista1 = [1, 3, 1, 5, 9, 7, 7, 5, 5]
#


"""
14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
"""

# def maxim(x,y,z):
#     if x > y and x > z:
#         print(x)
#     elif y > x and y > z:
#         print(y)
#     else:
#         print(z)
#
# x = int(input('Introduceti x: '))
# y = int(input('Introduceti y: '))
# z = int(input('Introduceti z: '))
# maxim(x,y,z)

"""
15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
"""

# suma = 0
# def suma_numerelor(numar):
#     #global suma
#     suma = 0
#     for i in range(numar+1):
#         suma = suma + i
#         i += 1
#         print(suma)
#
# numar = int(input('Introduceti un numar: '))
#
# suma_numerelor(numar)
# print(f'Suma primelor {numar} cifre este {suma}')
#


"""
16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""

# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
#
# def numere_comune(list1, list2):
#     list1 = set(list1)
#     list2 = set(list2)
#     print(list1.intersection(list2))
#
# numere_comune(list1,list2)


"""
17. Funcție care să aplice o reducere de preț.
Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.
"""

# pret = int(input('Pretul produsului este de:'))
# reducere = int(input('Reducerea va fi de:'))
#
#
# def reducere_pret(pret, reducere):
#     if reducere > 100:
#         print('Nu putem aplica o reducere mai mare de 100%')
#     else:
#         pret_redus = pret - reducere / 100 * pret
#         print(f'Pretul produsului dupa aplicarea reduceri de {reducere}% este de {pret_redus} lei')
#
#
# reducere_pret(pret, reducere)
"""
18.Funcție care să afișeze data și ora curentă din România.
(bonus: afișează și data și ora curentă din China)
"""

# from datetime import datetime
#
# # datetime object containing current date and time
# now = datetime.now()
# print(now)
"""
19. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)
"""

import datetime

dt = datetime.datetime
now = dt.now()

timeleft = dt(year = 2023, month = 12, day = 25) - dt(year=now.year, month=now.month, day=now.day)
print(timeleft.days)