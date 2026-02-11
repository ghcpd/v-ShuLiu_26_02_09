# miniprettytable

A minimal Python package for rendering table data as HTML. This project is used for testing HTML escaping options in table headers and data.

## Setup

1. Create a virtual environment and activate it:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install development dependencies:

   ```powershell
   pip install -r requirements-dev.txt
   ```

## Usage

Run the included tests to verify functionality:

```powershell
pytest
```

The tests cover HTML rendering and escaping options for headers and data cells.