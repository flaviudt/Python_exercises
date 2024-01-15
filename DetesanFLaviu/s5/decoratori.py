"""

DECORATORS

Implementati urmatorii decoratori:
timeit – decorator care masoara timpul de executie al unei functii
logger – decorator care printeaza argumentele de intrare, si rezultatul unei functii
"""


# def salut(func):
#     def wrapper(*args,**kwargs):
#         print('Sallut')
#         return func(*args,**kwargs)
#
#     return wrapper
#
#
# @salut
# def describe_vremea(grade):
#     return(f'Vremea e frumoasa afara.Grade {grade}')
#
# @salut
# def descrie_stare_spirit():
#     return('Visatoare')
#
#
# print(describe_vremea(23))
# print(descrie_stare_spirit())

# decorator care afiseaza salut inainte de functia pe care o descrie

## Decorator timeit
# import time
# def timeit(func):
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         end_time = time.time()
#         elapsed_time = end_time - start_time
#         print(f' Elapsed time: {elapsed_time} ')
#         return res
#     return wrapper
#
# @timeit
# def describe_vremea(grade):
#     time.sleep(5)
#     return(f'Vremea e frumoasa afara.Grade {grade}')
#
#
# @timeit
# def descrie_stare_spirit():
#     time.sleep(3)
#     return('Visatoare')
#
#
# print(describe_vremea(23))
# print(descrie_stare_spirit())

### Decorator logger
def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Date intrate *args : {args}')
        print(f'Date de intrate **kwargs: {kwargs}')
        res = func(*args, **kwargs)
        print(f'date de iesire: {res}')
        return res

    return wrapper


# @logger
# def describe_vremea(grade):
#
#     return(f'Vremea e frumoasa afara.Grade {grade}')
#
# @logger
# def descrie_stare_spirit():
#     return ('Visatoare')
#
#
# @logger
# def hello(msg):
#     print(f'hello {msg}')

#
# print(describe_vremea(23))
# print(descrie_stare_spirit())

# hello(msg = 'hello')


@logger
def suma1(a, b):
    return a + b


@logger
def suma2(a, b, c):
    return a + b + c


suma1(a=5, b=10)
print("===========")
suma1(1, 2)
print("===========")

suma2(1, 2, c=4)
print("===========")
suma2(1, 2, 3)
print("===========")
