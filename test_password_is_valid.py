import pytest
import password_checker as pass_check

#py_test: password is valid

def test_password_exists():
    with pytest.raises(Exception, match = "password should exist"):
        pass_check.password_is_valid("")

def test_password_len():
    with pytest.raises(Exception, match = "password should be longer than than 8 characters"):
        pass_check.password_is_valid("Hell1!")
