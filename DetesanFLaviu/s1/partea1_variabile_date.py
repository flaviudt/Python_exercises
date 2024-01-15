# # Partea 1 - Setup, Variabile, Tipuri de date
#
# # Exerciții - studiu în workshopul de weekend
#
# # 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
#
# # variabila = zona de memorie care stocheaza datele
#
# # 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
# # string
# masina = "Dacia 1310"
#
# # int
# nr1 = 20
#
# # float
# nr2 = 17.71
#
# # bool
# nr3 = True
#
# # Observație: Valorile vor fi alese de tine după preferințe.
#
# # 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
# print(type(masina))
# print(type(nr1))
# print(type(nr2))
# print(type(nr3))
#
# # 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# # Verifică tipul acesteia.
# nr2 = round(nr2)
# print(nr2)
# print(type(nr2))
# # 5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
# # Rezolvă nepotrivirile de tip prin ce modalitate dorești.

# print(f"{masina} este o masina de epoca")
# print(f"Numarul meu preferat este {nr1} ")
# print(f"Numarul {nr2} a fost anterior 17.71")
# print(f"Totul este {nr3} - Adevarat")
#
# # 6. Citește de la tastatură:
# # numele;

# nume = input('Numele va rog:')
#
# # prenumele.
# prenume = input('Prenumele va rog:')
#
# #     Afișează: 'Numele complet are x caractere'.
#
# print(f'Numele complet are  {len(nume+prenume)} caractere' )


# # 7. Citește de la tastatură:
# # lungimea;
# lungime = float(input('Lungimea:'))
#
# # lățimea.
# latime = float(input('Latimea:'))
#
# #    Afișează: 'Aria dreptunghiului este x'.
# aria = latime*lungime
# print(f'Aria dreptunghiului este {aria}')


# # 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# # afișează de câte ori apare cuvântul 'the';
# # Printează rezultatul.
# my_str = 'Coral is either the stupidest animal or the smartest rock'
# print(my_str.count('the'))

# # 9. Același string:
# # Folosește un assert ca să verifici dacă acest string conține doar numere.
# my_str = 'Coral is either the stupidest animal or the smartest rock'
# assert my_str.isnumeric()

# str1 = "Coral is either the stupidest animal or the smartest rock 1"
# assert str1.isnumeric()

# # 10. Exercițiu:
# # citește de la tastatură un string de dimensiune impară;
# # afișează caracterul din mijloc.
# my_str2= input('Introduceti textul:')
# y = len(my_str2)
# if y % 2 == 1:
#   #  print(my_str2[int(y/2)])
#     print(my_str2[y//2]) #floor divizion 7//2 = 3


# # 11. Folosind o singură linie de cod :
# # citește un string de la tastatură (ex: 'alabala portocala');
# # salvează fiecare cuvânt într-o variabilă;
# # printează ambele variabile pentru verificare.
# #my_str3, my_str4 = print(input('Introduceti a:')), print(input('Introduceti b:'))
#
# print(input('Introduceti textul:').split()) # folosind lista
# a, b = input('Introduceti textul:').split()
# print(a)
# print(b)


# # 12. Exercițiu:
# # citește un string de la tastatură (ex: alabala portocala);
# # salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
# # capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
# my_str5 = input('Introduceti textul:')
# b = my_str5[0]
# print(b)
# c = my_str5[1:-1].replace(b,b.upper())
# print(c)
# print(b + c + my_str5[-1])

# 13. Exercițiu:
# citește un user de la tastatură;
# citește o parolă;
# afișează: 'Parola pt user x este ***** și are x caractere';
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
#
user = input('Introduvceti userul:')
parola = input('introduceti parola:')
b = '*' * len(parola)

print(f'Parola pt {user} este {b} si are {len(parola)} caractere')

# eg: parola abc => ***
#       parola abcd => ****
