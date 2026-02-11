from __future__ import annotations

from prettytable import PrettyTable


def test_get_string_row_filter_filters_rows() -> None:
    table = PrettyTable(["A", "C"])
    table.add_row(["keep", 1])
    table.add_row(["drop", 0])

    output = table.get_string(row_filter=lambda row: row[1] == 1)

    assert "keep" in output
    assert "drop" not in output


def test_row_filter_applies_after_slicing() -> None:
    table = PrettyTable(["A", "C"])
    table.add_row(["r1", 0])
    table.add_row(["r2", 0])
    table.add_row(["r3", 1])

    # If filtering is applied BEFORE slicing, r3 could shift into the slice and appear.
    # Filtering must apply AFTER slicing, so only the sliced rows are candidates.
    output = table.get_string(start=0, end=2, row_filter=lambda row: row[1] == 1)

    assert "r1" not in output
    assert "r2" not in output
    assert "r3" not in output
