from book import Book

class Library():
    def __init__(self):
        self.collection = dict()
        self.active_book = None
        self.id_counter = 0

    def add_to_collection(self, title, content):
        new_book = Book(self.id_counter, title, content)
        self.collection[new_book.id] = new_book
        self.id_counter += 1
