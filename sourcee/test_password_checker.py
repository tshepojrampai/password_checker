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

def test_password_digit():
    with pytest.raises(Exception, match = "password should at least have one digit"):
        pass_check.password_is_valid("Helllokitty!")
        
def test_password_char():
    with pytest.raises(Exception, match = "password should have at least one special character"):
        pass_check.password_is_valid("Helllokitty1")

#py_test:password_is_ok
def test_password_is_ok():
    assert pass_check.password_is_ok("Hell1!") == False
    assert pass_check.password_is_ok("") == False
    assert pass_check.password_is_ok("HELLOKITTY1!") == True
    assert pass_check.password_is_ok("hellokitty1!") == True 
    assert pass_check.password_is_ok("hellokiTt!") == True
    
