# Requirements Traceability Matrix (RTM) — LibraryHub

| Requirement ID | Requirement Description | Linked Test Case(s) | Status |
|-----------------|--------------------------|----------------------|--------|
| REQ-1 | System shall reject a book whose ISBN already exists | TC-001, TC-002, TC-003 | Covered |
| REQ-2 | System shall reject a book with negative/zero copy count | TC-013 | Covered (gap closed) |
| REQ-3 | System shall allow case-insensitive title search | TC-014 | Covered (gap closed) |
| REQ-4 | System shall calculate late fine at $0.50/day, rounded to 2 decimals | TC-010, TC-011, TC-012 | Covered |
| REQ-5 | System shall return None for most-popular-book lookup with no borrow history | TC-015 | Covered (gap closed) |
| REQ-6 | System shall allow borrowing only if copies are available | TC-004, TC-005 | Covered |
| REQ-7 | System shall allow return only if member has that book on loan | TC-006, TC-007 | Covered |
| REQ-8 | System shall enforce max borrow limit per member | TC-008, TC-009 | Covered |

## Gap Analysis

Initial review found **3 requirements with zero linked test cases**:
REQ-2, REQ-3, and REQ-5 — these were defined in the pre-lab setup but
accidentally omitted from the original 12 test cases in Task 2. Three
new test cases were added to close these gaps:

| ID | Title | Requirement | Preconditions | Steps | Expected | Priority | Type |
|----|-------|-------------|----------------|-------|----------|----------|------|
| TC-013 | Reject negative copies on add_book | REQ-2 | Library is empty | 1. `lib.add_book(Book("111", "Test", "X", -5))` | `ValueError` is raised; book is not added | Medium | Negative / Functional |
| TC-014 | Case-insensitive title search | REQ-3 | Catalog contains "Clean Code" | 1. `lib.search_by_title("clean code")` | Returns the matching book regardless of casing | Low | Positive / Functional |
| TC-015 | Popular book lookup with no borrow history | REQ-5 | No borrow data exists | 1. `lib.get_most_popular_book({})` | Returns `None`, no exception raised | High | Positive / Functional |

All 8 requirements are now traced to at least one test case with **zero
orphan requirements** remaining.