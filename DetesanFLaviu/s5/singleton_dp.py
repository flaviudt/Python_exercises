"""
DESIGN PATTERNS
"""

"""
1. Singleton

Se da urmatoarea clasa:


class PresedinteRomania:

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

In momentul de fata, daca incercam sa cream mai multe obiecte din clasa aceasta, vom putea:

a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')

Scopul acestui exercitiu este sa modificam clasa de mai sus folosind DP Singleton pentru a obtine mereu acelasi obiect:
Vom folosi functia `__new__` (adevaratul constructor din Python)
Vom tine singurul obiect pe clasa (cls), si il vom crea doar la prima apelare a lui __new__
La orice alta apelare, vom returna obiectul deja existent
"""


class PresedinteRomania(object):
    __instance = None

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance


a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')
