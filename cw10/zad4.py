#!/usr/bin/python
# coding: utf8
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import NUMERIC

Base = declarative_base()

class Book(Base):
	__tablename__ = 'books'
	id = Column(Integer, primary_key=True)
	title = Column(String(100))
	author = Column(String(100))
	isbn = Column(String(50))
	publication_date = Column(NUMERIC)

	def __str__(self):
		return "id: %d, title: %s, author: %s, isbn: %s, publication date: %d" % (self.id, self.title, self.author, self.isbn, self.publication_date)

class Reader(Base):
	__tablename__ = 'readers'
	id = Column(Integer, primary_key = True)
	name = Column(String(100))
	surname = Column(String(100))
	
	def __str__(self):
		return "id: %d, name: %s, surname: %s" % (self.id, self.name, self.surname)

class Order(Base):
	__tablename__ = 'orders'
	id = Column(Integer, primary_key=True)
	book_id = Column(Integer, ForeignKey("book.id"))
	reader_id = Column(Integer, ForeignKey("reader.id"))

	def __str__(self):
		return "id: %d, book id: %d, reader id: %d" % (self.id, self.book_id, self.reader_id)

engine = create_engine('sqlite:///library.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

def main():
	print '''1 - Wypisz wszystkich czytelnikow
2 - Wypisz wszystkie ksiazki
3- Wypisz wszystkie zamowienia'''
	choice = raw_input()
	if choice == "1":
		show_all_readers()
	elif choice == "2":
		show_all_books()
	elif choice == "3":
		show_all_orders()
	else:
		print "Wpisano nieprawidlowa wartosc. Wpisz ponownie"
		main()

def show_all_readers():
	for reader in session.query(Reader).all():
		print reader
	main()

def show_all_books():
	for book in session.query(Book).all():
		print book
	main()

def show_all_orders():
	for order in session.query(Order).all():
		print order
	main()

main()
