## Boundary Value Analysis — fine_tier()

| Boundary | value-1 | value | value+1 | Expected |
|---|---|---|---|---|
| Domain edge / None→Low | -1 | 0 | 1 | -1: ValueError, 0: "None", 1: "Low" |
| Low→Medium | 7 | 8 | 9 | "Low", "Medium", "Medium" |
| Medium→High | 14 | 15 | 16 | "Medium", "High", "High" |
| High→Severe | 30 | 31 | 32 | "High", "Severe", "Severe" |
