# Code Review Checklist

## Correctness
- [ ] The change implements the stated behavior and acceptance criteria.
- [ ] Boundary values and empty or single-item inputs are handled correctly.
- [ ] Invalid and missing inputs produce clear, consistent errors.

## Tests
- [ ] Tests cover normal behavior and relevant edge cases.
- [ ] Tests fail for the original bug and verify observable behavior.
- [ ] Test names and assertions clearly identify the scenario.

## Readability
- [ ] Names are descriptive and follow existing project conventions.
- [ ] Functions and branches are easy to follow.
- [ ] Public behavior is documented when a docstring or comment is useful.

## Design
- [ ] The implementation fits existing module APIs and responsibilities.
- [ ] Logic is not unnecessarily duplicated or tightly coupled.
- [ ] Changes preserve compatibility with existing callers.

## Risk
- [ ] The change does not introduce data loss or unsafe state mutations.
- [ ] Performance and complexity are appropriate for the input size.
- [ ] Backwards compatibility and exception behavior are considered.

## Lessons Learned

The correctness checkpoint for boundary values caught the most valuable issue:
the percentile denominator had to use `N - 1` so the highest-ranked member maps
to 100 rather than `(N - 1) / N * 100`. For the next review cycle, I would add
a checklist item for tie and duplicate-value semantics, especially for ranking
functions where equal scores must receive a clearly specified percentile.

## Pull Request Evidence

- PR: https://github.com/zuhaibahmed347/sqe-library-management/pull/29
- Flawed commit: `167e7a5` (`feat: add member loyalty percentile`)
- Fix commit: `fdd8482` (`fix: address borrow percentile review feedback`)
- The PR contains six inline review comments, including a suggestion block for
  the off-by-one correction.
- Final verification: `68 passed`, with `100%` source coverage.
- GitHub does not permit a pull-request author to submit `REQUEST_CHANGES` or
  `APPROVE` reviews on their own PR. The structured review summary was therefore
  posted in the PR conversation, and the same account-blocked limitation applies
  to the final approval action.
