import sys, json

class Book:
    title = None
    ISBN = None
    author = None

    def __init__(self, title, ISBN, author):
        self.author = author
        self.title = title
        self.ISBN = ISBN

class Library:

    list = []

    def add(self, book):
        self.list.append({
            'title': book.title,
            'ISBN': book.ISBN,
            'author': book.author
        })

    def delete(self, title):
        for row in list:
            if(row[title] is title):
                self.list.remove(row)

    def save(self, path):
        with open(path,'w') as writer:
            for i in self.list:
                writer.write(json.dumps(i)+"\n")

    def load(self, path):
        with open(path, 'r')as reader:
            for i in reader.readlines():
                i = i.strip()
                self.list.append(json.loads(i))

library = Library()
library.add(Book('Ania z Lublina', 'ISBN-12313123', 'jan kowalski'))
library.add(Book('Romek z Lublina', 'ISBN-12332113123', 'Ania kowalski'))

library.save(sys.argv[1])
print(library.list)