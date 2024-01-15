"""
Folosim Simple Books API, descris aici : https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md

Toata rezolvarea se va face într-o clasa numita Books API Client.
Pentru testare se va crea un obiect din aceasta clasa și se vor apela metodele implementate.

1. Folosind endpoint-ul de authentication, genereaza un access token
(fa asta in constructor, client name si email ar trebui sa fie atribute).

2. Adaugă o metoda prin care poți vedea toate comenzile.
adaugam headers dupa url , pentru auth

3. Adaugă o metoda prin care poți vedea toate cărțile.

4. Adaugă o metoda prin care poți posta o comanda.

5. Adaugă o metoda prin care poți șterge o comanda.

"""
import requests


class BooksAPIClient:

    def __init__(self, client_name, email):
        self.client_name = client_name
        self.email = email
        self.token = self._generate_token()

    def _generate_token(self):
        json_data = {
            "clientName": self.client_name,
            "clientEmail": self.email
        }
        response = requests.post(url="https://simple-books-api.glitch.me/api-clients", json=json_data)
        return response.json()['accessToken']

    def get_all_orders(self):
        header = {
            'Authorization': self.token
        }
        response = requests.get(url="https://simple-books-api.glitch.me/orders", headers=header)
        # print(response.headers)
        return response.json()

    def get_all_books(self):
        response = requests.get(url="https://simple-books-api.glitch.me/books")
        return response.json()

    def create_order(self):
        json_data = {
            "bookId": 1,
            "customerName": self.client_name
        }
        headers = {
            'Authorization': self.token
        }
        response = requests.post(url="https://simple-books-api.glitch.me/orders", json=json_data, headers=headers)
        print(response.status_code)
        self.order_id = response.json()['orderId']
        print(response.json())
        return response.json()['orderId']

    def get_book_by_id(self, book_id):
        response = requests.get(url=f"https://simple-books-api.glitch.me/books/{book_id}")
        return response.json()

    def delete_order(self):
        headers = {
            'Authorization': self.token
        }

        response = requests.delete(url=f"https://simple-books-api.glitch.me/orders/{self.order_id}",
                                   headers=headers)
        print(response.status_code)
        return True


obj1 = BooksAPIClient('Flaviu986756435554455595665685557', 'flaviu9583555555454955556768666567@email.com')
print(obj1.token)
print(obj1.get_all_orders())

print(obj1.get_all_books())
print(obj1.create_order())
print(obj1.get_all_orders())
print(obj1.get_book_by_id(2))
print(obj1.delete_order())
