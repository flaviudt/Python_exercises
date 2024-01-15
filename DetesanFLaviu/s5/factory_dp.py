"""
FACTORY PATTERN

Acest pattern ne permite sa cream un obiect dintr-o clasa folosind o alta clasa (fabrica).
Fabrica are posibilitatea de a crea obiecte din mai multe clase
(de obicei aceste clase sunt siblings, adica mostenesc de la acelasi parinte).

Vom implementa urmatorele clase:
English/French/Spanish Translator – clase care stiu sa traduca cuvinte din romana in limba specificata.
translations va fi un dictionar cu acele cuvinte, exemplu `{ “masina”: “car” }` – se poate hardcoda in clasa
localize va fi o metoda care pentru un parametru de intrare,
ne va da traducerea lui in acea limba (exemplu `input(“masina”)` returneaza “car”)

TranslatorFactory – clasa care are o singura metoda (preferabil statica sau de clasa) numita get_translator(language)
 – in functie de parametrul language, returneaza un translator object.

english_trans = TranslatorFactory.get_translator('en')
spanish_trans = TranslatorFactory.get_translator('es')

print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In spaniola zicem {spanish_trans.localize("masina")}')

"""

### VARIANTA 1

# class BaseTranslator:
#     def __init__(self, translations):
#         self.translations = translations
#
#     def localize(self, word):
#         return self.translations.get(word, "Translation not available")
#
#
# class EnglishTranslator(BaseTranslator):
#
#     def __init__(self):
#         super().__init__({
#             "masina": "car",
#             "casa": "house",
#             "femeie": "woman",
#             "limba": "language",
#             "buna dimineata": "good morning",
#             "pa": "bye",
#             "munca": "work",
#             "comunicare": "communication"
#         })
#
#
# class FrenchTranslator(BaseTranslator):
#
#     def __init__(self):
#         super().__init__({
#             "masina": "voiture",
#             "casa": "maison",
#             "femeie": "femme",
#             "limba": "language",
#             "buna dimineata": "bonjour",
#             "pa": "au revoir",
#             "munca": "travail",
#             "comunicare": "communication"
#         })
#
#
# class SpanishTranslator(BaseTranslator):
#
#     def __init__(self):
#         super().__init__({
#             "masina": "coche",
#             "casa": "casa",
#             "femeie": "mujer",
#             "limba": "idioma",
#             "buna dimineata": "buen día",
#             "pa": "adiós",
#             "munca": "obra",
#             "comunicare": "comunicación"
#         })
#
#
# class TranslatorFactory:
#     @classmethod
#     def get_translator(cls, language):
#         if language == 'en':
#             return EnglishTranslator()
#         elif language == 'fr':
#             return FrenchTranslator()
#         elif language == 'es':
#             return SpanishTranslator()
#         else:
#             raise ValueError("Invalid language code")
#
#
# english_trans = TranslatorFactory.get_translator('en')
# spanish_trans = TranslatorFactory.get_translator('es')
#
# print(f'In engleza zicem {english_trans.localize("masina")}')
# print(f'In spaniola zicem {spanish_trans.localize("munca")}')

### VARIANTA 2

# from abc import ABC, abstractmethod
#
#
# class TranslatorInterface(ABC):
#
#     @abstractmethod
#     def localize(self, word):
#         pass
#
#
# class EnglishTranslator(TranslatorInterface):
#     translations = {'masina': 'car', 'casa': 'house'}
#
#     def localize(self, word):
#         return self.translations.get(word, word)
#
#
# class FrenchTranslator(TranslatorInterface):
#     translations = {'masina': 'voiture', 'casa': 'maison'}
#
#     def localize(self, word):
#         return self.translations.get(word, word)
#
#
# class SpanishTranslator(TranslatorInterface):
#     translations = {'masina': 'coche', 'casa': 'casa'}
#
#     def localize(self, word):
#         return self.translations.get(word, word)
#
#
# class TranslatorFactory:
#     translators = {
#         'en': EnglishTranslator,
#         'es': SpanishTranslator,
#         'fr': FrenchTranslator
#     }
#
#     @classmethod
#     def get_translator(cls, lang_abbreviation):
#         if lang_abbreviation in cls.translators:
#             return cls.translators[lang_abbreviation]()
#         raise KeyError(f'Translator not found for language {lang_abbreviation}')
#
#
# english_trans = TranslatorFactory.get_translator('en')
# spanish_trans = TranslatorFactory.get_translator('es')
# french_trans = TranslatorFactory.get_translator('fr')
#
# print(f'In engleza zicem {english_trans.localize("masina")}')
# print(f'In spaniola zicem {spanish_trans.localize("masina")}')
# print(f'In franceza zicem {french_trans.localize("masina")}')
#


# class Person:
#
#     def init(self, age):
#         self.age = age
#
#     def print_details(self):
#         print(self.age)
#         print("O persoana in general locuieste pe Pamanant.")
#
# pers1 = Person(25)
# pers1.print_details()



# class Person:
#
#     atribut_a = 'a'
#
#     @classmethod
#     def print_details(cls):
#         print(cls.atribut_a)
#         print("O persoana in general locuieste pe Pamanant.")
#
# Person.print_details()
#
# class Person:
#
#     atribut_a = 'a'
#
#     @staticmethod
#     def print_details():
#         print("O persoana in general locuieste pe Pamanant.")
#
# Person.print_details()
