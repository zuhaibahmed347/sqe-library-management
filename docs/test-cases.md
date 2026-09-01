\# Test Cases — LibraryHub



| ID | Title | Requirement | Preconditions | Steps | Expected | Priority | Type |

|----|-------|-------------|----------------|-------|----------|----------|------|

| TC-001 | Add book with valid new ISBN | REQ-1 | Catalog does not contain ISBN 9780134685991 | 1. `lib = Library()`<br>2. `lib.add\_book(Book("9780134685991", "Effective Java", "J. Bloch", 3))` | Book is added successfully; `lib.books` contains 1 entry with that ISBN | High | Positive / Functional |

| TC-002 | Reject duplicate ISBN on add\_book | REQ-1 | Catalog already contains ISBN 9780132350884 | 1. `lib.add\_book(Book("9780132350884", "Copy", "X", 1))` | `ValueError` is raised; catalog still has exactly one entry with that ISBN | High | Negative / Functional |

| TC-003 | Reject malformed ISBN on add\_book | REQ-1 | Library is empty | 1. `lib.add\_book(Book("abc-not-an-isbn", "Bad Book", "X", 2))` | System should raise a validation error for an invalid ISBN format | High | Negative / Functional |

| TC-004 | Borrow book when copies are available | REQ-6 | Book with ISBN X has 2 copies available | 1. `lib.borrow\_book(member\_id, "X")` | Borrow succeeds; available copies for that ISBN decreases by 1 | High | Positive / Functional |

| TC-005 | Borrow book when no copies are available | REQ-6 | Book with ISBN X has 0 copies available | 1. `lib.borrow\_book(member\_id, "X")` | System raises an error or returns failure; no copy is deducted (can't go negative) | High | Negative / Functional |

| TC-006 | Return a book currently on loan | REQ-7 | Member has borrowed book ISBN X | 1. `lib.return\_book(member\_id, "X")` | Return succeeds; available copies for ISBN X increases by 1 | Medium | Positive / Functional |

| TC-007 | Return a book not on loan by that member | REQ-7 | Member has NOT borrowed book ISBN X | 1. `lib.return\_book(member\_id, "X")` | System raises an error; no copy count is affected | High | Negative / Functional |

| TC-008 | Member borrowing at the allowed limit | REQ-8 | Member has borrowed (limit − 1) books already | 1. `lib.borrow\_book(member\_id, "Y")` | Borrow succeeds; member is now at the limit | Medium | Positive / Functional |

| TC-009 | Member borrowing beyond the allowed limit | REQ-8 | Member has already borrowed the maximum allowed books | 1. `lib.borrow\_book(member\_id, "Z")` | System raises an error; borrow is rejected | High | Negative / Functional |

| TC-010 | Fine calculation for zero days overdue | REQ-4 | None | 1. `lib.calculate\_fine(0)` | Returns `0.0` | Medium | Positive / Boundary |

| TC-011 | Fine calculation for a mid-range overdue period | REQ-4 | None | 1. `lib.calculate\_fine(10)` | Returns `5.0` (10 × 0.5) | Medium | Positive / Functional |

| TC-012 | Fine calculation at overdue boundary (negative days) | REQ-4 | None | 1. `lib.calculate\_fine(-1)` | Returns `0.0` (no negative fines; guard clause from Lab 3 fix applies) | Medium | Negative / Boundary |



\*\*Negative/error-path tests:\*\* TC-002, TC-003, TC-005, TC-007, TC-009, TC-012 (6 of 12 — exceeds the minimum of 3).

