import os

FENCE = "`" * 3
os.makedirs("docs", exist_ok=True)


def read(name):
    with open(name, encoding="utf-8", errors="replace") as f:
        return f.read().strip()


lines = [
    "# Unit Testing Notes (Lab 7)",
    "",
    "## Verbose vs. short output",
    "",
    "### python -m pytest -v tests/",
    "",
    FENCE,
    read("verbose_output.txt"),
    FENCE,
    "",
    "### python -m pytest --tb=short tests/",
    "",
    FENCE,
    read("short_output.txt"),
    FENCE,
    "",
    "**When to use each:** -v lists every test by name with its PASSED/FAILED status, so I use it",
    "to confirm exactly which cases ran (for example the parametrized ids) and as evidence in a",
    "submission. --tb=short trims failure tracebacks to the essential lines, so I use it when many",
    "tests fail and I need to scan errors quickly, or when reading CI logs.",
    "",
    "## Fixture scopes",
    "",
    "- **function (default):** a fresh object for every test. Used for library and",
    "  populated_library, because tests mutate them and must stay independent of each other.",
    "- **module:** built once per test file. Used for catalog_data, which is read-only seed data,",
    "  so sharing it is safe and avoids repeating setup.",
    "",
]

with open("docs/unit-testing-notes.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("written docs/unit-testing-notes.md")
