import pytest
import salt.modules.test as testmod
import saltext.mongodb.modules.mongodb_mod as mongodb_module
import saltext.mongodb.states.mongodb_mod as mongodb_state


@pytest.fixture
def configure_loader_modules():
    return {
        mongodb_module: {
            "__salt__": {
                "test.echo": testmod.echo,
            },
        },
        mongodb_state: {
            "__salt__": {
                "mongodb.example_function": mongodb_module.example_function,
            },
        },
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    expected = {
        "name": echo_str,
        "changes": {},
        "result": True,
        "comment": f"The 'mongodb.example_function' returned: '{echo_str}'",
    }
    assert mongodb_state.exampled(echo_str) == expected
