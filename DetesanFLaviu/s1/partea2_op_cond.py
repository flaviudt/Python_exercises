# Partea 2 - Operatori, condiționale

# Exerciții - studiu în workshopul de weekend

# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.

# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.


# # 2. Verifică și afișează dacă x este număr natural sau nu.
# x = int(input('Introduceti valorea lui X:'))
# if x > 0:
#     print('X este nr natural')
# else:
#     print('X nu este nr natural')

# # 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
# x = int(input('Introduceti valorea lui X:'))
# if x > 0:
#     print('X este nr pozitiv')
# elif x < 0:
#     print('X  este nr negativ')
# else:
#     print('X este numar neutru ')
#
#
# # 4. Verifică și afișează dacă x este între -2 și 13.
# x = int(input('Introduceti valorea lui X:'))
# if x >= -2 & x <= 13:
#     print('X este intre -2 si 13 ')
# else:
#     print('X nu este intre -2 si 13')


# # 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
# x = int(input('Introduceti valorea lui X:'))
# y = int(input('Introduceti valorea lui Y:'))
# z = x - y
# if z < 5:
#     print(f'X - Y este {z} (<5)')
# else:
#     print('X - Y > 5')


# # 6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
# x = int(input('Introduceti valorea lui X:'))
# if not(5 <= x <= 27):
#     print('X nu se afla in intervalul 5-27')
# else :
#     print('X se afla in intervalul 5-27')


# # 7.
# # x și y (int)
# # Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
# x = int(input('Introduceti valorea lui X:'))
# y = int(input('Introduceti valorea lui Y:'))
#
# if x == y:
#     print('Numerele sunt egale')
# elif x > y:
#     print('X > Y')
# else:
#     print('X < Y')

# # 8.
#
# # x, y, z - laturile unui triunghi.
# # Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
# x = int(input('Introduceti valorea lui X:'))
# y = int(input('Introduceti valorea lui Y:'))
# z = int(input('Introduceti valorea lui Z:'))
#
# if x == y == z:
#     print('Triunghi echilateral')
# elif x == y or x == z or y == z:
#     print('triunghi isoscel')
# else:
#     print('triunghi oarecare')


# # 9. Citește o literă de la tastatură.
# #     Verifică și afișează dacă este vocală sau nu.
# x = str(input('Introduceti o litera:'))
#
# if x =='a' or x =='e' or x =='i' or x =='o' or x == 'u':
#     print('Vocala')
# else:
#     print('Consoana')



# 10.Transformă și printează notele din sistem românesc în  >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
# x = float(input('Introduceti nota:'))
#
# if x >= 9:
#     print('A')
# elif 8 <= x < 9:    # x >= 8 and x < 9
#     print('B')
# elif 7 <= x < 8:
#     print('C')
# elif 6 <= x < 7:
#     print('D')
# elif 4 <= x < 6:
#     print('E')
# else:
#     print('F')


# #11.Verifică dacă x are minim 4 cifre (x e int).
# #(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
# x = int(input('Introduceti numarul X:'))
#
# if len(str(x)) >= 4:
#     print('X are minim 4 cifre')
# else:
#     print('X nu are minim 4 cifre')

# # 12.Verifică dacă x are exact 6 cifre.
# x = int(input('Introduceti numarul X:'))

## nu este valabil pt numere negative
# if len(str(x)) == 6:
#     print('X are exact 6 cifre')
# else:
#     print('X nu are 6 cifre')

## pentru numere negative
# if 100000 <= abs(x) < 1_000_000:
#     print('X are exact 6 cifre')
# else:
#     print('X nu are exact 6 cifre')

# # 13.Verifică dacă x este număr par sau impar (x e int).
# x = int(input('Introduceti numarul X:'))
#
# if x % 2 == 0:
#     print('X este par')
# else:
#     print('X este impar')


# 14.      x, y, z (int)
# Afișează care este cel mai mare dintre ele?
# x = int(input('Introduceti valorea lui X:'))
# y = int(input('Introduceti valorea lui Y:'))
# z = int(input('Introduceti valorea lui Z:'))
#
# if x > z and x > y:
#     print('X este cel mai mare')
# elif z > x and z > y:
#     print('Z este cel mai mare')
# elif y > z and y > x :
#     print('Y este cel mai mare')
# elif x == y and x > z:
#     print('X = Y si > Z')
# elif y == z and y > x :
#     print('Y = Z si > X')
# elif x == z and x > y:
#     print('X = Z si > Y')
# else:
#     print('X = Y = Z')


# # 15.
# # x, y, z - reprezintă unghiurile unui triunghi
# # Verifică și afișează dacă triunghiul este valid sau nu.

# x = int(input('Introduceti masura unghilui lui X:'))
# y = int(input('Introduceti masura unghilui lui Y:'))
# z = int(input('Introduceti masura unghilui lui Z:'))
#
# if ((x + y + z) != 180) or (x == 0 or y == 0 or z == 0):
#     print('Triunghi invalid')
# else:
#     print('triunghi valid')

# 16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# Citește de la tastatură un int x
# Afișează stringul fără ultimele x caractere
# Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'

# str1 = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('Introduceti valorea lui X:'))
# str2 = str1[0:-x]
# print(str2)
#
# if x != 0:
#     print(str2)
# else:
#     print('Coral is either the stupidest animal or the smartest rock')


# 17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
# str1 = 'Coral is either the stupidest animal or the smartest rock'
# str2 = str1[:5] + str1[-5:]
# print(str2)


# # 18. Același string.
# # Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
# # Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
# # output: 'Coral is either the stupidest animal or the smartest'
# str1 = 'Coral is either the stupidest animal or the smartest rock'
# index_s = str1.index('rock')
# print(index_s)
# print(str1[:index_s])
#


# 19. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Ia numărul ghicit de la utilizator
# Verifică și afișează dacă utilizatorul a ghicit
# Vei avea 3 opțiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# Ai ghicit. Felicitări! Ai ales x si zarul a fost y.

# import random
# nr_random = random.randint(1, 6)
# print(nr_random)
# dice_roll = int(input('Introdu un numar de la 1 la 6: '))
# if dice_roll == nr_random:
#     print(f'Ai ghicit. Felicitări! Ai ales {dice_roll} si zarul a fost {nr_random}.')
# elif dice_roll < nr_random:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {dice_roll} dar a fost {nr_random}.')
# else:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {dice_roll} dar a fost {nr_random}.')


# 20.  Citește de la tastatură un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
## v1
x = str(input('Introduceti un text:'))
first_char = x[0]
last_char = x[-1]
print(first_char, last_char)
assert first_char.casefold() == last_char.casefold()

## v2

str_input = input("Introduceti un string: ")
assert str_input[0].lower() == str_input[-1].lower()

# 21. Având stringul '0123456789'
# Afișează doar numerele pare
# Afișează doar numerele impare
# (hint: folosește slicing, controlează din pas)

# cifre = '0123456789'
# cifre_pare = cifre[0::2]
# cifre_impare = cifre[1::2]
#
# print(cifre_pare)
# print(cifre_impare)

