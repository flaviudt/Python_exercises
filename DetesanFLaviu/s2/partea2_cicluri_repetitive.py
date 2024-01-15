"""

PARTEA 2: CICLURI REPETITIVE

Exerciții - studiu în workshopul de weekend

"""

"""
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'] 

Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.
"""

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# # for
# for i in range(0,len(masini)):
#     print(f'Preferata mea este {masini[i]}')
#
# # for each
# for masina_preferata in masini:
#     print(f'Masina mea preferata este {masina_preferata}')
#
# #while
# x = 0
# while x < len(masini):
#     print(f'Masina preferata: {masini[x]}')
#     x += 1


"""
2. Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
"""

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# masina_maj = masini[1:-1]
# print(masina_maj)
#
# for masina_maj in masini:
#     print(masina_maj.upper())
#
# else:
#     print(masini)
#
# masini_final = masini[0] + masina_maj + masini[-1]
# print(masini_final)

## v2 for clasic - functionala
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# for i in range(0, len(masini)):
#     if i == 0 or i== len(masini)-1:
#         continue
#     masini[i] = masini[i].upper()
#
# else:
#     print(masini)


"""
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘
"""

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# ## for each
# for masina_dorita in masini:
#     print(masina_dorita)
#     if masina_dorita == 'Mercedes':
#         print('Am gasit masina dorita')
#         break
#     else:
#         print('Nu am gasit masina dorita.Mai cautam')
#
# # for clasic
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in range(0,len(masini)):
#     if masini[i] == 'Mercedes':
#         print("Am gasit masina dorita de dumneavoastra")
#         break
#     print(f'Am gasit masina {masini[i]}. Mai cautam')


## while
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# i = 0
# while i < len(masini):
#     print(masini[i])
#     if (masini[i]) == 'Mercedes':
#         print('Am gasit masina dorita')
#         break
#     print(f'Am gasit masina {masini[i]}. Mai cautam')
#     i += 1


"""
4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# for masina_dorita in masini:
#     print(masina_dorita)
#     if masina_dorita == 'Trabant' or masina_dorita == 'Lăstun':
#         continue
#     print(f'S-ar putea sa va placa masina: {masina_dorita}')


"""
5. Modernizează parcul de mașini:

Crează o listă goală, masini_vechi.
Iterează prin mașini.
Când găsesti Lăstun sau Trabant:
Salvează aceste mașini în masini_vechi.
Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
Printează Modele vechi: x.
Modele noi: x.
"""
### v1
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for masina_dorita in masini:
#     if masina_dorita == 'Lăstun' or masina_dorita =='Trabant':
#         masini_vechi.append(masina_dorita)
#         masini.remove(masina_dorita)
#         masini.append('Tesla')
#
# print(masini_vechi)
# print(masini)
### v2
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for m in masini:
#     if m == 'Trabant' or m == 'Lăstun':
#         masini_vechi.append(m)
#         masini.remove(m)
#         masini.append('Tesla')
# print(f"\nModelele vechi: {masini_vechi}")
# print(f"\nModele noi: {masini}")
#



"""
6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.

Prezintă doar mașinile care se încadrează în acest buget.
Iterează prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
Iterează prin listă.
"""

# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
#
# ## accesam cheile din dictionar folosind keys()
# for cheie in pret_masini.keys():
#     print(cheie)
#
# ## accesam valorile din dictionar folosind values()
# for valoare in pret_masini.values():
#     print(valoare)
#
# ## accesam cheile si valorile din dict folosind items()
# for cheie,valoare in pret_masini.items():
#     print(cheie, valoare)
#
# for masina, pret in pret_masini.items():
#     print(f'Masina {masina} are pretul {pret}')
#     if pret < 15000:
#         print(f' Pentru un buget de sub 15000 euro puteți alege mașină {masina}')
#     else:
#         print(f'Nu va incadrati in buget pentru masina {masina} care costa {pret}')


"""
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# nr_trei = 0
# for nr in numere:
#     if nr == 3:
#         nr_trei += 1
# print(nr_trei)

"""
8. Aceeași listă:
Iterează prin ea
Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# suma = 0
# for nr in numere:
#     print(nr)
#
#     suma += nr
# print(suma)


"""
9. Aceeași listă:
Iterează prin ea.
Afișază cel mai mare număr (nu ai voie să folosești max).
"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# maxim = numere[0]
# for nr in numere:
#     if nr > maxim:
#         maxim = nr
# print(maxim)

"""
10. Aceeași listă:
Iterează prin ea.
Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
Afișază noua listă.
"""
#numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# ## varianta for
# for index in range(0, len(numere)):
#     if numere[index] > 0:
#         numere[index] = numere[index] * -1
# print(numere)


# foreach
# my_list = []
#
# for numar in numere:
#     if numar > 0:
#         nr_negativ = numar * -1
#         my_list.append(nr_negativ)
#     else:
#         my_list.append(numar)
# print(my_list)

"""
11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere 
Populează corect celelalte liste
Afișează cele 4 liste la final
"""
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
#
# for numar in alte_numere:
#     if numar > 0 :
#         numere_pozitive.append((numar))
#     else:
#         numere_negative.append((numar))
#     if numar % 2 == 0:
#         numere_pare.append((numar))
#     else:
#         numere_impare.append(numar)
#
# print(f'Numerele pozitive sunt: {numere_pozitive}')
# print(f'Numerele negative sunt: {numere_negative}')
# print(f'Numerele pare sunt: {numere_pare}')
# print(f'Numerele impare sunt: {numere_impare}')


""""
12. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
"""
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#
# # Bubble sort in Python
# for i in range(len(alte_numere)):
#     for j in range(0, len(alte_numere) - i - 1):
#         if alte_numere[j] > alte_numere[j + 1]:
#             temp = alte_numere[j]
#             alte_numere[j] = alte_numere[j + 1]
#             alte_numere[j + 1] = temp
#
# print(alte_numere)

"""
13. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!
"""

# import random
# numar_secret = random.randint(1, 30)
# print(numar_secret)
# numar_ghicit = None
#
# while numar_ghicit != numar_secret:
#     numar_ghicit = int(input('Alege un numar: '))
#     if numar_ghicit < numar_secret:
#         print('nr secret e mai mare')
#     elif numar_ghicit > numar_secret:
#         print('nr secret e mai mic')
#     else:
#         print('Ai ghicit')

"""
14. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
"""
#
# n = int(input('Introduceti un nr: '))
#
# for i in range(1, n+1):
#     print(str(i)*i)
"""
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
"""

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for lista_cifre in tastatura_telefon:
    for cifra in lista_cifre:
        print(f"Cifra curent este {cifra}")



