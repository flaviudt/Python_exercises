import requests
# """
# HTTP. Rest APIs. Requests
#
# Folosim https://jsonplaceholder.typicode.com/guide/
# Toate requesturile se vor face prima data in Postman (pentru verificare),
# iar apoi folosind libraria requests din Python.
#
# Structura datelor este următoarea:
# - fiecare post este deținut de un user, și poate avea mai multe comments
# - fiecare album este deținut de un user, și poate avea mai multe photos
# - fiecare todo este detinut de un user.
#
# 1. Alege un user din lista de useri predefiniti.
# Pentru acesta, fa requesturile necesare pentru a afișa următoarele informații:
# -> lista de posts
# -> lista de albume
# -> lista de todos
# Pentru a menține output-ul la un nivel acceptabil, afișează la fiecare dintre aceste liste
# doar informații despre primele 3 obiecte,
# iar apoi afiseaza "+x more posts/albums/todos", unde x este numărul de obiecte rămase.
# """
# # 1.luam toate postarile pentru userul cu id 1
# response = requests.get(url="https://jsonplaceholder.typicode.com/users/1/posts")
# # print(response.status_code)
# # print(response.content)
# # print(response.text)
#
# # posts = response.json()
# # for post in posts[0:3]:
# #     print(f'Post id {post["id"]} title {post["title"]}, userId {post["userId"]}')
# # left_posts = len(posts) - 3
# # print(f'+ {left_posts} more posts')
# #
# #
# # for index, post in enumerate(posts):
# #     if index > 2:
# #         left_posts = len(posts) - 3
# #         print(f'+ {left_posts} more posts')
# #         break
# #     print(f'Post id {post["id"]} title {post["title"]}, userId {post["userId"]}')
#
# ## pentru albume
# response = requests.get(url='https://jsonplaceholder.typicode.com/users/1/albums')
# print(response.status_code)
# # print(response.content)
# # print(response.text)
#
# albums = response.json()
# for album in albums[0:3]:
#     print(f'Album id {album["id"]}, title: {album["title"]}')
# left_albums = len(albums) - 3
# print(f'+ {left_albums} more albums')
#
#
# ## pentru todos
# response = requests.get(url='https://jsonplaceholder.typicode.com/users/1/todos')
# print(response.status_code)
# # print(response.content)
# # print(response.text)
#
# todos = response.json()
# for todo in todos[0:3]:
#     print(f'Todo id {todo["id"]}, title: {todo["title"]}, status: {todo["completed"]}')
# left_todos = len(todos) - 3
# print(f'+ {left_todos} more todos')
#
# """
# 2. Alege un post, și afișează lista de comentarii.
# Alege un album, si afiseaza lista de photos.
# """
#
# response = requests.get(url='https://jsonplaceholder.typicode.com/posts/3/comments')
# print(response.status_code)
# print(response.json())
#
#
# response = requests.get(url='https://jsonplaceholder.typicode.com/albums/5/photos')
# print(response.status_code)
# print(response.json())
#
# """
# 3. Creeaza un post nou (atentie, acesta NU va fi salvat, dar putem analiza răspunsul pentru a vedea cum ar arata
# în viitor dacă ar fi fost salvat). Încearcă să-l creezi cu si fără id. Ce observi?
# """
# json_data = {
#     "userId":1,
#     "title":"title1",
#     "body":"body1"
# }
# response = requests.post(url="https://jsonplaceholder.typicode.com/posts/",json=json_data)
# print(response.status_code)
# print(response.json())
#
# """
# 4. Alege un post existent și realizează operațiunile de PUT si PATCH
# (atentie, modificările NU vor fi salvate, analizăm doar răspunsul).
# Ce observi ca este diferit între cele 2 metode?
# """
# json_data = {
#     "userId": 1,
#     "title": "Modificare PUT"
# }
# response = requests.put(url="https://jsonplaceholder.typicode.com/posts/2",json=json_data)
# print(response.status_code)
# print(response.json())
#
#
# json_data = {
#     "userId": 1,
#     "title": "Modificare PATCH"
# }
# response = requests.patch(url="https://jsonplaceholder.typicode.com/posts/2",json=json_data)
# print(response.status_code)
# print(response.json())
# """
# 5. Folosind query parameters, filtrează lista de todos pentru userul ales astfel incat
# sa afisezi doar todos care nu sunt completed.
# """
# response = requests.get(url='https://jsonplaceholder.typicode.com/users/1/todos?completed=false')
# print(response.status_code)
# # print(response.content)
# print(response.text)
#
# todos = response.json()
# for todo in todos[0:3]:
#     print(f'Todo id {todo["id"]}, title: {todo["title"]}, status: {todo["completed"]}')
# left_todos = len(todos) - 3
# print(f'+ {left_todos} more todos')


"""
6. Alege un album, și ia pozele din acesta în 2 moduri diferite (o data cu nested resource, o data folosind query params)
Verifica dacă exista vreo diferenta intre cele 2 rezultate. 
"""
response = requests.get(url='https://jsonplaceholder.typicode.com/albums/5/photos')
print(response.status_code)
print(response.json())
# print(response.text)


response = requests.get(url='https://jsonplaceholder.typicode.com/photos?albumId=5')
print(response.status_code)
print(response.json())
# print(response.text)