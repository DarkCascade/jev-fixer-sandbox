from slugkit import slugify


def test_basic():
    assert slugify("Hello World") == "hello-world"


def test_lowercases():
    assert slugify("ABC") == "abc"
