#This is a program for password checker

import re
password= input("insert your password: ")

# Defining  the function for the password

def password_is_valid(password):
    #Checking the if the password exists
    if len(password) == 0:
        raise Exception("password should exist")
    else: 
        # Checking the length of the password
        if len(password)<=8:
            
            raise Exception("password should be longer than than 8 characters")
        #Checking for a lowercase in password
        
        elif not re.search('[a-z]', password):
            raise Exception('password should have at least one lowercase letter')
            
       #Checking for a UPPERcase in password
        elif not re.search('[A-Z]', password):
            raise Exception ('password should have at least one uppercase letter')
       #Checking for a digit in password
        elif not re.search('[0-9]', password):
            raise Exception('password should at least have one digit')
       #Checking for a characters in password 
        else:
            if not re.search("[$&+,:;=?@#|'<>.-^*()%!]", password):
                raise Exception('password should have at least one special character')
        
password_is_valid(password)