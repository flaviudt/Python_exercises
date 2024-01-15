"""

Context Managers

Se da un fisier text hello.txt, care contine un text scurt. Deschideti fisierul si cititi continutul, folosind urmatoarele 2 metode:
try - finally
Fisierul se deschide inainte de try, folosind functia open
In interiorul try citim continutul folosind functia read
In finally se inchide fisierul
with (context manager)
Se va observa ca pentru with nu mai este nevoie sa inchidem noi manual fisierul, pentru ca context managerul face asta pentru noi.

"""
# V1
f = open('hello.txt','r')
try:
    print(f.read())

finally:
    f.close()

# V2
with open('hello.txt','r') as f:
    print(f.read())

