Test Plan — LibraryHub
1. Introduction

This document defines the scope, approach, and criteria for testing the
LibraryHub module (src/library.py), which handles book cataloging,
member management, borrowing/returns, and fine calculation. It follows
the IEEE 829 test plan structure.

2. Test Items
Book class (ISBN, title, author, copy count)
Library class: add_book(), search_by_title(), get_most_popular_book(), calculate_fine()
Member class and borrowing/return behavior (planned)
3. Features to be Tested
Adding books (valid, duplicate ISBN, malformed ISBN, negative copies)
Searching books by title (case-insensitive)
Fine calculation across day ranges and boundaries
Borrowing and returning books, including limit enforcement
Popular-book lookup with empty borrow history
4. Features Not to be Tested
UI is out of scope for this document — LibraryHub is a backend library module with no user interface; visual/UX testing does not apply here.
Database persistence layer — not yet implemented in the current codebase.
5. Approach

Testing will be primarily manual, executing each test case against
the current codebase via a Python shell or small test scripts. Where
GitHub Actions CI is configured, applicable test cases will be
automated in future sprints. Negative/error-path cases are prioritized
alongside happy-path cases.

6. Pass/Fail Criteria

A test cycle is considered successful when:

95% of planned test cases pass
Zero Critical severity defects remain open
All High severity defects have a linked GitHub Issue
7. Test Deliverables
docs/test-plan.md (this document)
docs/test-cases.md
docs/rtm.md
Execution results log with linked defect issues
8. Environmental Needs
Python 3.x runtime
Local clone of sqe-library-management on main branch
GitHub access for issue filing
9. Schedule
Test Plan authored: September 1, 2026
Test cases written: within 1 day of plan
RTM built: within 1 day of test cases
Manual execution pass: within 1 day of RTM completion
10. Risks
Borrow/return/member-limit functionality does not yet exist in code, so those test cases will fail by design until implemented (tracked as known gaps, not defects).
Manual execution is time-consuming and error-prone compared to automated testing; mitigated by clear, repeatable step definitions.