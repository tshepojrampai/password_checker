#This is a program for password checker

import re

# Defining  the function for the password
def password_is_valid(password):

    #Checking if the password exists
    if len(password) == 0:
        raise Exception ("password should exist")
    else: # first condition has been met if this gets executed
        
        # length of the password
        if len(password)<=8:
            raise Exception("password should be longer than than 8 characters")
	
      # lowercase in password
        elif not re.search('[a-z]', password):

            raise Exception('password should have at least one lowercase letter')	
       # UPPERcase in password
        elif not re.search('[A-Z]', password):
            raise Exception('password should have at least one uppercase letter')
        # digit in password
        elif not re.search('[0-9]', password):
            raise Exception('password should at least have one digit')

       #character(s) in password 
        elif  not re.search("[!@#$%^&*()_+:;'{}[]|\;'<>?/.,]", password):
            raise Exception('password should have at least one special character')
        else:
            return True
