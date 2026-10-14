import pytest

from slugkit import slugify


def test_issue_example_punctuation_and_repeated_whitespace():
    assert slugify("Hello,  World!") == "hello-world"


def test_runs_of_non_alphanumerics_collapse_to_single_hyphen():
    assert slugify("a   b") == "a-b"
    assert slugify("a---b") == "a-b"
    assert slugify("a, ;!b") == "a-b"


def test_no_leading_or_trailing_hyphens():
    assert slugify("!!!Hello World???") == "hello-world"
    assert slugify("  spaced out  ") == "spaced-out"


@pytest.mark.parametrize("text", ["Hello,  World!", "--foo--bar--", " a . b . c "])
def test_output_has_no_double_or_edge_hyphens(text):
    result = slugify(text)
    assert "--" not in result
    assert not result.startswith("-")
    assert not result.endswith("-")
