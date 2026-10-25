from src.library import Book, Library, rank_books_by_popularity


def make_book(title, times_borrowed):
    isbn = f"978{sum(map(ord, title)):010d}"
    book = Book(isbn, title, "Author", 1)
    book.times_borrowed = times_borrowed
    return book


def library_with(*books):
    library = Library()
    for book in books:
        library.add_book(book)
    return library


def test_rank_books_empty_catalog_returns_empty_list():
    library = Library()
    assert rank_books_by_popularity(library) == []

def test_rank_books_single_book_returns_that_book():
       library = Library()
       book = Book("9780132350884", "Clean Code", "R. Martin", 2)
       library.add_book(book)
       assert rank_books_by_popularity(library) == [book]


def test_rank_books_orders_by_borrow_count_descending():
       library = Library()
       low = Book("9780000000001", "Low", "A. Author", 1)
       high = Book("9780000000002", "High", "B. Author", 1)
       mid = Book("9780000000003", "Mid", "C. Author", 1)
       low.times_borrowed = 1
       high.times_borrowed = 9
       mid.times_borrowed = 4
       for book in (low, high, mid):
           library.add_book(book)
       assert rank_books_by_popularity(library) == [high, mid, low]

def test_rank_books_tie_broken_alphabetically_by_title():
    zebra = make_book("Zebra", 5)
    apple = make_book("Apple", 5)
    assert rank_books_by_popularity(library_with(zebra, apple)) == [apple, zebra]


def test_rank_books_tie_break_is_case_insensitive():
    lower = make_book("alpha", 5)
    upper = make_book("Beta", 5)

    assert rank_books_by_popularity(library_with(lower, upper)) == [lower, upper]
