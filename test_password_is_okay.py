import pytest
import password_checker as pass_check

#py_test:password_is_ok
def test_password_is_ok():
    assert pass_check.password_is_ok("Hell1!") == False
    assert pass_check.password_is_ok("") == False
    assert pass_check.password_is_ok("HELLOKITTY1!") == True
    assert pass_check.password_is_ok("hellokitty1!") == True 
    assert pass_check.password_is_ok("hellokiTt!") == True
