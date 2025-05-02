import pytest
from convert import convert_text

def test_to_uppercase():
    """Test dla konwersji na wielkie litery."""
    assert convert_text("hello", "/toupper") == "HELLO"
    assert convert_text("Python", "/toupper") == "PYTHON"
    assert convert_text("123abc", "/toupper") == "123ABC"
    assert convert_text("", "/toupper") == ""  # Test pustego napisu

def test_to_lowercase():
    """Test dla konwersji na małe litery."""
    assert convert_text("HELLO", "/tolower") == "hello"
    assert convert_text("Python", "/tolower") == "python"
    assert convert_text("123ABC", "/tolower") == "123abc"
    assert convert_text("", "/tolower") == ""  # Test pustego napisu

def test_default_behavior():
    """Test dla domyślnego trybu (czyli `/toupper`)."""
    assert convert_text("hello") == "HELLO"
    assert convert_text("Python") == "PYTHON"
    assert convert_text("123abc") == "123ABC"

if __name__ == "__main__":
    pytest.main()


# version 1

# import pytest
# from uppercase import to_uppercase

# def test_to_uppercase():
#     assert to_uppercase("hello") == "HELLO"
#     assert to_uppercase("Python") == "PYTHON"
#     assert to_uppercase("123abc") == "123ABC"
#     assert to_uppercase("") == ""  # Test pustego napisu

# if __name__ == "__main__":
#     pytest.main()
