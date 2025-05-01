import pytest
from uppercase import to_uppercase

def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
    assert to_uppercase("Python") == "PYTHON"
    assert to_uppercase("123abc") == "123ABC"
    assert to_uppercase("") == ""  # Test pustego napisu

if __name__ == "__main__":
    pytest.main()
