class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages == other.pages

class Bookshelf:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def total_pages(self):
        total = 0
        for book in self.books:
            total += book.pages
        return total

    def __len__(self):
        return len(self.books)

    def __contains__(self, item):
        if isinstance(item, str):
            return any(book.title == item for book in self.books)
        return item in self.books

clean_code = Book("Clean Code", 464)
python_crash_course = Book("Python Crash Course", 544)
rak_buku = Bookshelf()

print(f"Buku: {clean_code}")
print(f"Buku: {python_crash_course}")

rak_buku.add_book(clean_code)
rak_buku.add_book(python_crash_course)

print(f"Total buku: {len(rak_buku)}")
print(f"Total halaman: {rak_buku.total_pages()}")

print(f"Apakah 'Clean Code' ada di rak? {'Clean Code' in rak_buku}")
