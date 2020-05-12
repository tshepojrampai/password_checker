import pytest
import password_checker as pass_check

#py_test: password is valid

def test_password_exists():
    with pytest.raises(Exception, match = "password should exist"):
        pass_check.password_is_valid("")

def test_password_len():
    with pytest.raises(Exception, match = "password should be longer than than 8 characters"):
        pass_check.password_is_valid("Hell1!")

def test_password_lowcase():
    with pytest.raises(Exception, match = "password should have at least one lowercase letter"):
        pass_check.password_is_valid("HELLOKITTY1!")
def test_password_uppcase():
    with pytest.raises(Exception, match = "password should have at least one uppercase letter"):
        pass_check.password_is_valid("hellokitty1!")
