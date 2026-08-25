# Triage Log — Sprint 1

## Ranked Fix Order

| Rank | Issue | Severity | Priority | Decision |
|------|-------|----------|----------|----------|
| 1 | #4 Crash when finding most popular book with no borrow data | High | P1 | Fix this sprint |
| 2 | #6 Duplicate ISBN allowed | High | P1 | Fix this sprint |
| 3 | #7 Incorrect fine calculation | Medium | P2 | Fix this sprint |
| 4 | #5 Negative copies accepted when adding a book | Medium | P2 | Won't fix this sprint |
| 5 | #8 Case-sensitive title search | Low | P3 | Won't fix this sprint |

## Trade-off Reasoning

**#4 vs #6 (both High/P1):** Both crash-level or data-integrity-level issues
tied for top priority. #4 is ranked first because it causes an unhandled
exception that can crash the entire application on a common empty-state
scenario (a brand-new library with no borrow history yet). #6 is serious —
it silently corrupts data by allowing duplicate ISBNs — but it doesn't
crash anything immediately, so its damage is slower and more recoverable.
Given equal priority, we fix the one with the more immediate blast radius
first.

**#7 vs #5 (both Medium/P2):** #7 (incorrect fine calculation) is prioritized
over #5 (negative copies accepted) because #7 directly affects money — an
incorrect fine amount is a financial/business-facing error that could
confuse or upset real users. #5 produces bad data internally, but it has
no visible effect on any user-facing feature yet, so it's lower business
risk despite having the same technical severity rating.

## Deferred This Sprint

- **#5 — Negative copies accepted:** Deferred (status:wontfix this sprint).
  Low immediate business impact — no feature currently displays or acts on
  copy count in a way that breaks anything. Will revisit once inventory
  reporting is built.
- **#8 — Case-sensitive title search:** Deferred (status:wontfix this
  sprint). A workaround exists (search using exact casing), and it's a
  minor UX papercut rather than a functional blocker. Lower priority than
  fixing data integrity and crash issues first.
