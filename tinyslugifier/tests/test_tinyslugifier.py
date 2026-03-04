import tinyslugifier


def test_slugify_basic():
    assert tinyslugifier.slugify("Hello World!") == "hello-world"


def test_slugify_empty():
    assert tinyslugifier.slugify("") == ""
    assert tinyslugifier.slugify("   ") == ""


def test_slugify_strips_hyphens():
    assert tinyslugifier.slugify("--foo--") == "foo"
