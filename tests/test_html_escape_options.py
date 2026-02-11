from miniprettytable import PrettyTable


def _table_with_html_in_header_and_data() -> PrettyTable:
    t = PrettyTable(field_names=["", "Field 1", "<em>Field 2</em>", "<a href='#'>Field 3</a>"])
    t.add_row([1, "value 1", "value2", "value3"])
    t.add_row([2, "<b>value 2</b>", "<span style='text-decoration: underline;'>v</span>", "<a href='#'>x</a>"])
    return t


def test_default_escapes_header_and_data_simple_html() -> None:
    t = _table_with_html_in_header_and_data()
    html = t.get_html_string()

    # default behavior must keep escaping (security-friendly)
    assert "&lt;em&gt;Field 2&lt;/em&gt;" in html
    assert "&lt;a href=&#x27;#&#x27;&gt;Field 3&lt;/a&gt;" in html
    assert "&lt;b&gt;value 2&lt;/b&gt;" in html


def test_explicit_true_matches_default() -> None:
    t = _table_with_html_in_header_and_data()
    html = t.get_html_string(escape_header=True, escape_data=True)
    assert "&lt;em&gt;Field 2&lt;/em&gt;" in html
    assert "&lt;b&gt;value 2&lt;/b&gt;" in html


def test_can_disable_header_escaping_simple_html() -> None:
    t = _table_with_html_in_header_and_data()

    # PR 305 behavior: allow disabling escaping for headers
    html = t.get_html_string(escape_header=False)
    assert "<em>Field 2</em>" in html
    assert "<a href='#'>Field 3</a>" in html

    # Data should still be escaped by default
    assert "&lt;b&gt;value 2&lt;/b&gt;" in html


def test_can_disable_header_escaping_formatted_html() -> None:
    t = _table_with_html_in_header_and_data()

    html = t.get_html_string(format=True, escape_header=False)
    assert "<em>Field 2</em>" in html
    assert "<a href='#'>Field 3</a>" in html


def test_can_disable_data_escaping_formatted_html() -> None:
    t = _table_with_html_in_header_and_data()

    # PR 305 behavior: allow disabling escaping for data
    html = t.get_html_string(format=True, escape_data=False)
    assert "<b>value 2</b>" in html
    assert "<span style='text-decoration: underline;'>v</span>" in html
    assert "<a href='#'>x</a>" in html

    # Header should still be escaped by default
    assert "&lt;em&gt;Field 2&lt;/em&gt;" in html


def test_can_disable_data_escaping_simple_html() -> None:
    t = _table_with_html_in_header_and_data()

    html = t.get_html_string(escape_data=False)
    assert "<b>value 2</b>" in html
    assert "<span style='text-decoration: underline;'>v</span>" in html
    assert "<a href='#'>x</a>" in html
