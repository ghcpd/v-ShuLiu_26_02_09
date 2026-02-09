# miniprettytable

A minimal Python library for rendering simple tables as HTML. This project is a lightweight subset of the PrettyTable package, focusing on storing field names and rows and generating safe or unescaped HTML output.

## Features

- Store field names and rows
- Generate HTML tables via `PrettyTable.get_html_string()`
- Configurable HTML escaping for headers and data cells
- Optional formatted output with inline styles

## Requirements

- Python 3.10+

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install development dependencies:

   ```powershell
   pip install -r requirements-dev.txt
   ```

## Running Tests

Execute the test suite using `pytest`:

```powershell
pytest
```

All tests should pass, confirming correct behavior of HTML escaping options.

## Usage

```python
from miniprettytable import PrettyTable

t = PrettyTable(field_names=["Name","Value"])
t.add_row(["<em>HTML</em>", "<b>bold</b>"])

# Default escapes both headers and data
html = t.get_html_string()

# Disable escaping for headers only
html_no_header_escape = t.get_html_string(escape_header=False)

# Disable escaping for data only
html_no_data_escape = t.get_html_string(escape_data=False)
```

## License

MIT License. See `LICENSE` for details.