class BookNotFoundError(Exception):
    pass


class BookAlreadyBorrowedError(Exception):
    pass


class BookNotBorrowedError(Exception):
    pass


class Book:
    def __init__(self, title, author, isbn, is_borrowed=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed

    def __str__(self):
        return f"{self.title} - {self.author} ({self.isbn})"

    def __eq__(self, value):
        if not isinstance(value, Book):
            return NotImplemented
        return self.isbn == value.isbn


class Member:
    def __init__(self, name, borrowed_books=None):
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    @property
    def total_books(self):
        return len(self.borrowed_books)

    def __str__(self):
        return f"Member: {self.name} (borrowed: {self.total_books} book(s))"


class Library:
    def __init__(self):
        self.library = []

    def add_book(self, value):
        if not isinstance(value, Book):
            return NotImplemented
        self.library.append({
            "title": value.title,
            "author": value.author,
            "isbn": value.isbn,
            "is_borrowed": value.is_borrowed
        })
        print(f"Book added: {value.title} - {value.author} ({value.isbn})")

    def find_book(self, isbn_target):
        if not self.library:
            print("There are no books in the library!")
            return
        for item in self.library:
            if item["isbn"] == isbn_target:
                if not item["is_borrowed"]:
                    print(f"Searching for book {isbn_target}: {item['title']} - {item['author']} ({isbn_target})")
                    return item
                else:
                    raise BookAlreadyBorrowedError(
                        f"Searching for book {isbn_target}: The book is currently borrowed!"
                    )
        raise BookNotFoundError(f"Searching for book {isbn_target}: Book not found!")

    def borrow_book(self, member, isbn_target):
        if not self.library:
            print("There are no books in the library!")
            return
        if not isinstance(member, Member):
            print("You are not allowed to borrow books! Please join as a member.")
            return

        for item in self.library:
            if item["isbn"] == isbn_target:
                if not item["is_borrowed"]:
                    if member.total_books < 4:
                        print(f"Book {item['title']} - {item['author']} ({isbn_target}) is available to borrow!")
                        print("Please return it on time!")
                        item["is_borrowed"] = True
                        member.borrowed_books.append(item)
                        return
                    else:
                        print("You have borrowed more than 3 books! Return a book first!")
                        return
                else:
                    raise BookAlreadyBorrowedError(
                        f"Searching for book {isbn_target}: The book is currently borrowed!"
                    )
        raise BookNotFoundError(f"Searching for book {isbn_target}: Book not found!")

    def return_book(self, member, isbn_target):
        if not self.library:
            print("There are no books in the library!")
            return
        if not isinstance(member, Member):
            print("Thanks for returning the books, but you are not allowed to borrow books anymore!")
            return

        for item in self.library:
            if item["isbn"] == isbn_target:
                if item["is_borrowed"]:
                    found_in_member = False
                    for collection in member.borrowed_books:
                        if collection["isbn"] == isbn_target:
                            found_in_member = True
                            break

                    if found_in_member:
                        print(f"Book {item['title']} - {item['author']} ({isbn_target}) returned!")
                        print("Thank you for returning the book on time!")
                        member.borrowed_books = [
                            b for b in member.borrowed_books if b["isbn"] != isbn_target
                        ]
                        item["is_borrowed"] = False
                        return
                    else:
                        print("ISBN not found in your borrowed collection!")
                        return
                else:
                    raise BookNotBorrowedError(
                        f"Searching for book {isbn_target}: The book is not currently borrowed!"
                    )
        raise BookNotFoundError(f"Searching for book {isbn_target}: Book not found!")

    def list_available(self):
        if not self.library:
            print("There are no books in the library!")
            return
        print("\n=== LIBRARY BOOK LIST ===")
        for index, item in enumerate(self.library, start=1):
            status = "Borrowed" if item["is_borrowed"] else "Available"
            print(f"{index}. {item['title']} - {item['author']} (ISBN: {item['isbn']}) [{status}]")
        print()

    def __len__(self):
        return len(self.library)

    def __contains__(self, isbn_target):
        if isinstance(isbn_target, (str, int)):
            return any(book['isbn'] == isbn_target for book in self.library)
        return False

    def __iter__(self):
        return iter(self.library)


# =========================================================
# --- Test Script: demonstrating ALL features ---
# =========================================================
def print_section(title):
    print("\n" + "=" * 55)
    print(f"  {title}")
    print("=" * 55)


# ---------- 1. Empty library behavior ----------
print_section("1. Empty Library")
empty_lib = Library()
empty_lib.list_available()
empty_lib.find_book(9999)          # BookNotFoundError is NOT raised -> just "no books"
empty_lib.borrow_book(Member("X"), 9999)
print(f"Length of empty library: {len(empty_lib)}")


# ---------- 2. Setup library & members ----------
print_section("2. Setup Library")
lib = Library()
member1 = Member("Budi")
member2 = Member("Sari")
print(member1)
print(member2)

book1 = Book("The Chicken", "Kay", 1666, False)
book2 = Book("Python 101", "Guido", 2001, False)
book3 = Book("Clean Code", "Robert", 2008, False)

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.list_available()


# ---------- 3. __len__ and __contains__ ----------
print_section("3. __len__ and __contains__")
print(f"Total books in library: {len(lib)}")
print(f"Is ISBN 1666 in library? {1666 in lib}")
print(f"Is ISBN 9999 in library? {9999 in lib}")


# ---------- 4. __iter__ ----------
print_section("4. Iterating with __iter__")
for b in lib:
    print(f"  -> {b['title']} by {b['author']} (ISBN: {b['isbn']})")


# ---------- 5. Book.__str__ and Book.__eq__ ----------
print_section("5. Book __str__ and __eq__")
print(book1)
print(f"book1 == Book('The Chicken', 'Kay', 1666): {book1 == Book('The Chicken', 'Kay', 1666)}")
print(f"book1 == book2: {book1 == book2}")
print(f"book1 == 'not a book': {book1 == 'not a book'}")


# ---------- 6. find_book (success) ----------
print_section("6. find_book (success)")
lib.find_book(2001)


# ---------- 7. borrow_book (success) ----------
print_section("7. borrow_book (success)")
lib.borrow_book(member1, 1666)
lib.borrow_book(member1, 2001)
lib.list_available()
print(f"{member1.name}'s total books: {member1.total_books}")


# ---------- 8. find_book on borrowed book -> error ----------
print_section("8. find_book on borrowed book (BookAlreadyBorrowedError)")
try:
    lib.find_book(1666)
except BookAlreadyBorrowedError as e:
    print(f"Caught: {e}")


# ---------- 9. borrow_book already borrowed -> error ----------
print_section("9. borrow already borrowed book (BookAlreadyBorrowedError)")
try:
    lib.borrow_book(member2, 1666)
except BookAlreadyBorrowedError as e:
    print(f"Caught: {e}")


# ---------- 10. borrow_book not found -> error ----------
print_section("10. borrow book not in library (BookNotFoundError)")
try:
    lib.borrow_book(member1, 9999)
except BookNotFoundError as e:
    print(f"Caught: {e}")


# ---------- 11. borrow limit (>3 books) ----------
print_section("11. Borrow limit check")
# member1 already has 2, add more to hit the limit
lib.add_book(Book("Book D", "Author D", 3001, False))
lib.add_book(Book("Book E", "Author E", 3002, False))
lib.borrow_book(member1, 2008)   # 3rd
lib.borrow_book(member1, 3001)   # 4th
lib.borrow_book(member1, 3002)   # should be rejected
print(f"{member1.name}'s total books: {member1.total_books}")


# ---------- 12. Non-member tries to borrow ----------
print_section("12. Non-member attempts to borrow")
lib.borrow_book("random person", 3002)


# ---------- 13. return_book (success) ----------
print_section("13. return_book (success)")
lib.return_book(member1, 1666)
lib.list_available()
print(f"{member1.name}'s total books: {member1.total_books}")


# ---------- 14. return_book not borrowed -> error ----------
print_section("14. return book that is not borrowed (BookNotBorrowedError)")
try:
    lib.return_book(member1, 1666)
except BookNotBorrowedError as e:
    print(f"Caught: {e}")


# ---------- 15. return_book wrong member ----------
print_section("15. return book not in member's collection")
# member2 borrowed nothing, but let's make sure book 2001 is borrowed by member1
print(f"member2.borrowed_books = {member2.borrowed_books}")
lib.return_book(member2, 2001)   # "ISBN not found in your borrowed collection!"


# ---------- 16. Non-member tries to return ----------
print_section("16. Non-member attempts to return")
lib.return_book("random person", 2001)


# ---------- 17. return_book not found in library ----------
print_section("17. return book not in library (BookNotFoundError)")
try:
    lib.return_book(member1, 9999)
except BookNotFoundError as e:
    print(f"Caught: {e}")


# ---------- 18. Final state ----------
print_section("18. Final Library State")
lib.list_available()
print(f"Total books in library: {len(lib)}")