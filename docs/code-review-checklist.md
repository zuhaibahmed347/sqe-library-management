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
