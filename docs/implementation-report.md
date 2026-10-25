# Bug-Fix and Popularity Feature Report

## Scope

- Bug A: reject negative and non-integer `Book.copies`.
- Bug B: make `Library.search_by_title` case-insensitive.
- Bug C: reject invalid ISBN values during `Book` construction.
- Feature: add `rank_books_by_popularity(library)`.

## Issue tracking

- [Issue #20](https://github.com/zuhaibahmed347/sqe-library-management/issues/20): negative copies and case-sensitive title search.
- [Issue #21](https://github.com/zuhaibahmed347/sqe-library-management/issues/21): invalid ISBN accepted by `Book`.
- [Issue #22](https://github.com/zuhaibahmed347/sqe-library-management/issues/22): popularity ranking feature.
- [Issue #23](https://github.com/zuhaibahmed347/sqe-library-management/issues/23): consolidated Bug A/B tracking issue.

All issues include severity, priority, and acceptance-criteria checklists and use the `bug` label.

## Reproduction evidence

The initial regression tests failed before implementation:

- Bug A: negative, floating-point, and string copy counts did not raise `ValueError`.
- Bug B: `"clean code"` and `"CLEAN CODE"` returned no result for `"Clean Code"`.
- Bug C: `"abc"`, an empty ISBN, and a 12-digit ISBN did not raise `ValueError`.

The failures were captured in the red test commits before their corresponding fixes.

## Branch and PR workflow

### PR 1: Bugs A and B

- Branch: `bugfix/copies-and-search`, created from the old `main`.
- PR: [#24](https://github.com/zuhaibahmed347/sqe-library-management/pull/24).
- Red tests were added first, then implementation was committed separately.
- The WIP/test/fix history was squashed with `git rebase -i` into
  `840bc2d fix(copies-search): validate copies and normalize title search`.
- Review included four inline comments: praise, suggestion, casefold rationale, and
  accepted-boundary coverage.
- The requested helper extraction and boundary tests were implemented in
  `6c49f13`.

GitHub does not allow the PR author to submit formal `REQUEST_CHANGES` or
`APPROVE` reviews on their own pull request. Both transitions were attempted
and rejected by GitHub; the review follow-up was recorded as a PR comment.

### PR 2: Bug C and popularity feature

- Branch: `feature/rank-books-popularity`, created from the old `main` lineage.
- PR: [#25](https://github.com/zuhaibahmed347/sqe-library-management/pull/25).
- PR 1 was merged first, so merging `origin/main` into this branch produced a
  real conflict in `src/library.py`.
- The conflict was resolved by retaining both ISBN and copy validation,
  case-insensitive search, and popularity ranking.
- The resolution was committed as
  `84b7845 merge: resolve rank and copies validation conflict`.

## TDD audit

The popularity feature has five red-green cycles, with red and green kept in
separate commits:

1. Empty catalog: `35150fe` red, `a934e37` green.
2. Single book: `3ab5fce` red, `43043c6` implementation continued.
3. Borrow-count descending order: `38bc0c5` red, `43043c6` green.
4. Alphabetical ties: `740b773` red, `40bcbcc` green.
5. Case-insensitive alphabetical ties: `a923c86` red, `3163733` green.

The branch contains more than ten commits, including separate Bug C red/green
commits and the explicit conflict-resolution merge. The final implementation
sorts by `(-times_borrowed, title.casefold())`.

## Final verification

After both PRs were merged, the full suite was run on `main`:

```text
52 passed
```

The focused Bug A/B and Bug C/ranking suites also passed independently before
the final merge.
