"""

Decorators extra

Implementati o clasa User, cu urmatoarele cerinte:
– constructorul va primi nume, email, parola, si data nasterii
– o metoda login, care va primi email si parola ca parametrii; daca acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informatiile despre user DOAR DACA acesta este logat, folosind un decorator `@require_login`
– o metoda logout, fara params, care delogheaza userul.


Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, si dupa inca o logare.

"""

logged_users = set()


def require_login(func):
    def wrapper(*args, **kwargs):
        if args[0] in logged_users:
            return func(*args, **kwargs)
        else:
            print('Please login first!')

    return wrapper


class User:

    def __init__(self, nume, email, parola, data_nasterii):
        self.nume = nume
        self.email = email
        self.parola = parola
        self.data_nasterii = data_nasterii
        self.is_logged_in = False

    def login(self, email, parola):
        if email == self.email and parola == self.parola:
            logged_users.add(self)
        else:
            print('User sau parola grestit/gresita')

    @require_login
    def get_info(self):
        msg = f'User-ul {self.nume}, cu email-ul {self.email} are data nasterii: {self.data_nasterii}'
        return msg

    def logout(self):
        logged_users.remove(self)


user1 = User('Ana', 'ana@gmail.com', 'qwert123', '13.01.1999')
print(user1.get_info())
user1.login('ana@gmail.com', 'qwert123')
print(user1.get_info())
print('========')
user1.logout()
print(user1.get_info())
user1.login('ana@gmail.com', 'qwert123')
print(user1.get_info())