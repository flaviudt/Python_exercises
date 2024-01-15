"""
PARTEA 1 - STRUCTURI DE DATE

Exerciții - studiu în workshopul de weekend
"""


"""
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o.
Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.

Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări. Ambele variante își găsesc utilitatea în funcție de ce ne dorim în acel moment. 
"""

# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(note_muzicale)
# note_muzicale_inversate = note_muzicale[::-1]
# print(note_muzicale_inversate)
# note_muzicale_inversate.reverse()
# print(note_muzicale_inversate)


""""
2. De câte ori apare ‘do’?
"""
# print(note_muzicale.count('do'))

"""
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
   Găsește 2 variante să le unești într-o singură listă. 
"""

# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista3 = lista1 + lista2
# print(lista3)
# lista1.extend((lista2))
# print(lista1)
"""
4.
Sortează și afișează lista generată la exercițiul anterior.
"""
# lista3.sort()
# print(lista3)


"""
5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
Lista este goală.
Lista nu este goală.
"""
##  if lista3 ==[]
# if len(lista3) == 0 :   #lista3 ==[]
#     print('Lista este goala')
# else:
#     print('lista nu este goala')


"""
6. Folosește o funcție care să șteargă lista de la exercițiul 3.
"""

# lista3.clear()
# print(lista3)

"""
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
"""

# if len(lista3) == 0 :
#     print('Lista este goala')
# else:
#     print('lista nu este goala')

"""
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
"""

# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5 }
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())



"""
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
"""
# print('Ana a luat nota ' + str(dict1['Ana']))
# print('Gigel a luat nota ' + str(dict1['Gigel']))
# print('Dorel a luat nota ' + str(dict1['Dorel']))

## varianta  get e mai buna
# print(f"\nAna a luat nota {dict1['Ana']}")
# print(f"\nGigel a luat nota {dict1['Gigel']}")
# print(f"\nDorel a luat nota {dict1['Dorel']}")
#
# print(f"\nMaria a luat nota {dict1.get('Maria',-1)}")

"""
10. Dorel a făcut contestație și a primit 6
Modifică nota lui Dorel în 6
Printează nota după modificare
"""

# dict1['Dorel'] = 6
# print('Dorel a luat dupa contestatie nota ' + str(dict1['Dorel']))
#

"""
11. Gigel se transferă din clasă
Căuta o funcție care să îl șteargă
Vine un coleg nou. Adaugă Ionică, cu nota 9
Printează noii elevi
"""
## v1
# dict1.pop('Gigel')
# print(dict1)
# dict1['Ionica'] = 9
# print(dict1)
# ## v2
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# del dict1["Gigel"]
# print(dict1)
# dict1.update({"Ionica" : 9})
# print(dict1)


#dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# il stergem pe Gigel / stergem un element (pereche cheie-valoare) din dictionar

# varianta 1: folosind del

# del dict1["Gigel"]
# print(dict1)

# varianta 2: folosind metoda pop
# dict1.pop('Gigel')
# print(dict1)

# Actualizare dictionar

# folosind metoda update
# dict1.update({"Ionica": 9, "Maria": 10})
# print(dict1)

# folosind accesarea dupa cheie si atribuirea unei noi valori
# dict1['Ionica'] = 9
# dict1['Maria'] = 10
# print(dict1)



"""
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
Efectuează schimbarea 
Șterge jucătorul scos din listă
Adaugă jucătorul intrat
Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
Afișază ‘mai ai z schimbări’

Testează codul cu diferite valori

Google search hint
“how to check if item is în list python”
"""
#
# echipa = ['Ronaldo', 'Hagi', 'Pele', 'Maradona', 'Zidane']
# schimbari_efectuate = 0
# schimbari_max = 3
# print(echipa)
#
# # v1
# x = echipa[2]
# print(x)
# check = x in echipa
# print(check)
#
# if check == True and schimbari_efectuate < schimbari_max :
#     echipa.remove(x)    #eliminam din lista jucatorul de pe poz[2]
#     print(echipa)
#     y = echipa.append('Raul')
#     print(echipa)
#     schimbari_efectuate += 1
#     schimbari_ramase = schimbari_max - schimbari_efectuate
#     print(f'A intrat {y} , a iesit {x}, mai ai {schimbari_ramase} schimbari')
# else:
#     schimbari_ramase = schimbari_efectuate
#     print(f'Nu se poate efectua schimbarea deoarece hucatorul{x} nu e in teren')
#     print(f'Mai ai {schimbari_ramase}')
# print(check)

## v2

# check = 'Ronaldo' in echipa
# print(check)
# if check == True and schimbari_efectuate <= schimbari_max :
#     echipa.remove('Ronaldo')
#     echipa.append('Raul')
#     print('A intrat Raul , a iesit Ronaldo, mai ai 2 schimbari')
# else:
#     print('Nu se poate efectua schimbarea deoarece jucatorul Figo nu e in teren')
#     print('Mai ai trei schimbari')
# print(echipa)

## v3 -functionala -  jucatorul de la tastatura

# player_list = ['Rolando', 'Messi', 'Ibrahimovic', 'Benzema', 'Neymar']
# print(f"\nEchipa de jucători este formată din {player_list}")
# schimbari_efectuate = 2
# schimbari_max = 3
# y = str(input("Ce jucător înlocuiești: "))
# x = str(input("Ce jucător adaugi: "))
# if schimbari_efectuate < schimbari_max:
#      if y in player_list:
#         schimbari_efectuate += 1
#         player_list.remove(y)
#         player_list.append(x)
#         z = schimbari_max - schimbari_efectuate
#         print(f"\nA intrat {x}, a ieșit {y}, mai ai {z} schimbări")
#      else:
#         print(f"\nNu se poate efectua schimbarea deoarece jucătorul {y} nu e în teren")
# else:
#     print(f"\nNu mai sunt schimbări disponibile")

"""
13.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
Adaugă în zilele_sapt ‘luni’
Afișează zile_sapt
"""

# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica',}
# zile_sapt.add('luni')
# print(zile_sapt)

"""
14.Folosește un if și verifică dacă:
Weekend este un subset al zilelor din săptămânii.
Weekend nu este un subset al zilelor din săptămânii.
"""
# if weekend.issubset(zile_sapt):
#     print('Weekend este un subset al zilelor din săptămânii.')
# else:
#     print('Weekend nu este un subset al zilelor din săptămânii.')

"""
15. Afișează diferențele dintre aceste 2 seturi.
"""
# print(zile_sapt.difference(weekend))
# print(weekend.difference((zile_sapt)))
"""
16. Afișează intersecția elementelor din aceste 2 seturi.
"""
# print(zile_sapt.intersection(weekend))