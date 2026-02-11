from __future__ import annotations

from dataclasses import dataclass, field
from html import escape
from typing import Iterable, Sequence


@dataclass
class PrettyTable:
    """A tiny subset of PrettyTable-style behavior.

    This project only implements what the exercises need:
    - store field names + rows
    - render a basic HTML table via get_html_string()

    Baseline behavior: HTML output always escapes header & data.
    """

    field_names: list[str] = field(default_factory=list)
    _rows: list[list[str]] = field(default_factory=list, init=False, repr=False)

    def add_row(self, row: Sequence[object]) -> None:
        if self.field_names and len(row) != len(self.field_names):
            raise ValueError("Row length must match number of fields")
        self._rows.append(["" if v is None else str(v) for v in row])

    def add_rows(self, rows: Iterable[Sequence[object]]) -> None:
        for row in rows:
            self.add_row(row)

    def get_html_string(self, *, format: bool = False, xhtml: bool = False, escape_header: bool = True, escape_data: bool = True, **_kwargs) -> str:
        """Return an HTML representation of the table.

        Parameters (subset):
        - format: when True, include some style attributes
        - xhtml: when True, use <br/> for newlines, else <br>
        - escape_header: when True, escape HTML in header text
        - escape_data: when True, escape HTML in data cell text

        Note: baseline intentionally ignores extra kwargs.
        """

        linebreak = "<br/>" if xhtml else "<br>"
        table_attrs = ' frame="box" rules="cols"' if format else ""
        lines: list[str] = []

        lines.append(f"<table{table_attrs}>")
        lines.append("    <thead>")
        lines.append("        <tr>")

        for name in self.field_names:
            header_text = (escape(name) if escape_header else name).replace("\n", linebreak)
            if format:
                lines.append(
                    '            <th style="padding-left: 1em; padding-right: 1em; text-align: center">%s</th>'
                    % header_text
                )
            else:
                lines.append(f"            <th>{header_text}</th>")

        lines.append("        </tr>")
        lines.append("    </thead>")
        lines.append("    <tbody>")

        for row in self._rows:
            lines.append("        <tr>")
            for datum in row:
                cell_text = (escape(datum) if escape_data else datum).replace("\n", linebreak)
                if format:
                    lines.append(
                        '            <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">%s</td>'
                        % cell_text
                    )
                else:
                    lines.append(f"            <td>{cell_text}</td>")
            lines.append("        </tr>")

        lines.append("    </tbody>")
        lines.append("</table>")
        return "\n".join(lines)
