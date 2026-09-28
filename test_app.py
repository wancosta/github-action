from app import hello


def test_hello():
    assert hello() == "Hello from my first CI/CD pipeline"


def test_hello_is_string():
    assert isinstance(hello(), str)
