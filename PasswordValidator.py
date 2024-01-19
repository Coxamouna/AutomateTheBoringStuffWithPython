import re

def isPasswordValid(password):
    if len(password) < 8:
        return False    
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False    
    return True

assert(isPasswordValid("Abcd1234") == True)  # Strong password
assert(isPasswordValid("abc123") == False)   # Not strong (missing uppercase)
assert(isPasswordValid("ABCD1234") == False) # Not strong (missing lowercase)
assert(isPasswordValid("abcdefg") == False)  # Not strong (missing digits)