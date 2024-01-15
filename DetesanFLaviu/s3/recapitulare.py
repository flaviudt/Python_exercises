"""
Recapitulare partea 1 - Functii
"""

# Ce este o functie?
# -> reprezinta un bloc de cod, care nu se executa decat cand este apelat
# + putem sa folosim functionalitatea de cate ori vrem
# + putem sa apelam/invocam functia de cate ori vrem
# print("Hello")
# my_str = 'aabbacd'
# print(my_str.count('a'))

# O functie are marele avantaj ca este REUTILIZABILA.

# Un exemplu de functie
# def say_hi():
#     print("Hello")

# apelam/invocam functia
# say_hi()

# Hello, Cosmina
# Hello, Andrei

# def say_hi(name):
#     print(f"Hello, {name}")
#
# say_hi("Cosmina")
# say_hi("Andrei")

# Cati parametri poate sa aiba o functie?
# Oricati
# def describe_movie(title, director, release_date = "01.01.2023"):
#     print(f"The movie {title} directed by {director} will be available from {release_date}")
# #
# # # positional arguments
# # describe_movie("Topgun", "John Doe", "08.04.2023")
# # describe_movie("Avatar", "Nick Doe", "01.12.2022")
# #
# # # named arguments
# # describe_movie(director="John Doe", title="Topgun", release_date="08.04.2023")
# #
# # describe_movie("Topgun", "John Doe") # da eroare daca release_date nu are valoare default -> TypeError

# def multiply(*args):
#     result = 1
#     for value in args:
#         result *= value
#     return result
#
# # result = multiply(1, 2)
# # print(result)
#
# print(multiply(1, 2))
# print(multiply(1, 2, 3))
# print(multiply(4, 10, 2, 5))

# **kwargs

# def concatenate(**kwargs):
#     result = ''
#     for arg in kwargs.values():
#         result += arg
#
#     return result
#
# print(concatenate(a="Hello", b="World"))
# print(concatenate(a="Python", b="Is", c="Great"))


class Masina:

    # ATRIBUTE ale clasei
    marca = 'Dacia'

    def init(self, culoare):
        # ATRIBUTE ALE OBIECTULUI
        self.culoare = culoare

    # METODE
    def accelereaza(self):
        print("Vrum vrum")

masina1 = Masina("rosu")
masina2 = Masina("albastru")
print(masina2.culoare)

print(masina1.culoare)
print(Masina.marca)
masina1.accelereaza()

