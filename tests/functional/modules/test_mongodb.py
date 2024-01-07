import pytest

pytestmark = [
    pytest.mark.requires_salt_modules("mongodb.example_function"),
]


@pytest.fixture
def mongodb(modules):
    return modules.mongodb


def test_replace_this_this_with_something_meaningful(mongodb):
    echo_str = "Echoed!"
    res = mongodb.example_function(echo_str)
    assert res == echo_str
