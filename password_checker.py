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
	
	
