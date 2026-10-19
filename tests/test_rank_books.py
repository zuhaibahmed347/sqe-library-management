from src.library import Book, Library, rank_books_by_popularity

def test_rank_books_empty_catalog_returns_empty_list():
    library = Library()
    assert rank_books_by_popularity(library) == []

   def test_rank_books_single_book_returns_that_book():
       library = Library()
       book = Book("9780132350884", "Clean Code", "R. Martin", 2)
       library.add_book(book)
       assert rank_books_by_popularity(library) == [book]
