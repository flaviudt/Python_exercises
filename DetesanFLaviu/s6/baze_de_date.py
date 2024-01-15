"""

1. Write a SQL statement to create a table called continents, with the following columns:
continent_id
continent_name
continent_code – 2 letters code, use this link: https://datahub.io/core/continent-codes
"""

import sqlite3

connection = sqlite3.connect("geography.db")
cursor = connection.cursor()
# cursor.execute(
#     """
#     CREATE TABLE Continents (
#     continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     continent_name TEXT NOT NULL,
#     continent_code CHAR(2) NOT NULL
#     );
#     """
# )


"""
2. Using the link above, write all SQL statements needed to add all the seven continents (INSERT).
"""
# continents_list =[
#     ('Asia','AS'),
#     ('Africa','AF'),
#     ('North America','NA'),
#     ('South America','SA'),
#     ('Oceania','OC'),
#     ('Europa','EU'),
#     ('Antartica','AN')
# ]
# sql_query= 'INSERT INTO Continents ( continent_name, continent_code) VALUES (? , ?) '
#
# cursor.executemany(sql_query,continents_list)
# connection.commit()
#

"""
3. Write a SQL statement to create a table called countries, with the following columns:
country_code – 2 letters code (e.g. RO, US, IT, etc)
country_name
continent_id – foreign key
population – number
"""
#import sqlite3
# cursor.execute(
#     """
#     CREATE TABLE Countries (
#     country_code CHAR(2) PRIMARY KEY,
#     country_name TEXT NOT NULL,
#     continent_id INTEGER NOT NULL,
#     population INTEGER,
#     FOREIGN KEY (continent_id) REFERENCES Continents (continent_id)
#     );
#     """
# )
# connection.commit()
"""
4. Write a few SQL statements to add some countries. Here is a list of countries with their codes.
Feel free to invent or approximate their populations,
 and use your geography knowledge for their continent.
Add at least 10 countries, as diverse as possible (INSERT). Examples:
– Romania, EU, 19mil
– USA, NA, 330mil
– France, EU, 70mil
– Hungary, EU,  9mil
– Canada, NA, 40mil
– China, AS, 1450mil
– Belgium, EU, 12mil
–  Egypt, AF, 110mil
– Australia, OC, 25mil
"""

# sql_query = "INSERT INTO Countries (country_code, country_name, continent_id, population) VALUES ('RO', 'Romania', 6, 19000000)"
# cursor.execute(sql_query)
# sql_query = "INSERT INTO Countries (country_code, country_name, continent_id, population) VALUES ('US', 'USA', 3, 33000000)"
# cursor.execute(sql_query)
# sql_query = "INSERT INTO Countries (country_code, country_name, continent_id, population) VALUES ('FR', 'Franta', 6, 70000000)"
# cursor.execute(sql_query)
# sql_query = "INSERT INTO Countries (country_code, country_name, continent_id, population) VALUES ('HU', 'Hungary', 6, 9000000)"
# cursor.execute(sql_query)
# sql_query = "INSERT INTO Countries (country_code, country_name, continent_id, population) VALUES ('CA', 'Canada',3, 40000000)"
# cursor.execute(sql_query)
# sql_query = "INSERT INTO Countries (country_code, country_name, continent_id, population) VALUES ('CN', 'China',1, 1450000000)"
# cursor.execute(sql_query)
# sql_query = "INSERT INTO Countries (country_code, country_name, continent_id, population) VALUES ('BE', 'Belgium',6, 12000000)"
# cursor.execute(sql_query)
# sql_query = "INSERT INTO Countries (country_code, country_name, continent_id, population) VALUES ('EG', 'Egypt',2, 110000000)"
# cursor.execute(sql_query)
# sql_query = "INSERT INTO Countries (country_code, country_name, continent_id, population) VALUES ('BR', 'Brazil',4, 370000000)"
# cursor.execute(sql_query)
# sql_query = "INSERT INTO Countries (country_code, country_name, continent_id, population) VALUES ('AU', 'Australia',5, 25000000)"
# cursor.execute(sql_query)
#
#
# connection.commit()
"""
5. Write a SQL statement to select all countries, ordered by name. Write another statement to count them all.
"""

cursor.execute("SELECT * FROM Countries ORDER BY country_name ")
sql_query = cursor.fetchall()
for i in sql_query:
    print(i)

cursor.execute("SELECT COUNT(*) FROM countries;")
print(f'Nr de tari: {cursor.fetchall()}')


"""
6. Write a SQL statement to select only countries with a population greater than 20 millions.
"""
print('-'*30)
cursor.execute("SELECT country_name,population FROM Countries WHERE population > 20000000 ")
sql_query = cursor.fetchall()
for i in sql_query:
    print(i)

"""
7. Write a SQL statement to select only countries that start with a certain letter (choose one that exists for you, e.g. C in the example above).
"""
print('-'*30)
cursor.execute("SELECT * FROM Countries WHERE country_name LIKE 'B%'")
sql_query = cursor.fetchall()
for i in sql_query:
    print(i)

"""
8. Write a SQL statement that groups all countries by continents, and counts them.
"""

print('-'*30)
cursor.execute("""
SELECT continents.continent_name, COUNT(countries.country_name) 
FROM countries 
INNER JOIN continents ON countries.continent_id = continents.continent_id 
GROUP BY continents.continent_name;
""")
sql_query = cursor.fetchall()
for i in sql_query:
    print(i)

"""
9. Write a SQL statement that groups all countries by continent, and computes the total population per continent (SUM).
"""

print('-'*30)
cursor.execute("""
SELECT Continents.continent_id,Continents.continent_name, SUM(Countries.population) 
FROM Countries 
INNER JOIN Continents ON Countries.continent_id = Continents.continent_id 
GROUP BY Continents.continent_id;
""")
sql_query = cursor.fetchall()
for i in sql_query:
    print(i)


# This statement uses an INNER JOIN to combine the "countries" and "continents" tables
# based on the "continent_id" column, and then groups the resulting rows by continent name
# using the GROUP BY clause. The SUM function is used to compute the total population of each
# group. This will return a result set that shows the continent name and the total population
# of each continent.

"""
10.Extra exercises can be found online:
W3Schools: https://www.w3schools.com/mysql/exercise.asp?filename=exercise_select1
OneCompiler: https://onecompiler.com/mysql

"""