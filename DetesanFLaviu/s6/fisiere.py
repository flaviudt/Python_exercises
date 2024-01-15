"""

Pachete python. Interacțiune cu fișiere.

1. Create a text file called “hello.txt” and add the following text inside of it:
Python
Java
Javascript
C/C++/C#
PHP
Node.js

Write a short program to read and display the text file
"""
# ## V1
# f = open('hello.txt', 'r')
# text_fisier = f.read()
# f.close()
# print(text_fisier)
#
# ## V2 - context manager
# with open('hello.txt', 'r') as f:
#     text = f.read()
#     print(text)

"""
2. Write a short program to append the following lines to “hello.txt” (you will use a list of strings and a for-loop):
Go
Kotlin
Swift

Display the new contents of the file.
"""
# lst = ['Go', 'Kotlin', 'Swift']
# with open('hello.txt', 'a') as f:
#     for elem in lst:
#         text = f.write('\n' + elem)
#
# with open('hello.txt', 'r') as f:
#     text = f.read()
#     print(text)

"""
3. Write a short program that reads the “hello.txt” file and displays every other line (only odd lines).
"""
# ## V1
# with open('hello.txt', 'r') as f:
#     lines = f.readlines()
#     print(lines[::2])
#
# ## V2
# with open("hello.txt", "r") as f:
#     lines = f.readlines()
#     # for l in range(0, len(lines)):
#     #     if l % 2 == 0:
#     #         print(lines[l])
#
#     for n in range(0, len(lines), 2):
#         print(lines[n])


"""
4. Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`. 
Each file will contain the sentences below:

My name is letter X.
I am the 24th letter of the alphabet.

Make sure you use the correct ending for the letter’s number (e.g. 1st, 2nd, 3rd, etc.)
"""


## v1
# alfabet_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# for index,element in enumerate(alfabet_letters):
#     with open(f'{element}.txt','w') as f:
#         f.write(f'My name is letter {element}'+ '\n')
#         t = ''
#         if index == 0:
#             t = 'st'
#         elif index == 1:
#             t = 'nd'
#         elif index == 2:
#             t = 'rd'
#         else:
#             t = 'th'
#         f.write(f'I am the {index+1}{t} letter of the alphabet')


# ## V2
# import string
#
# # loop through all the uppercase letters in the alphabet
# for letter in string.ascii_uppercase:
#     # get the index of the letter in the alphabet (0-25)
#     index = ord(letter) - ord('A')
#     # A -> ord(A) = 65
#     # B -> ord(B) = 66
#     # calculate the ordinal number of the letter
#     if index == 0:
#         ordinal = '1st'
#     elif index == 1:
#         ordinal = '2nd'
#     elif index == 2:
#         ordinal = '3rd'
#     else:
#         ordinal = f"{index+1}th"
#     # create the file name and open the file
#     file_name = f"{letter}.txt"
#     with open(file_name, 'w') as file:
#         # write the sentences to the file
#         file.write(f"My name is letter {letter}.\n")
#         file.write(f"I am the {ordinal} letter of the alphabet.\n")

"""
5. Create a csv file called “students.csv” and add the following text inside of it:
id,fname,lname,age,grade
1,Maria,Popescu,31,7.5
2,Andrei,Ionescu,26,8.0
3,Adriana,Marinescu,21,7.5
4,Matei,Gheorghescu,42,8.5
5,Eusebiu,Pop,33,9.5
6,Ioana,Popa,29,9.0

Read the file using Python’s `csv` standard library, and display it 
in the terminal as a table, using the options for string formatting from Python:


id	fname		lname		age	grade
---------------------------------------------------
1	Maria		Popescu		31	7.5
2	Andrei		Ionescu		26	8.0
3	Adriana		Marinescu	21	7.5
4	Matei		Gheorghescu	42	8.5
5	Eusebiu		Pop			33	9.5
6	Ioana		Popa		29	9.0
"""

# import csv
# with open('students.csv','w',newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['id','fname','lname','age','grade'])
#     writer.writerow(['1', 'Maria', 'Popescu', '31', '7.5'])
#     writer.writerow(['2', 'Andrei', 'Ionescu', '26', '8.0'])
#     writer.writerow(['3', 'Adriana', 'Marinescu', '21', '7.5'])
#     writer.writerow(['4', 'Matei', 'Gheorghescu', '42', '8.5'])
#     writer.writerow(['5', 'Eusebiu', 'Pop', '33', '9.5'])
#     writer.writerow(['6', 'Ioana', 'Popa', '29', '9.0'])
#
# with open('students.csv', 'r') as csv_file:
#     reader = csv.reader(csv_file)
#     header = next(reader)
#     print(f'{header[0]:3} {header[1]:10} {header[2]:12} {header[3]:4} {header[4]:4}')
#     print('-'*50)
#     for row in reader:
#         print(f'{row[0]:3} {row[1]:10} {row[2]:12} {row[3]:4} {row[4]:4}')


"""
6. Read again the information from the csv file above, store it all in a list of data, and then write a new file,
called “students.json”, which will contain a valid JSON object. 

Use the following format for each student (and use Python’s standard JSON module):
[
    {
        "id": 1,
        "fname": "Maria",
        "lname": "Popescu",
        "age": 31,
        "grade": 7.5
    },
    ...
]
"""
import json,csv
list_rows = []
with open('students.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        list_rows.append(row)
    print(list_rows)

with open('students.json', 'w') as json_file:
    json.dump(list_rows,json_file,indent=2)








"""
7.
Create a new PyCharm project. Make sure it has a virtualenv. Install all the following packages from PYPI:
behave
behave-html-formatter
requests
selenium
webdriver-manager
Use pip to create a `requirements.txt` file. Send your project to a colleague and ask them to install all dependencies using pip.
"""
