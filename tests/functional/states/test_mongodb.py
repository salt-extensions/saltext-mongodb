import pytest

pytestmark = [
    pytest.mark.requires_salt_states("mongodb.exampled"),
]


@pytest.fixture
def mongodb(states):
    return states.mongodb


def test_replace_this_this_with_something_meaningful(mongodb):
    echo_str = "Echoed!"
    ret = mongodb.exampled(echo_str)
    assert ret.result
    assert not ret.changes
    assert echo_str in ret.comment
