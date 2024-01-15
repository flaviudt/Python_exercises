"""

Generators

Implementati un generator pentru loteria 6/49 si noroc:
Primele 6 apelari catre generator vor da cate un numar intre 1 si 49 (inclusiv
Ultima apelare va da un singur numar de “noroc” format din 7 cifre

"""
## V1
import random


# def loto_gen():
#     for i in range(1, 7):
#         yield random.randint(1, 49)
#         random.sample()
#     yield random.randint(1_000_000, 9_999_999)


## V2
def loto_gen():
    my_list =random.sample(range(1,50),6)
    for nr in my_list:
        yield nr
    yield random.randint(1_000_000, 9_999_999)


for val in loto_gen():
    print(val)

import random


## V3
def generator_loto():
    numere_generate = []
    for i in range(6):
        numar = random.randint(1, 49)
        while numar in numere_generate:
            numar = random.randint(1, 49)
        numere_generate.append(numar)
        yield numar
    yield random.randint(1_000_000, 9_999_999)


print(generator_loto())
for numar in generator_loto():
    print(numar)