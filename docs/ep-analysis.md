# Equivalence Partitioning Analysis — LibraryHub

## Input 1: `days_overdue` → `fine_tier()`

| Class | Range | Representative | Expected |
|-------|-------|-----------------|----------|
| Invalid | < 0 | -3 | ValueError |
| None | 0 | 0 | "None" |
| Low | 1–7 | 4 | "Low" |
| Medium | 8–14 | 10 | "Medium" |
| High | 15–30 | 20 | "High" |
| Severe | 31+ | 45 | "Severe" |

## Input 2: Books on loan per member → `borrow_book()`

| Class | Range | Representative | Expected |
|-------|-------|-----------------|----------|
| Valid | 0–5 books | 3 | Borrow succeeds |
| Invalid | 6+ books | 5 (attempting 6th) | ValueError raised |

## Input 3: ISBN field → `validate_isbn()`

| Class | Description | Representative | Expected |
|-------|--------------|-----------------|----------|
| Valid | Exactly 13 numeric digits | "9780134685991" | Returns True |
| Empty | Empty string | "" | ValueError |
| Too short | Fewer than 13 digits | "12345" | ValueError |
| Invalid chars | Contains letters/symbols | "abc-not-an-isbn" | ValueError |

## Limitation of Equivalence Partitioning

EP is effective at reducing redundant test cases by grouping inputs
that should behave identically, but it does not specifically target
the edges of each class. For example, EP alone would not distinguish
between `days_overdue = 7` (Low) and `days_overdue = 8` (Medium) —
an off-by-one error in the boundary condition (e.g. `<=7` mistakenly
written as `<7`) could pass all EP tests above while still being
wrong exactly at the class boundary. This gap is addressed in Lab 6
using Boundary Value Analysis, which explicitly tests values at and
just around each class boundary.

## Test Execution Summary
