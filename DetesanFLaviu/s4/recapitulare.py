"""
Recapitulare OOP ( Clase, obiecte, cei 4 piloni OOP)
"""

"""

- 4 piloni ai OOP-ului: mostenire, polimorfism, abstractizare, incapsulare

1. Mostenire = capacitatea unei clase de a deriva sau a mosteni din alta clasa.
- clasa de baza (clasa parinte/parent class) - clasa din care se mosteneste.
- clasa derivata (clasa copil/child class) - clasa care mosteneste/deriva din clasa parinte.

# o metoda din clasa parinte
def descrie(self):
    print("clasa parinte")
    
# clasa copil - extindem comportamentul metodei descrie din clasa parinte
def descrie(self):
    super().descrie()
    print("clasa copil")
    
2. Polimorfism = mai multe forme (permitem obiectului sa ia mai multe forme)

# functie built-in polimorfica
len("abc")
len([1, 2, 3, 4])

# functie polimorfica definita de noi
def add(x, y, z = 0):
    return x + y + z
    
add(1, 2, 3)
add(1, 2)

# clase
Class Student:
    def descrie(self):
        print("Student")
        
Class Employee:
    def descrie(self):
        print("Employee)
        
student1 = Student()
student1.descrie()

angajat1 = Angajat()
angajat1.descrie()

3. Abstractizare = ascunderea implementarii comportamentului + presupune folosirea de clase abstracte/interfete

- clasa abstracta => metode abstracte (cele decorate cu @abstractmethod) si care nu au corp/fara implemenatare
+ metode cu implementare/logica definita.
- interfata = clasa abstracta care are DOAR metode abstracte.

4. Encapsulare = facem datele si comportamentul dintr-o clasa, sa NU fie accesibile in exteriorul clasei.

-> atribute/metode PRIVATE -> care sunt prefixate cu __.

- proprietati - incapsuleaza atribute private -> @property
- getter, setter, deleter
"""

"""
1. Defineste o clasa abstracta AbstractVideo.
Aceasta va avea o metoda abstracta show_details.
De asemenea, va mai avea o metoda, play, care va afisa mesajul
'Video is playing.'
"""


from abc import ABC, abstractmethod


class AbstractVideo(ABC):

    @abstractmethod
    def show_details(self):
        pass

    def play(self):
        print("Video is playing")

"""
2. Defineste o clasa Videoclip.
Aceasta va implementa clasa abstracta AbstractVideo.
Va avea atribute in constructor: title, duration.
Va implementa metoda show_details, in care va afisa mesajul:
'<title> has a duration of <duration> minutes.'
"""

class Videoclip(AbstractVideo):

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_details(self):
        print(f'{self.title} has a duration of {self.duration} minutes.')


videoclip1 = Videoclip('title1', 10)

# accesam atributele obiectului videoclip1
print(videoclip1.title)
print(videoclip1.duration)

# accesam metodele obiectului videoclip1
videoclip1.show_details()
videoclip1.play()

"""
3. 
a. Defineste o clasa numita Movie care va mosteni clasa Videoclip.
Extinde constructorul/metoda de initializare a clasei Movie,
astfel incat sa aiba ca atribute si :
- genre (str)
- director (str) -> ATRIBUT PRIVAT!
- actors (list)

b. Extinde metoda show details, astfel incat sa se afiseze si
mesajul: 
'Is directed by {director} and the actors are {actors}.'

c. Defineste o proprietate director, cu getter, setter si deleter,
care incapsuleaza atributul privat __director.
"""

class Movie(Videoclip):

    def __init__(self, title, duration, genre, director, actors):
        super().__init__(title, duration)
        self.genre = genre
        self.__director = director
        self.actors = actors

    @property
    def director(self):
        return self.__director

    @director.getter
    def director(self):
        print("Get")
        return self.__director

    @director.setter
    def director(self, value):
        print("Set")
        self.__director = value

    @director.deleter
    def director(self):
        print("Delete")
        self.__director = None

    def show_details(self):
        super().show_details()
        print(f'Is directed by {self.__director} and the actors are {self.actors}.')

movie1 = Movie(
    title="Topgun",
    duration=120,
    genre='action',
    director='John Doe',
    actors=['actor1', 'actor2']
)

# printam toate atributele de pe movie1
print(movie1.title)
print(movie1.duration)
print(movie1.actors)
print(movie1.genre)
# print(movie1.__director) -> DA EROARE!

# printam toate proprietatile de pe movie1
print(movie1.director)

movie1.director = 'Nick'
print(movie1.director)

del movie1.director
print(movie1.director)

# accesam metodele
movie1.show_details()
movie1.play()
