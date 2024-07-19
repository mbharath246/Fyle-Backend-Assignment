from core.libs import assertions
from core.libs.exceptions import FyleError


def test_assert_auth():
    assertions.assert_auth(True)
    try:
        assertions.assert_auth(False)
    except FyleError as e:
        assert e.status_code == 401


def test_assert_true():
    assertions.assert_true(True)
    try:
        assertions.assert_true(False)
    except FyleError as e:
        assert e.status_code == 403