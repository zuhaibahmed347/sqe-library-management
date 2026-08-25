class Book:
    def __init__(self, isbn, title, author, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.copies = copies  # BUG 2: no validation, negative allowed


class Library:
    def __init__(self):
        self.books = []
        self.members = {}

    def add_book(self, book):
        # BUG 3: no check for duplicate ISBN
        self.books.append(book)

    def search_by_title(self, title):
        # BUG 5: case-sensitive comparison
        results = [b for b in self.books if b.title == title]
        return results

    def get_most_popular_book(self, borrow_counts):
        # BUG 1: crashes if borrow_counts is empty
        return max(borrow_counts, key=borrow_counts.get)

    def calculate_fine(self, days_late):
        # BUG 4: wrong rate + no rounding, e.g. should be 0.5/day
        return days_late * 0.3333333


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
