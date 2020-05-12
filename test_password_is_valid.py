import pytest
import password_checker as pass_check

#py_test: password is valid

def test_password_exists():
    with pytest.raises(Exception, match = "password should exist"):
        pass_check.password_is_valid("")
