import pytest
from unittest.mock import mock_open, patch
from src.library import LibraryIOError


def test_export_catalog_writes_expected_content(populated_library):
    m = mock_open()
    with patch("builtins.open", m):
        populated_library.export_catalog("catalog.csv")

    m.assert_called_once_with("catalog.csv", "w")
    expected = (
        "9780132350884,Clean Code,R. Martin,2\n"
        "9780135957059,The Pragmatic Programmer,D. Thomas,1"
    )
    m.return_value.write.assert_called_once_with(expected)


def test_export_catalog_raises_custom_error_on_oserror(populated_library):
    with patch("builtins.open", side_effect=OSError("disk full")):
        with pytest.raises(LibraryIOError) as exc_info:
            populated_library.export_catalog("catalog.csv")

    assert "catalog.csv" in str(exc_info.value)
    assert isinstance(exc_info.value.__cause__, OSError)
