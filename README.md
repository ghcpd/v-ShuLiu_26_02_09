# MiniPrettyTable

A lightweight Python library that implements a minimal subset of PrettyTable-style behavior, providing simple HTML table generation with optional HTML escaping controls.

## Features

- Store field names and row data
- Generate HTML table output via `get_html_string()`
- Control HTML escaping for headers and data independently
- Support for both simple and formatted (styled) HTML output

## Setup Instructions

### Create and Activate a Virtual Environment

```powershell
# Create virtual environment
python -m venv .venv

# Activate it (Windows PowerShell)
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```powershell
pip install -r requirements-dev.txt
```

## Running Tests

```powershell
pytest
```

All tests should pass with exit code 0.

## Usage

### Basic Example

```python
from miniprettytable import PrettyTable

# Create a table with field names
table = PrettyTable(field_names=["Name", "Value"])

# Add rows
table.add_row(["Item 1", "<em>emphasized</em>"])
table.add_row(["Item 2", "<b>bold</b>"])

# Get HTML with default escaping (safe)
html = table.get_html_string()
# Output: &lt;em&gt;emphasized&lt;/em&gt;, &lt;b&gt;bold&lt;/b&gt;

# Disable header escaping to allow markup in headers
html = table.get_html_string(escape_header=False)

# Disable data escaping to allow markup in cells
html = table.get_html_string(escape_data=False)

# Use formatted mode with styling
html = table.get_html_string(format=True)

# Combine options
html = table.get_html_string(format=True, escape_header=False, escape_data=False)
```

## API Reference

### `get_html_string()` Parameters

- `format` (bool, default=False): When True, includes CSS style attributes for better formatting
- `xhtml` (bool, default=False): When True, uses `<br/>` for newlines instead of `<br>`
- `escape_header` (bool, default=True): When False, preserves HTML markup in header text
- `escape_data` (bool, default=True): When False, preserves HTML markup in data cell text

## Security Notes

- By default, all HTML in headers and data is escaped for security
- Only disable escaping (`escape_header=False`, `escape_data=False`) for trusted content
- User input with escaping disabled can introduce XSS vulnerabilities

## Environment Requirements

- Python 3.10+
- Dependencies listed in `requirements-dev.txt`
