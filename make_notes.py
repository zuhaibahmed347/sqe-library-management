import os

os.makedirs("docs", exist_ok=True)

def read(name):
    with open(name, encoding="utf-8", errors="replace") as f:
        return f.read().strip()

notes = f"""# Unit Testing Notes (Lab 7)

## Verbose vs. short output

### `python -m pytest -v tests/`
