# Automated Test Coverage

## Baseline

The baseline command was run before adding the gap tests:

```text
py -m pytest -p pytest_cov.plugin --cov=src --cov-branch --cov-report=term-missing --cov-report=html
```

The suite passed all 52 tests. The baseline report for `src/library.py` was:

| File | Line coverage | Statements | Missing | Branch coverage | Branches | Partial | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `src/library.py` | 87% | 78 | 10 | 79% | 28 | 2 | 85% |

The baseline HTML report is available at `htmlcov/index.html`. Its missing lines
were 25, 33-35, 38-40, 80, and 98-99. Because this project has one source
module, the three weakest areas were treated as the three weakest functions:
`add_book`, `get_most_popular_book`/`calculate_fine`, and
`validate_isbn`/`Member.__init__`.

## Gap closure

`tests/test_coverage_gaps.py` now covers duplicate ISBN rejection, both empty
and populated popularity lookups, both fine-calculation branches, non-happy
object initialization, and the `Member` constructor. The borrow-limit test now
also verifies the updated count instead of only the success flag.

The final HTML report is generated at `htmlcov/index.html` after the updated
suite runs. The final report is expected to show all executable lines and
branches in `src/library.py` covered.

## Final results

After the changes:

```text
59 passed
src/library.py      78     0     28      0   100%
TOTAL               78     0     28      0   100%
```

The final report is 100% for both lines and branches (and 100% combined).

The project enforces an 85% minimum through `pytest.ini`, so a future
regression below the agreed threshold fails pytest.

## Coverage versus quality

The original `test_borrow_at_four_books_succeeds` asserted only that
`borrow_book` returned `True`. That assertion executed the success path and
therefore contributed to line coverage, but it did not verify the important
state change: the member's borrow count must increase from four to five.
This was a coverage trap because the implementation could return `True` while
forgetting to update `borrowed_counts` and the test would still pass.

The test now asserts both the return value and
`library.borrowed_counts["m1"] == 5`. Coverage identifies untested code, but
the state assertion checks that the exercised behavior is correct.

## Reports and screenshots

The HTML summary and per-file details are generated in `htmlcov/`. The
terminal summary above records the before/after measurements; screenshots of
the baseline and final summary should be captured from `htmlcov/index.html`
when submitting the lab.
