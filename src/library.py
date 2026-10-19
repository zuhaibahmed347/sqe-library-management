class LibraryIOError(Exception):
    """Raised when the library cannot read or write its catalog file."""


class Book:
    def __init__(self, isbn, title, author, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.copies = copies  # BUG 2: no validation, negative allowed
        self.available_copies = copies


class Library:
    def __init__(self):
        self.books = []
        self.members = {}
        self.borrowed_counts = {}

    def add_book(self, book):
        if any(b.isbn == book.isbn for b in self.books):
            raise ValueError(f"Book with ISBN {book.isbn} already exists")
        self.books.append(book)

    def search_by_title(self, title):
        # BUG 5: case-sensitive comparison
        results = [b for b in self.books if b.title == title]
        return results

    def get_most_popular_book(self, borrow_counts):
        if not borrow_counts:
            return None
        return max(borrow_counts, key=borrow_counts.get)

    def calculate_fine(self, days_late):
        if days_late < 0:
            return 0.0
        return round(days_late * 0.5, 2)

    def borrow_book(self, member_id, isbn):
        current = self.borrowed_counts.get(member_id, 0)
        if current >= 5:
            raise ValueError(f"Member {member_id} has reached the 5-book borrow limit")
        self.borrowed_counts[member_id] = current + 1
        return True

    def total_available_copies(self):
        return sum(b.available_copies for b in self.books)

    def export_catalog(self, path):
        content = "\n".join(
            f"{b.isbn},{b.title},{b.author},{b.copies}" for b in self.books
        )
        try:
            with open(path, "w") as f:
                f.write(content)
        except OSError as e:
            raise LibraryIOError(f"Could not export catalog to {path}: {e}") from e


def fine_tier(days_overdue):
    if days_overdue < 0:
        raise ValueError("days_overdue cannot be negative")
    if days_overdue == 0:
        return "None"
    elif 1 <= days_overdue <= 7:
        return "Low"
    elif 8 <= days_overdue <= 14:
        return "Medium"
    elif 15 <= days_overdue <= 30:
        return "High"
    else:
        return "Severe"


def validate_isbn(isbn):
    if not isinstance(isbn, str):
        raise ValueError("ISBN must be a string")
    if len(isbn) == 0:
        raise ValueError("ISBN cannot be empty")
    if not isbn.isdigit():
        raise ValueError("ISBN must contain only digits")
    if len(isbn) != 13:
        raise ValueError("ISBN must be exactly 13 digits")
    return True


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

def rank_books_by_popularity(library):
    """Return the library's books ranked by popularity (most borrowed first)."""
    return list(library.books)