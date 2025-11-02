from src.hello import greet


def test_greet():
    assert greet("Ada", True) == "Hola, Ada 👋"
    assert greet("Ada", False) == "Hola, Ada "
