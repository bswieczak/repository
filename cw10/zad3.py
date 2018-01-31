# -*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect('library.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books
(id integer primary key autoincrement, title text not null, author text not null, isbn text not null,
publication_date integer not null)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS readers
(id integer primary key autoincrement, name text not null, surname text not null)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS readers
(id integer primary key autoincrement, name text not null, surname text not null)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS orders
(id integer primary key autoincrement, book_id integer not null, reader_id integer not null, foreign key(book_id) references books(id),
foreign key(reader_id) references readers(id))''')

cursor.execute('''INSERT INTO books (title, author, isbn, publication_date) VALUES ('Thinking in Java', 'Bruce Eckel', '3-598-21500-2' , 2006)''')
cursor.execute('''INSERT INTO books (title, author, isbn, publication_date) VALUES ('Język C++', 'Prata Stephen', '3-598-21501-0', 2012)''')
cursor.execute('''INSERT INTO books (title, author, isbn, publication_date) VALUES ('HTML i CSS', 'Duckett Jon', '3-598-21503-7' , 2014)''')
cursor.execute('''INSERT INTO books (title, author, isbn, publication_date) VALUES ('Python', 'Raschka Sebastian', '3-598-21504-5' , 2017)''')
cursor.execute('''INSERT INTO books (title, author, isbn, publication_date) VALUES ('JavaScript i jQuery', 'Duckett Jon', '3-598-21502-9' , 2015)''')

cursor.execute('''INSERT INTO readers (name, surname) VALUES ('Jan', 'Kowalski')''')
cursor.execute('''INSERT INTO readers (name, surname) VALUES ('Piotr', 'Nowal')''')
cursor.execute('''INSERT INTO readers (name, surname) VALUES ('Mariusz', 'Janowski')''')


connection.commit()

connection.close()